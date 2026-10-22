#!/usr/bin/env python3
"""meta/scripts/restructure_n8n_2026-10-22.py — переложение Skill n8n-engineering-manual по трём правилам
протокола синтеза (meta/PROTOCOL_knowledge-synthesis.md, внесены 2026-10-22):
  1. основание правила — по адресу в references/basis.md, в правиле ярлык [основание: <ярлык>];
  2. шапка SKILL.md для исполнителя — не больше трёх строк, объяснение устройства — в basis.md;
  3. зерно references/ — момент действия: roots.md и engine.md разрезаны; под прежними именами остаются
     закон раздела и указатель «пункт → файл», чтобы ссылки других Skills на roots.md и engine.md работали.

Запуск: python3 meta/scripts/restructure_n8n_2026-10-22.py SRC OUT
  SRC — папка Skill (зеркало или живой), OUT — папка результата (создаётся).
Пишет OUT/../restructure_report.json — вход приёмки meta/scripts/accept_restructure_n8n.py.
Модель текст исходника не набирает: всё, что не названо в ADDED, — байты исходника, перенесённые скриптом.
Образец — meta/scripts/restructure_sbe_2026-10-22.py (second-brain-engineer).
"""
import os, re, sys, json

SRC, OUT = sys.argv[1], sys.argv[2]
ADDED, REMOVED, MOVED = [], [], []      # строки сессии / снятые с заменой / ушедшие в «Устройство Skill»
BASIS = []                              # (label, section, [lines])
REPORT = 'meta/SYNTHESIS_n8n-engineering-manual_2026-10-20.md'

def read(p): return open(p, encoding='utf-8').read()
def write(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(t)
def add(line): ADDED.append(line); return line
def rem(line): REMOVED.append(line); return line

BASIS_RE = re.compile(r'(?:^|(?<=[.;»)!*] ))((?:\s*- )?\s*Основани[ея](?![»])(?: [^:]{0,70})?:)')
SEC_RE = [re.compile(r'^#{2,3} (.+)'),
          re.compile(r'^\*\*((?:R\d+[a-z]?|A\d|T\d(?:-[A-Z])?|\d+(?:\.\d+)+)[. ][^*]{0,50})')]

def extract_basis(text, stem, counter):
    lines = text.split('\n'); out = []; i = 0; section = ''
    while i < len(lines):
        ln = lines[i]
        for r in SEC_RE:
            m = r.match(ln)
            if m: section = m.group(1).strip().rstrip('.*'); break
        mm = BASIS_RE.search(ln)
        if not mm:
            out.append(ln); i += 1; continue
        start = mm.start(1)
        prefix, tail = ln[:start], ln[start:]
        lead = re.match(r'^\s*(?:- )?\s*', tail).group(0)
        prefix, tail = prefix + lead, tail[len(lead):]
        block = [tail]
        if tail.rstrip().endswith(':'):
            j = i + 1
            while j < len(lines) and lines[j].startswith('- '):
                block.append(lines[j]); j += 1
            i = j - 1
        counter[0] += 1
        label = f'{stem}-{counter[0]:02d}'
        sec = re.sub(r' {2,}', ' ', re.sub(r'[():]', '', section))[:70].strip()
        BASIS.append((label, sec, block))
        rid = re.findall(r'правил[оа] ([§A-Z]?[\w.-]*\w)', ' '.join(block))
        tag = f'{label} · правило {", ".join(dict.fromkeys(rid))}' if rid else label
        if prefix.strip() in ('', '-'):
            out.append(add(f'{prefix}[основание: {tag}]'))
        else:
            out.append(prefix.rstrip() + ' ' + add(f'[основание: {tag}]'))
        i += 1
    return '\n'.join(out)

def move_lines(text, pred):
    keep = []
    for ln in text.split('\n'):
        if ln.strip() and pred(ln): MOVED.append(ln)
        else: keep.append(ln)
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(keep))

RED_OLD, RED_NEW = 'Редакция 2026-10-20', 'Редакция 2026-10-22.'
def bump(text):
    assert RED_OLD in text
    rem(RED_OLD); return text.replace(RED_OLD, add(RED_NEW), 1)

# ---------- 1. SKILL.md ----------
s = read(os.path.join(SRC, 'SKILL.md'))
s = bump(s)
s = move_lines(s, lambda l: l.startswith(('**Номера пунктов не меняются', '**Один факт живёт', '**Здесь только правила, верные',
                                         'Этот файл читается всегда. Механика движка', 'Состав Skill — пять файлов')))
hdr = add('Этот файл читается всегда. Остальное лежит в references/ и читается перед своим действием целиком, по таблице «Что читать дальше»; номера пунктов (§, A, R, T) сквозные и не перенумеровываются, ссылка в скобках вида *(R1b)* или *(§4.8)* значит «механизм читать там» и разрешается по той же таблице. Действие, для которого свой файл не прочитан, — то же нарушение, что действие без этого Skill. Почему Skill устроен так — references/basis.md, раздел «Устройство Skill» (его читает тот, кто Skill правит, а не тот, кто исполняет).')
s = s.replace(RED_NEW + '\n\n', RED_NEW + '\n\n' + hdr + '\n\n', 1)
heading_old = '## Как устроен Skill — что читать дальше'
s = s.replace(heading_old, add('## Что читать дальше'), 1); rem(heading_old)

rows = s.split('\n'); nr = []
for ln in rows:
    if ln.startswith('| проектирование или правку логики воркфлоу'):
        rem(ln)
        nr.append(add('| проектирование или правку логики воркфлоу: Code-узлы, items и их размножение, executeOnce, pairedItem, Merge/Switch, Execute Workflow, HTTP, пагинация, время, память, Data Table | references/engine.md — закон раздела и указатель «пункт → файл», затем файл нужных пунктов: engine-code.md, engine-flow.md, engine-http.md, engine-time.md | 4.1–4.12 |'))
    elif ln.startswith('| диагностику: воркфлоу упал'):
        rem(ln)
        nr.append(add('| диагностику: воркфлоу упал, молчит, пишет не то или не туда; разбор отказа по корню; проверку по чек-листу T4, когда гейт ссылается на R-номер | references/roots.md — закон раздела, таблица «симптом → корень» и указатель «корень → файл», затем файл названного корня: roots-credential.md, roots-write.md, roots-silent.md, roots-sheets.md, roots-net-time.md, roots-security.md | 5 (R1a–R19), 7 |'))
    elif ln.startswith('| харвест или обслуживание: откуда пришёл корень'):
        nr.append(ln)
        nr.append(add('| править Skill, спорить с правилом, найти адрес случая за ярлыком [основание: …]; синтез и харвест | references/basis.md | основания правил, устройство Skill |'))
    elif ln.startswith('| Случаи, на которых стоят правила'):
        rem(ln)
        nr.append(add(f'| Случаи, на которых стоят правила (адреса журналов, номера исполнений) | references/basis.md: ярлык [основание: …] ведёт на строку с номером правила, адреса случаев — в отчёте синтеза `{REPORT}` по этому номеру |'))
    else:
        nr.append(ln)
s = '\n'.join(nr)
write(os.path.join(OUT, 'SKILL.md'), extract_basis(s, 'MAIN', [0]))

# ---------- 2. шапки references: строка «Часть Skill …» уходит в «Устройство Skill», вместо неё короткая ----------
def ref_head(text, new_line):
    text = bump(text)
    lines = text.split('\n')
    for k, ln in enumerate(lines):
        if ln.startswith('Часть Skill n8n-engineering-manual.'):
            MOVED.append(ln); lines[k] = add(new_line); break
    else: raise SystemExit('нет строки «Часть Skill»')
    return '\n'.join(lines)

COMMON = ' Номера пунктов сквозные, общие со SKILL.md; ссылка на пункт другой части разрешается по таблице «Что читать дальше» в SKILL.md; основание правила — по ярлыку в references/basis.md.'

w = ref_head(read(os.path.join(SRC, 'references', 'write.md')),
             'Часть Skill n8n-engineering-manual. Читать: перед любой записью или правкой воркфлоу — `create_workflow_from_code`, `update_workflow`, `publish_workflow`, `unpublish_workflow`, работа с webhook-триггером, привязка ключей, выбор пути записи, судьба ненужного воркфлоу, копия воркфлоу; целиком, один раз за сессию.' + COMMON)
write(os.path.join(OUT, 'references', 'write.md'), extract_basis(w, 'WR', [0]))
t_src = read(os.path.join(SRC, 'references', 'templates.md'))
TPL_KEEP = re.search(r'Шаблон описывает форму, а не воркфлоу инстанса: .*?адреса — в отчёте синтеза\.', t_src).group(0)   # фраза исполнителя из прежней шапки, перенесена скриптом
t = ref_head(t_src,
             'Часть Skill n8n-engineering-manual. Читать: перед применением конкретного шаблона — идемпотентная запись (T1), HTTP и обработка ошибок (T2), вызов Anthropic API (T3), чеклист перед публикацией (T4), воркфлоу записи во внешний кабинет (T5); целиком, один раз за сессию. ' + TPL_KEEP + ' Пункт чек-листа, который отсылает к корню или пункту в скобках, наследует основание того пункта.' + COMMON)
write(os.path.join(OUT, 'references', 'templates.md'), extract_basis(t, 'TPL', [0]))

# ---------- 3. engine.md → указатель + четыре файла ----------
e = ref_head(read(os.path.join(SRC, 'references', 'engine.md')),
             'Часть Skill n8n-engineering-manual: закон раздела 4 и указатель «пункт → файл». Читать: перед проектированием или правкой логики воркфлоу — этот файл, затем файл нужных пунктов по указателю ниже, каждый целиком.' + COMMON)
e = extract_basis(e, 'ENG', [0])
parts = re.split(r'(?m)^(?=\*\*4\.\d+[ .])', e)
e_head, e_pts = parts[0], parts[1:]
top = lambda p: int(re.match(r'\*\*4\.(\d+)', p).group(1))
ENG = [('engine-code.md', (1, 2), 'RAW-слой и Code-узел', 'перед тем как писать или править Code-узел, решать, что попадает в RAW-слой, или пользоваться памятью воркфлоу между прогонами (static data)'),
       ('engine-flow.md', (3, 4, 5, 6, 7), 'поток элементов', 'перед проектированием или правкой потока элементов: Execute Once, трассировка pairedItem, fan-out, Merge и Switch, Execute Workflow'),
       ('engine-http.md', (8, 9), 'HTTP и пагинация', 'перед настройкой или правкой HTTP-узла (тело, заголовки, обработка ответа, пагинация), узла Telegram (разметка, длинное сообщение), записи файла в GitHub, проверки страницы, найденной поиском, воркфлоу-зонда; перед выражением в любом поле — три вида выражения (4.8.2)'),
       ('engine-time.md', (10, 11, 12), 'время, память, Data Table', 'перед работой со временем, датами и часовым поясом, с большими объёмами данных (память, OOM) или с Data Table')]
seen = []
router = [add('**Указатель «пункт → файл».** Пункты раздела лежат в файлах по моменту действия; номер пункта не меняется:'), '',
          add('| Пункты | Файл | Когда читать |'), add('|---|---|---|')]
for fn, nums, title, when in ENG:
    body = ''.join(p for p in e_pts if top(p) in nums); seen += [top(p) for p in e_pts if top(p) in nums]
    rng = f'4.{nums[0]}' if len(nums) == 1 else f'4.{nums[0]}–4.{nums[-1]}'
    router.append(add(f'| {rng} | references/{fn} | {when} |'))
    txt = (add(f'# n8n-engineering-manual — механика движка: {title}') + '\n\n' + RED_NEW + '\n\n'
           + add(f'Часть Skill n8n-engineering-manual, пункты {rng} раздела 4. Читать: {when}; целиком, один раз за сессию. Закон раздела 4 (движок при несовпадении формы молча берёт первое, пустое или буквальное) — references/engine.md.' + COMMON) + '\n\n'
           + add(f'## 4. Механика движка (продолжение): {title}') + '\n\n' + body.rstrip('\n') + '\n')
    ADDED.append(RED_NEW)
    write(os.path.join(OUT, 'references', fn), txt)
assert sorted(seen) == sorted(top(p) for p in e_pts), 'пункт раздела 4 не разложен'
write(os.path.join(OUT, 'references', 'engine.md'), e_head.rstrip('\n') + '\n\n' + '\n'.join(router) + '\n')

# ---------- 4. roots.md → закон, указатель, §7 + шесть файлов ----------
r = read(os.path.join(SRC, 'references', 'roots.md'))
r = move_lines(r, lambda l: l.startswith('Строки «Основание» называют номер правила'))
r = ref_head(r, 'Часть Skill n8n-engineering-manual: закон раздела 5, поиск по смыслу сравнения, указатель «корень → файл» и таблица «симптом → корень» (§7). Читать: перед диагностикой отказа или когда чек-лист T4 ссылается на R-номер — этот файл, затем файл названного корня, каждый целиком.' + COMMON)
r = extract_basis(r, 'ROOT', [0])
pre, sec7 = r.split('\n## 7. ', 1); sec7 = '## 7. ' + sec7
parts = re.split(r'(?m)^(?=\*\*R\d+[a-z]?\. |\*\*Закон (?!раздела))', pre)
r_head, raw = parts[0], parts[1:]
r_pts = []; pend = ''
for p_ in raw:                       # закон группы корней стоит перед своим первым корнем и едет вместе с ним
    if p_.startswith('**Закон '): pend += p_
    else: r_pts.append(pend + p_); pend = ''
assert pend == '', 'закон без корня после него'
rid = lambda p: re.search(r'(?m)^\*\*(R\d+[a-z]?)\.', p).group(1)
ROOTS = [('roots-credential.md', ['R1a'], 'привязка ключа доступа', 'узел не видит ключ доступа, ключ не тот, кабинет не тот; перед привязкой или сменой ключа'),
         ('roots-write.md', ['R1b', 'R2', 'R17'], 'запись и публикация воркфлоу', 'после записи воркфлоу кодом, правки в редакторе или публикации что-то пропало, исполняется не та версия, настройка не применилась; имя параметра в JSON не говорит, что значит флаг'),
         ('roots-silent.md', ['R3', 'R4', 'R8', 'R9', 'R10', 'R16', 'R18', 'R19'], 'тихая потеря данных', 'прогон зелёный, а результата нет или он неполный: ноль элементов, Switch, Merge, fan-out, Execute Workflow; цена get_execution с данными и ответ больше предела MCP (R4.5, R4.6); запись «заменить целиком» стёрла то, что чтение не вернуло; неизвестное значение стало нулём'),
         ('roots-sheets.md', ['R6'], 'Google Sheets', 'узел Google Sheets пишет не туда, не то или упирается в квоту'),
         ('roots-net-time.md', ['R5', 'R7', 'R11'], 'HTTP, расписание, таймаут', 'HTTP-узел потерял поля или элементы, расписание сработало не в то время, сетевой узел завис'),
         ('roots-security.md', ['R12', 'R13', 'R14', 'R15'], 'вебхуки и секреты', 'вебхук без аутентификации или вызывается в обход неё, секрет в параметрах узла или в коде; закон периметра R12–R15')]
seen = []
router = [add('**Указатель «корень → файл».** Корни лежат в файлах по моменту действия; номер корня не меняется:'), '',
          add('| Корни | Файл | Когда читать |'), add('|---|---|---|')]
for fn, ids, title, when in ROOTS:
    body = ''.join(p for i in ids for p in r_pts if rid(p) == i); seen += ids
    router.append(add(f'| {", ".join(ids)} | references/{fn} | {when} |'))
    txt = (add(f'# n8n-engineering-manual — корневые причины: {title}') + '\n\n' + RED_NEW + '\n\n'
           + add(f'Часть Skill n8n-engineering-manual, корни {", ".join(ids)} раздела 5. Читать: {when}; целиком, один раз за сессию. Закон раздела 5 и таблица «симптом → корень» — references/roots.md.' + COMMON) + '\n\n'
           + add(f'## 5. Корневые причины (продолжение): {title}') + '\n\n' + body.rstrip('\n') + '\n')
    ADDED.append(RED_NEW)
    write(os.path.join(OUT, 'references', fn), txt)
assert sorted(seen) == sorted(rid(p) for p in r_pts), 'корень не разложен'
write(os.path.join(OUT, 'references', 'roots.md'), r_head.rstrip('\n') + '\n\n' + '\n'.join(router) + '\n\n---\n\n' + sec7)
ADDED.append('---')   # разделитель между указателем и §7

# ---------- 5. basis.md ----------
b = [add('# n8n-engineering-manual — основания правил и устройство Skill'), '',
     add(f'Редакция 2026-10-22. Кто читает: синтез (`meta/PROTOCOL_knowledge-synthesis.md`), харвест, сессия, которая правит Skill или оспаривает правило. Исполнитель правил этот файл не читает: ему нужны условие, действие, «почему» и «не путать», и они остались в правиле. Ярлык `[основание: X]` в тексте правила разрешается строкой `- X (...)` ниже; продолжение многострочного основания — строки с отступом в два пробела. «Отчёт синтеза» в строке основания — `{REPORT}`, таблица «правило → случаи», по номеру правила. Текст оснований и абзацы устройства перенесены скриптом байт в байт (`meta/scripts/restructure_n8n_2026-10-22.py`).'), '',
     add('## Устройство Skill'), '',
     add('Переложение 2026-10-22 (контракт автопилота, `projects/knowledge-synthesis/PLAN.md`): основания вынесены сюда ярлыками — ярлык в правиле несёт и номер правила в отчёте синтеза, чтобы ссылки других Skills вида «правило §1.1.0» находили место без этого файла; шапка SKILL.md сокращена до строки редакции и двух строк; references/roots.md и references/engine.md разрезаны по моменту действия — под прежними именами остались закон раздела и указатель «пункт → файл», чтобы ссылки других Skills и файлов репозитория на roots.md и engine.md продолжали работать; закон группы корней стоит в том же файле, что и её корни (закон периметра — с R12–R15, закон пропуска — с R18 и R19).'), '',
     add('### Правила для того, кто правит Skill (из шапки SKILL.md до 2026-10-22, дословно; действуют)'), '']
EDITOR = ('**Номера пунктов не меняются', '**Один факт живёт', '**Здесь только правила, верные')
for ln in MOVED:
    if ln.startswith(EDITOR): b += [ln, '']
b += [add('Правило «файл, которого нет в таблице «Что читать дальше», не читается никем — каждый новый файл Skill получает строку таблицы тем же действием, которым создан» действует; его прежний текст с основанием — абзац «Состав Skill — пять файлов…» раздела ниже.'), '',
      add('### Прежние описания устройства (до 2026-10-22, дословно) — история: число файлов, их состав и правила чтения в них устарели, действуют таблица «Что читать дальше» SKILL.md и указатели references/engine.md и references/roots.md'), '']
for ln in MOVED:
    if not ln.startswith(EDITOR): b += [ln, '']
b += [add('## Основания правил'), '']
for label, section, block in BASIS:
    b.append(add(f'- {label} ({section}): ') + block[0])
    for cont in block[1:]: b.append('  ' + cont)
write(os.path.join(OUT, 'references', 'basis.md'), '\n'.join(b).rstrip('\n') + '\n')

json.dump({'added': ADDED, 'removed': REMOVED, 'basis': BASIS, 'moved': MOVED},
          open(os.path.join(OUT, '..', 'restructure_report.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('basis entries:', len(BASIS), '| added:', len(ADDED), '| removed:', len(REMOVED), '| moved:', len(MOVED))
for f in ['SKILL.md'] + ['references/' + x for x in sorted(os.listdir(os.path.join(OUT, 'references')))]:
    print(f'{os.path.getsize(os.path.join(OUT, f)):7d}  {f}')
