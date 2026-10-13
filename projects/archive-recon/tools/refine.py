"""refine.py — вторая раскладка описи для страницы поиска (2026-10-13, запись Р-30 журнала LOG.md).

Что делает. Берёт данные страницы поиска (массив DATA, вырезанный из HTML артефакта в data.json)
и опись скрипта archive_scan.py (files.csv), сопоставляет их по md5 содержимого и пересчитывает:
  1) темы — по зонам текста: название (вес 8), «голова» — первые 1500 знаков своей первой страницы
     (вес 2 за попадание, не больше 3 попаданий на термин), остальной текст (вес 0,5, не больше 3);
     тема ставится, только если у неё есть попадание в названии или в голове; вторая и третья тема —
     если набрали не меньше половины первой; новая тема «Atemwegsmanagement» отдельно от «Beatmung»;
  2) руководства — по названию файла и по голове своей первой страницы («Leitlinie», «Guideline»,
     «AWMF-Register»), а не по номеру AWMF в списке литературы; главы книг руководствами не считаются;
     руководства без номера AWMF собираются в семьи по ключевым словам названия;
  3) DOI — принимается, если найден в рамке выходных данных статьи (bib-box), в имени файла,
     или в голове своей первой страницы; DOI, найденный дальше по тексту, отбрасывается вместе
     с годом CrossRef;
  4) год — год того издания, которое лежит в архиве: год авторского права своей страницы,
     если он позже года CrossRef (переиздание CME), иначе год CrossRef; первый год сохраняется
     в поле y0.
Вход и выход — НЕ в repo: в них пути личных папок владельца и чужие тексты.
Запуск: python refine.py <data.json> <files.csv> <out.json>
"""
import csv, json, re, sys, collections

TOPICS = {
 'Sepsis': ['sepsis','septisch','septic','qsofa','sofa-score','procalcitonin','surviving sepsis','fokussanierung','septischer schock','septic shock','SOFA'],
 'Antibiotika': ['antibiot','antiinfektiv','antimikrob','antimicrob','stewardship','resistenz','multiresist','MRSA','VRE','ESBL','carbapenem','penicillin','cephalosporin','vancomycin','staphylococcus','infektiolog','antimykot','antiviral','erreger','pathogen','harnwegsinfekt','ASP','pneumonie','pneumonia','periprothetisch','periprosthetic','tuberkulose','infektion','infection'],
 'Beatmung': ['beatmung','ventilation','beatmet','ARDS','lungenversagen','respiratory failure','respiratorische insuffizienz','PEEP','tidalvolumen','tidal volume','weaning','entwöhnung','ECMO','extrakorporal','NIV','high-flow','highflow','oxygenierung','oxygenation','respirator','lungenprotektiv'],
 'Atemwegsmanagement': ['atemweg','airway','intubation','intubiert','extubation','larynxmaske','laryngeal mask','videolaryngoskop','laryngoskop','doppellumen','double-lumen','koniotomie','cricothyr','tracheotomie','tracheostom','schwieriger atemweg','difficult airway','rapid sequence','RSI','aspiration'],
 'Delir': ['delir','delirium','postoperative cognitive','kognitive dysfunktion','agitation','verwirrtheit'],
 'Sedierung': ['sedierung','sedation','analgosedierung','dexmedetomidin','RASS','sedativ'],
 'Kardiologie': ['kardial','cardiac','herzinsuffizienz','heart failure','myokardinfarkt','myocardial infarction','koronar','coronary','vorhofflimmern','atrial fibrillation','rhythmusstörung','arrhythm','endokarditis','endocarditis','herzklappe','aortenstenose','kardiogen','cardiogenic','ventrikel','ventricle','EKG','ECG','ACS','STEMI','kardiovaskul','cardiovascul','hypertensiv'],
 'Reanimation': ['reanimation','resuscitation','herzstillstand','kreislaufstillstand','cardiac arrest','CPR','eCPR','ECPR','defibrillation','advanced life support','ROSC','postreanimation','ertrinkung','drowning','ACLS','PALS','BLS','herz-kreislauf-stillstand','kammerflimmern'],
 'Polytrauma': ['polytrauma','schwerverletzt','schwerstverletzt','major trauma','ATLS','damage control','traumaversorgung','traumatologisch','traumatologie','beckenfraktur','fast-protokoll','FAST-Aufbau','E-FAST','trauma abcde','hochrasanz','verkehrsunfall','major bleeding','traumatic bleeding','traumatologische blutung'],
 'Unfallchirurgie': ['unfallchirurg','fraktur','fracture','luxation','osteosynthese','traumatisch','traumatic','nervenläsion','verletzung','injury','sturz'],
 'Schockraum': ['schockraum','trauma bay','resuscitation room','schockraummanagement','zentrale notaufnahme','notaufnahme','emergency department'],
 'Transfusionsmedizin': ['transfusion','erythrozytenkonzentrat','red blood cell','thrombozytenkonzentrat','platelet','frischplasma','gefrorenes plasma','FFP','massivtransfusion','patient blood management','blood management','blutkomponent','blutprodukt','blood product','erythrozyt','plasmaderivat','blutverlust','blood loss'],
 'Blutung und Gerinnung': ['blutung','bleeding','hämorrhag','haemorrhag','hemorrhag','blutverlust','blood loss','gerinnung','koagulopathie','coagulopathy','coagulation','hämostase','haemostasis','hemostasis','ROTEM','TEG','viskoelast','viscoelast','fibrinogen','tranexam','TXA','gerinnungsfaktor','antikoagul','anticoagul','heparin','INR','thrombozytenfunktion','PPSB','prothrombinkomplex'],
 'Notarzt': ['notarzt','notärzt','rettungsdienst','präklinisch','prähospital','prehospital','emergency medical service','rettungswagen','leitstelle','notfallsanitäter','luftrettung','notfallmedizin','emergency medicine'],
 'Leitender Notarzt': ['leitender notarzt','leitende notärzt','massenanfall','MANV','großschaden','katastroph','sichtung','triage','mass casualty'],
 'Regionalanästhesie': ['regionalanästhesie','regional anesthesia','regional anaesthesia','nervenblockade','nerve block','plexus','spinalanästhesie','spinal anesthesia','periduralanästhesie','epidural','rückenmarksnah','rückenmarknah','neuraxial','lokalanästhetik','local anesthetic'],
 'Schmerztherapie': ['schmerz','pain','analgesie','analgesia','opioid','opiat','NSAR','metamizol','paracetamol','piritramid','morphin'],
 'Allgemeine Anästhesiologie': ['anästhesie','anaesthesia','anesthesia','narkose','allgemeinanästhesie','prämedikation','präoperativ','preoperative','perioperativ','perioperative','aufwachraum','muskelrelax','neuromuscular','volatile','TIVA','PONV','ASA-','anästhesist','anaesthesist'],
 'Allgemeine Chirurgie': ['laparotomie','laparoskop','akutes abdomen','acute abdomen','ileus','peritonitis','appendizit','cholezyst','kompartment','viszeralchirurg','abdominalchirurg','whipple','pankrea','darmpassage','obstipation','darm'],
 'Thorax': ['thorax','thoraxdrainage','chest tube','pneumothorax','pleuraerguss','pleural effusion','thoraxchirurgie','thoracic','lungenresektion','einlungenventilation','one-lung'],
 'Neurochirurgie': ['neurochirurg','neurosurg','subarachnoidal','subarachnoid','intrakraniell','intracranial','hirndruck','schädel-hirn','SHT','traumatic brain','hydrozephalus','hirnblutung','intracerebral','kraniotomie','craniotomy','neurointensiv'],
 'Medikamente': ['pharmakolog','pharmacolog','pharmakokinetik','pharmacokinetic','arzneimittel','medikament','dosierung','dosing','wechselwirkung','drug interaction','katecholamin','vasopressor','noradrenalin','norepinephrine','allergie','allergy','anaphylax','bioverfügbar','bioverfueg','darreichungsform'],
 'Physiologie': ['physiologie','physiology','pathophysiolog','sauerstofftransport','oxygen delivery','säure-basen','acid-base','hämodynamik','hemodynamic','kreislaufregulation','blutgas'],
 'Patientensicherheit': ['patientensicherheit','patient safety','CIRS','crisis resource','CRM','human factors','checkliste','checklist','simulation','behandlungsfehler','medical error','qualitätsmanagement','aufklärung'],
 'Innere Medizin': ['innere medizin','internal medicine','diabetes','hypertonie','hypertension','COPD','asthma','lungenembolie','pulmonary embolism','thrombose','thrombosis'],
 'Nephrologie': ['niere','renal','kidney','nierenversagen','acute kidney injury','AKI','dialyse','dialysis','nierenersatz','kreatinin','creatinine','elektrolyt','hyperkali','harnweg'],
 'Hepatologie': ['leber','liver','hepati','hepato','leberversagen','liver failure','zirrhose','cirrhosis','bilirubin'],
 'Endokrinologie': ['endokrin','endocrin','schilddrüse','thyroid','nebenniere','adrenal','cortisol','insulin','hypoglykäm','ketoazidose'],
 'Ernährungsmedizin': ['ernährung','nutrition','enteral','parenteral','kalorien','calorie','mangelernährung','malnutrition'],
 'Geburtshilfe': ['geburtshilf','obstetri','schwangerschaft','pregnan','sectio','caesarean','cesarean','peripartal','postpartal','präeklampsie','preeclampsia','gebär'],
 'Pädiatrie': ['kinder','kindes','pädiatr','paediatr','pediatr','neugeboren','neonat','säugling','infant','jugendliche'],
 'Dermatologie': ['dermatolog','verbrennung','burn injur','wundversorgung','rosacea','haut','skin'],
 'Arbeitsmedizin': ['arbeitsmedizin','occupational','arbeitsschutz','arbeitszeit','betriebsarzt','dienstplan','schichtdienst','schichtarbeit','shift work'],
 'Sonografie': ['sonographie','sonografie','ultraschall','ultrasound','echokardiograph','echocardiograph','echokardiograf','POCUS','E-FAST','eFAST','TEE','TTE','lungenultraschall','lung ultrasound','doppler','sonographisch','sonografisch','эхокардиограф','УЗИ','ультразвук','kursbuchecho','B-Bild','M-Mode','schallkopf','transducer','notfallsonograf','sono','echo','ECHO','sonograph','sonogra','WINFOCUS','ЭУС','эхо'],
}
# Термин в ВЕРХНЕМ регистре (или со смешанным регистром и цифрой/дефисом, как eCPR, E-FAST) — с учётом регистра и по
# границам слова; короткий строчный (до 4 знаков) — без учёта регистра, по границам слова; длинный — основа внутри слова.
L = 'A-Za-zÄÖÜäöüßА-Яа-яЁё'
def comp(t):
    if t != t.lower() and (t.isupper() or any(c.isupper() for c in t[1:])):
        return re.compile(r'(?<![%s])%s(?![%s])' % (L, re.escape(t), L))
    if len(t) <= 4:
        return re.compile(r'(?<![%s])%s(?![%s])' % (L, re.escape(t), L), re.I)
    return re.compile(re.escape(t), re.I)
PAT = {k: [(t, comp(t)) for t in v] for k, v in TOPICS.items()}

TITLED = {}
NOTOPIC = re.compile(r'^(?:PALS|ACLS|BLS)\b|zertifikat|certificate|bescheinigung|testfragen|fortbildung|programm|eref|rechnung|bestätigung|bestaetigung|anmeldung|hotel|booking|antrag', re.I)

def topics_for(title, head, body):
    res = {}; tit = set()
    for tp, pats in PAT.items():
        st = sh = sb = 0
        for t, p in pats:
            if p.search(title): st += 8
            sh += 2 * min(len(p.findall(head)), 3)
            sb += 0.5 * min(len(p.findall(body)), 3)
        if st or sh:
            res[tp] = st + sh + sb
            if st: tit.add(tp)
    if not res: return [], res
    TITLED[id(res)] = tit
    rk = sorted(res.items(), key=lambda x: -x[1])
    top = rk[0][1]
    if top < 6: return [], res
    titled = TITLED.get(id(res), set())
    return [t for t, s in rk if t in titled or s >= max(6, 0.5 * top)][:3], res

GL_TITLE = re.compile(r'leitlinie|(?<![a-z])LL(?![a-z])|guideline|querschnitts|empfehlungen zur|consensus|konsensus|(?<![A-Za-z])S[123][ke]?(?![a-z0-9])|positionspapier|pocket.?guide', re.I)
GL_HEAD = re.compile(r'Querschnitts-Leitlinie|Clinical Practice Guideline|Leitliniengremium|AWMF[- ]?Regist|AWMF-Nr|S[123][ke]?-Leitlinie|Leitlinie der|Leitlinienreport|guidelines? (?:for|on|of)|recommendations? (?:for|on)|Empfehlungen (?:zur|der|für)|Konsensus|consensus statement', re.I)
AWMF = re.compile(r'(?<!\d)(0\d\d|1\d\d)[-/](0\d\d)(?!\d)')
FAMILY = [  # семья руководства без номера AWMF: (ключ, шаблон по названию и голове)
 ('Extrakorporale Reanimation (eCPR-Konsensuspapier)', re.compile(r'extra.?korporal', re.I)),
 ('Reanimation ERC/GRC', re.compile(r'LL Reanimation|(?<![A-Za-z])(?:ERC|GRC)(?![A-Za-z])|European Resuscitation')),
 ('Reanimation AHA (ACLS, CPR)', re.compile(r'(?<![A-Za-z])(?:ACLS|CPR|AHA)(?![A-Za-z])|American Heart')),
 ('Blutung und Gerinnung bei Trauma (European guideline)', re.compile(r'major bleeding|trauma.{0,40}bleeding|blutung.{0,40}trauma', re.I)),
 ('Erythrozytentransfusion bei kritisch Kranken (CHEST 2025, mit deutscher Übersetzung)', re.compile(r'red blood cell transfusion|transfusion roter|erythrozyten', re.I)),
 ('Hämotherapie (Querschnitts-Leitlinien BÄK)', re.compile(r'querschnitts|blut 20', re.I)),
 ('Antikoagulation und Regionalanästhesie / perioperativ', re.compile(r'antikoag|anticoag|antiplatelet', re.I)),
 ('Endokarditis (ESC)', re.compile(r'endokarditis|endocarditis', re.I)),
 ('Antiinfektiva / Infektionen (Empfehlungen, Pocket Guides)', re.compile(r'antiinfektiv|pocket.?guide|infektion', re.I)),
 ('Metamizol perioperativ', re.compile(r'metamizol|novalgin', re.I)),
]
AWMF_TITLES = [  # номер реестра AWMF по словам названия — для файлов-руководств без номера в имени и на первой странице
 ('001-021', re.compile(r'invasive.?beatmung', re.I)), ('079-001', re.compile(r'sepsis', re.I)),
 ('001-012', re.compile(r'analgesie.?sedierung|delirmanagement', re.I)), ('012-019', re.compile(r'polytrauma|schwerverletzt', re.I)),
 ('001-005', re.compile(r'r(ü|ue)ckenmarks?n(a|ä|ae)h', re.I)), ('020-015', re.compile(r'weaning', re.I)),
 ('001-020', re.compile(r'volumentherapie', re.I)),
]
DOI_RE = re.compile(r'10\.\d{4,9}/[^\s"<>,;)\]]+')
VERSION_YEAR = re.compile(r'(?:überarbeitete|aktualisierte|revidierte)\s+(?:Version|Fassung|Auflage)[^0-9]{0,25}((?:19|20)\d\d)', re.I)
NAME_YEAR = re.compile(r'(?<!\d)((?:19|20)\d\d)(?:[._-](?:0[1-9]|1[0-2]))?(?!\d)')
OWN_YEAR = ('text-copyright', 'text-stand', 'text-published', 'text-firstpage-most-common')

def words(s):
    return set(w for w in re.findall(r'[%s]{4,}' % L, s.lower()))

def same_title(cr, own):
    # название CrossRef совпадает со своей первой страницей: не меньше 60 процентов его слов есть в начале текста
    a = words(cr)
    return len(a) >= 3 and len(a & words(own)) >= 0.6 * len(a)

def cand(r):
    out = {}
    for part in (r.get('year_candidates') or '').split(';'):
        if ':' in part:
            k, v = part.split(':', 1)
            if re.fullmatch(r'(19|20)\d\d', v.strip()): out.setdefault(k.strip(), v.strip())
    return out

def main(data_json, files_csv, out_json):
    D = json.load(open(data_json, encoding='utf-8'))
    R = {r['md5']: r for r in csv.DictReader(open(files_csv, encoding='utf-8-sig')) if r['kind'] == 'pdf'}
    rep = collections.Counter()
    for x in D:
        r = R.get(x['h'], {})
        text = (x.get('x', '') + ' ' + x.get('ft', '')).strip()
        title = x['t'] if x['t'] == x['n'] else x['t'] + ' ' + x['n']
        head, body = text[:1500], text[1500:]
        # DOI и год
        doi = r.get('doi', ''); src = r.get('doi_source', '')
        tdois = [] if x['d'] == 'presentation' else [d.rstrip('.').lower() for d in DOI_RE.findall(text[:1500]) if d.count('(') == d.count(')')]
        if tdois and doi and doi.lower() not in tdois:  # на своей первой странице напечатан другой DOI: он и есть свой
            x['doi'] = tdois[0]; x['dd'] = ''; rep['doi_from_text'] += 1
            c = cand(r); own = next((c[k] for k in OWN_YEAR if k in c), '')
            if own: x['y'], x['ys'] = own, 'text-copyright'
            x.pop('y0', None); doi = ''
        ok = bool(doi) and r.get('doi_belongs') == 'yes' and (src in ('bib-box', 'filename-springer') or doi.lower()[-10:] in head.lower() or same_title(r.get('crossref_title', ''), title + ' ' + head))
        if doi and not ok: rep['doi_dropped'] += 1
        if not x.get('doi'): x['doi'] = doi if ok else ''
        c = cand(r); y0 = c.get('crossref') if ok else ''
        own = next((c[k] for k in OWN_YEAR if k in c), '')
        if 'bk' in x:  # глава собранной книги: год издания книги, DOI главы из списка литературы не берётся
            x['y'], x['ys'], x['doi'] = '2019', 'book', ''
        elif y0 and own and own > y0:
            x['y'], x['ys'], x['y0'] = own, 'text-copyright', y0; rep['year_reprint'] += 1
        elif y0:
            x['y'], x['ys'] = y0, 'crossref'
        elif x.get('ys') in ('crossref', 'pdf-metadata') and own and x.get('ys') != 'text-copyright' and (x['d'] == 'book' or int(own) >= int(x.get('y') or 0) - 3):
            # год свойств PDF — дата сохранения файла; год со своей страницы точнее, если он не старше на годы (иначе это год источника)
            x['y'], x['ys'] = own, 'text-copyright'; rep['year_meta_to_text'] += 1
        elif x.get('ys') == 'crossref' and not x.get('doi'):  # год CrossRef от чужого DOI
            alt = own or c.get('pdf-metadata') or c.get('filename') or ''
            x['y'], x['ys'] = alt, ('text-copyright' if own else 'pdf-metadata' if alt else ''); rep['year_from_foreign_doi'] += 1
        if x['d'] == 'certificate' and int(x.get('p') or 0) > 5:  # 20-страничное пособие — не справка
            x['d'] = 'other_pdf'; rep['certificate_to_other'] += 1
        mf = re.search(r'(?:Erstpublikation|Erstver(?:ö|oe)ffentlichung|erstmals (?:erschienen|ver(?:ö|oe)ffentlicht)|first published|Originalpublikation).{0,60}?(?<!\d)((?:19|20)\d\d)(?!\d)', text[:4000], re.I)
        if mf and x.get('y') and mf.group(1) < x['y']: x['y0'] = mf.group(1); rep['first_published_text'] += 1
        if x['d'] == 'certificate' or re.search(r'zertifikat|ACLS|PALS|BLS', x['n'], re.I):
            m = NAME_YEAR.search(x['n'])
            if m: x['y'], x['ys'] = m.group(1), 'filename'; rep['year_from_name'] += 1
        if not x['doi'] and x.get('dd'):
            x['dd'] = ''; rep['doi_group_dropped'] += 1
        # руководство
        name_title = x['n'] + ' ' + x['t']
        is_gl = 'bk' not in x and x['d'] not in ('mindmap_card', 'certificate') and (bool(GL_TITLE.search(name_title)) or bool(GL_HEAD.search(head[:800])))
        if x['d'] in ('journal_article', 'cme_article') and not GL_HEAD.search(head[:1500]) and not re.search(r'Empfehlungen zur|Konsensus|Expertenempfehlung', x['t']):
            is_gl = False  # статья о руководстве — не само руководство
        was = x['d'] == 'guideline'
        is_gl = is_gl or (was and 'bk' not in x)
        if re.search(r'\bCME\b|Fall \d|Testfragen|Programm|Reading List|\bASP\b', name_title):
            is_gl = False
        if is_gl and not was: x['d0'] = x['d']; x['d'] = 'guideline'; rep['guideline_added'] += 1
        if was and not is_gl: x['d'] = x.get('d0') or 'other_pdf'; rep['guideline_removed'] += 1
        if x['d'] == 'guideline':
            m = (AWMF.search(x['n']) or AWMF.search(head[:600])) if re.search(r'AWMF|S[123]|Leitlinie', name_title + head[:600]) else None
            m2 = VERSION_YEAR.search(text[:4000])
            if m2 and m2.group(1) > (x['y'] or '0'): x['y'], x['ys'] = m2.group(1), 'text-version'; rep['year_version'] += 1
            if x['aw'] or AWMF.search(x['n']):
                m3 = re.search(r'_((?:19|20)\d\d)[-_](0[1-9]|1[0-2])', x['n'])
                if m3: x['y'], x['ys'] = m3.group(1), 'filename'
            mv = re.search(r'\d{3}-\d{3}([lk])[_ ]', x['n'])
            if mv: x['gv'] = 'long' if mv.group(1) == 'l' else 'short'
            elif re.match(r'(Kurz|Fazit)', x['n']): x['gv'] = 'short'
            x['exp'] = 1 if re.search(r'abgelauf', x['n'] + ' ' + x['t'], re.I) else 0
            prev = x.get('aw', '')
            x['aw'] = (m.group(1) + '-' + m.group(2)) if m else prev or next((n for n, p in AWMF_TITLES if p.search(name_title)), '')
            x['fam'] = '' if x['aw'] else next((k for k, p in FAMILY if p.search(name_title)), 'Прочие руководства')
        else:
            x['aw'] = ''; x['fam'] = ''
        # темы
        tp, sc = topics_for(title, head, body)
        if x['d'] == 'certificate' or NOTOPIC.search(x['n']): tp = []
        if re.search(r'nicht-?\s?traumatolog', x['t'], re.I) and 'Polytrauma' in tp: tp.remove('Polytrauma')
        if 'bk' in x and 'Sonografie' not in tp: tp = ['Sonografie'] + tp[:2]
        if tp != x['tp']: rep['topics_changed'] += 1
        x['tp0'] = x['tp']; x['tp'] = tp
    # сходство текста в группе одного DOI: точные копии — 100 процентов
    G = collections.defaultdict(list)
    for x in D:
        if x.get('dd'): G[x['dd']].append(x)
    for k, a in G.items():
        if len(set(x.get('dc') or x['h'] for x in a)) == 1:
            for x in a: x['sm_dd'] = 100
        if len(a) < 2:
            for x in a: x['dd'] = ''
    json.dump(D, open(out_json, 'w', encoding='utf-8'), ensure_ascii=False)
    print(dict(rep)); print('без темы:', sum(1 for x in D if not x['tp']))
    print(collections.Counter(t for x in D for t in x['tp']).most_common())

if __name__ == '__main__':
    main(*sys.argv[1:4])
