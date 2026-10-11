"""ЧЕРНОВИК v0 (2026-10-10, сессия archive-recon, запись Р-21 LOG.md). Не принят: проверен только сверкой
с темами старой таблицы (330 из 414 совпадений) и на 462 медицинских PDF «AA Beruf» (тема у 410).
Запуск: python topics.py <files.csv> <папка texts> <topics.csv>. Выход topics.csv — НЕ в repo (пути владельца).
Раскладка тем по тексту первых страниц. Папки владельца не используются.
Вход: files.csv (опись archive_scan.py), папка texts/. Выход: topics.csv.
Тема = словарь терминов (нем./англ.). Счёт: попадания в тексте (не больше 5 на термин)
+ попадания в названии (CrossRef или имя файла) с весом 6. Термин-аббревиатура
(в верхнем регистре) ищется с учётом регистра и по границам слова — чтобы «ards»
внутри «Standards» не давало ARDS.
"""
import csv, re, sys, os, collections

TOPICS = {
 'Sepsis': ['sepsis','septisch','septic','sofa-score','qsofa','procalcitonin','laktat','lactate','vasopressor','noradrenalin','norepinephrine','surviving sepsis','fokussanierung'],
 'ANTIBIOTIKA': ['antibiot','antiinfektiv','antimikrob','antimicrob','stewardship','resistenz','resistance','mrsa','vre','esbl','carbapenem','penicillin','cephalosporin','vancomycin','staphylococcus','staph. aureus','infektiolog','pilzinfektion','antimykot','antiviral','erreger','pathogen'],
 'Beatmung': ['beatmung','ventilation','beatmet','ARDS','lungenversagen','respiratory failure','respiratorische insuffizienz','peep','tidalvolumen','tidal volume','weaning','entwöhnung','ecmo','extrakorporal','niv','high-flow','highflow','oxygenierung','oxygenation','intubation','atemweg','airway','tracheotomie','tracheostomy'],
 'Delir': ['delir','delirium','kognitiv','cognitive dysfunction','postoperative cognitive','agitation','verwirrtheit'],
 'Sedierung': ['sedierung','sedation','analgosedierung','propofol','midazolam','dexmedetomidin','ketamin','rass','sedativ'],
 'Kardiologie': ['kardial','cardiac','herzinsuffizienz','heart failure','myokardinfarkt','myocardial infarction','koronar','coronary','vorhofflimmern','atrial fibrillation','rhythmusstörung','arrhythm','endokarditis','endocarditis','herzklappe','aortenstenose','kardiogen','cardiogenic','ekg','ecg','acs','stemi'],
 'Reanimation': ['reanimation','resuscitation','herzstillstand','kreislaufstillstand','cardiac arrest','cpr','ecpr','defibrillation','advanced life support','ALS','ERC','rosc','postreanimation'],
 'Polytrauma': ['polytrauma','schwerverletzt','trauma','verletzung','injury','unfall','fraktur','fracture','beckenfraktur','schädel-hirn-trauma','traumatic brain','atls','damage control'],
 'SchockRaum': ['schockraum','emergency department','notaufnahme','trauma bay','resuscitation room','schockraummanagement','zentrale notaufnahme'],
 'TransfusuonsMedizin': ['transfusion','erythrozyt','red blood cell','thrombozyt','platelet','plasma','gerinnung','koagulopathie','coagulopathy','coagulation','hämostase','haemostasis','hemostasis','rotem','teg','viskoelast','viscoelast','fibrinogen','tranexam','blutung','bleeding','hämorrhag','haemorrhag','hemorrhag','patient blood management','massivtransfusion','gerinnungsfaktor','antikoagul','anticoagul'],
 'Notarzt': ['notarzt','rettungsdienst','präklinisch','prähospital','prehospital','emergency medical service','ems','einsatz','rettungswagen','leitstelle','notfallsanitäter','luftrettung'],
 'Leitender NA': ['leitender notarzt','leitende notärzt','massenanfall','manv','großschadenslage','katastrophen','sichtung','triage','mass casualty'],
 'Regionale A': ['regionalanästhesie','regional anesthesia','regional anaesthesia','nervenblockade','nerve block','plexus','spinalanästhesie','spinal anesthesia','periduralanästhesie','epidural','rückenmarksnah','neuraxial','lokalanästhetik','local anesthetic','ultraschallgesteuert'],
 'Schmerztherapie': ['schmerz','pain','analgesie','analgesia','opioid','opiat','nsar','metamizol','paracetamol','piritramid','morphin','chronischer schmerz'],
 'Allgemeine Anästhesiologie': ['anästhesie','anaesthesia','anesthesia','narkose','allgemeinanästhesie','prämedikation','präoperativ','preoperative','perioperativ','perioperative','aufwachraum','muskelrelax','neuromuscular','volatile','tiva','ponv','aspiration','asa-'],
 'Allgemeine Chirurgie': ['chirurg','surgery','surgical','laparotomie','laparoskop','akutes abdomen','acute abdomen','ileus','peritonitis','appendizit','cholezyst','darm','bowel'],
 'Thorax': ['thorax','thoraxdrainage','chest tube','pneumothorax','pleuraerguss','pleural effusion','thoraxchirurgie','thoracic','lungenresektion','einlungenventilation','one-lung'],
 'Neurochirurgie': ['neurochirurg','neurosurg','subarachnoidal','subarachnoid','aneurysma','aneurysm','intrakraniell','intracranial','hirndruck','schädel-hirn','hydrozephalus','liquor','hirnblutung','intracerebral','kraniotomie','craniotomy'],
 'Medikamente': ['pharmakolog','pharmacolog','pharmakokinetik','pharmacokinetic','arzneimittel','medikament','dosierung','dosing','wechselwirkung','interaction','drug'],
 'Physiologie': ['physiologie','physiology','pathophysiolog','sauerstofftransport','oxygen delivery','säure-basen','acid-base','hämodynamik','hemodynamic','kreislaufregulation'],
 'Patientensicherheit': ['patientensicherheit','patient safety','fehler','error','cirs','crisis resource','crm','human factors','checkliste','checklist','simulation','kommunikation'],
 'Innere Medizin': ['innere medizin','internal medicine','diabetes','hypertonie','hypertension','copd','asthma','pneumonie','pneumonia','lungenembolie','pulmonary embolism','thrombose','thrombosis'],
 'Nephrologie': ['niere','renal','kidney','nierenversagen','acute kidney injury','aki','dialyse','dialysis','nierenersatz','kreatinin','creatinine','elektrolyt','hyperkali'],
 'Hepatologie': ['leber','liver','hepat','leberversagen','liver failure','zirrhose','cirrhosis','bilirubin'],
 'Endokrinologie': ['endokrin','endocrin','schilddrüse','thyroid','nebenniere','adrenal','cortisol','insulin','hypoglykäm','ketoazidose'],
 'Ernährungsmedizin': ['ernährung','nutrition','enteral','parenteral','kalorien','calorie','protein','mangelernährung','malnutrition'],
 'Geburtshilfe': ['geburtshilf','obstetri','schwangerschaft','pregnan','sectio','caesarean','cesarean','peripartal','postpartal','präeklampsie','preeclampsia','gebär'],
 'Dermatologie': ['dermatolog','haut','skin','verbrennung','burn','wundversorgung'],
 'Arbeitsmedizin': ['arbeitsmedizin','occupational','arbeitsschutz','arbeitszeit','betriebsarzt'],
 '00 SONO': ['sonographie','sonografie','ultraschall','ultrasound','echokardiograph','echocardiograph','pocus','fast-','e-fast','efast','tee','tte','lungenultraschall','lung ultrasound','doppler','sonographisch','эхокардиограф','узи','ультразвук','эхо','ECHO','echo','echokardiografie','kursbuchecho','sonografisch','b-mode','m-mode','schallkopf','transducer'],
}

def compile_terms(terms):
    out = []
    for t in terms:
        if t.isupper():  # аббревиатура: регистр и границы слова
            out.append((t, re.compile(r'(?<![A-Za-zÄÖÜäöü])' + re.escape(t) + r'(?![A-Za-zÄÖÜäöü])')))
        elif len(t) <= 4:  # короткие строчные термины — тоже по границе слова, без учёта регистра
            out.append((t, re.compile(r'(?<![a-zäöüß])' + re.escape(t) + r'(?![a-zäöüß])', re.I)))
        else:  # основа слова: немецкие сложные слова требуют поиска внутри слова
            out.append((t, re.compile(re.escape(t), re.I)))
    return out

PAT = {k: compile_terms(v) for k, v in TOPICS.items()}

def score(text, title):
    res = {}
    for topic, pats in PAT.items():
        s = 0; hits = []
        for term, p in pats:
            n = len(p.findall(text)); m = len(p.findall(title))
            if n or m:
                s += min(n, 5) + 6 * min(m, 1); hits.append(term)
        if s: res[topic] = (s, hits)
    return res

def assign(res):
    if not res: return []
    ranked = sorted(res.items(), key=lambda x: -x[1][0])
    top = ranked[0][1][0]
    chosen = [t for t, (s, h) in ranked if s >= max(4, 0.45 * top)][:3]
    return chosen

def main(files_csv, texts_dir, out_csv):
    rows = list(csv.DictReader(open(files_csv, encoding='utf-8')))
    out = []
    for r in rows:
        if r['kind'] != 'pdf':
            continue
        text = ''
        if r['text_file'] and os.path.exists(os.path.join(texts_dir, r['text_file'])):
            text = open(os.path.join(texts_dir, r['text_file']), encoding='utf-8', errors='replace').read()
        title = r['crossref_title'] if r['doi_belongs'] == 'yes' and r['crossref_title'] else os.path.splitext(r['name'])[0]
        res = score(text, title)
        topics = assign(res)
        out.append({'path': r['path'], 'title': title, 'text_chars': len(text),
                    'topics': '; '.join(topics),
                    'scores': '; '.join(f"{t}={res[t][0]}" for t in sorted(res, key=lambda x: -res[x][0])[:5])})
    w = csv.DictWriter(open(out_csv, 'w', encoding='utf-8', newline=''), fieldnames=list(out[0]))
    w.writeheader(); w.writerows(out)
    print(len(out), 'PDF;', sum(1 for o in out if o['topics']), 'с темой;', sum(1 for o in out if o['text_chars'] < 200), 'без текста')

if __name__ == '__main__':
    main(*sys.argv[1:4])
