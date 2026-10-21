#!/usr/bin/env python3
"""Apply carrier transfers of the apps-script-sheets synthesis to a clone.
Usage: apply_carriers.py CLONE_DIR. Idempotent: each text is added only if absent."""
import sys, pathlib
R = pathlib.Path(sys.argv[1])
SRC = 'синтез Skill apps-script-sheets 2026-10-20, отчёт meta/SYNTHESIS_apps-script-sheets_2026-10-20.md'

def append(path, text):
    p = R / path
    t = p.read_text()
    if text.strip() in t:
        return f'skip {path}'
    if not t.endswith('\n'):
        t += '\n'
    p.write_text(t + '\n' + text + '\n')
    return f'append {path}'

def insert_after(path, anchor, text):
    p = R / path
    t = p.read_text()
    if text.strip() in t:
        return f'skip {path}'
    assert t.count(anchor) == 1, (path, anchor, t.count(anchor))
    p.write_text(t.replace(anchor, anchor + text, 1))
    return f'insert {path}'

out = []
# --- labs/ozon-ue/t-books-followups.md : three facts removed from the Skill
out.append(append('labs/ozon-ue/t-books-followups.md',
f"""## 2026-10-20 — факты книг, снятые из Skill apps-script-sheets синтезом ({SRC})

Skill больше не держит особенностей конкретных книг (решение Андрея 2026-10-20 «Skill — инструкции для всех», `labs/sys/t-knowledge-synthesis.md`); три факта книг этой лаборатории перенесены сюда без изменения смысла. Источник каждого — текст Skill до синтеза: зеркало `skills/apps-script-sheets/` на коммите aeb4b23.
- Часовой пояс (бывший §2.7 Skill): 2026-09-28 часовой пояс проекта скрипта и пояс книги «Деньги» совпадают — проверено результатом, а не настройками: после перевода дат функцией `localDate_` даты недель на листе «Деньги по неделям», прочитанные `gsheets-read` с `render:"UNFORMATTED_VALUE"`, — целые числа. У книг «Цена» и «Товары» совпадение отдельно не проверялось.
- Сверка «Получили» (бывший §4.5 Skill): по тексту Skill, сверка «Получили» стоит в отчёте прогона всех трёх книг — «Цена», «Деньги», «Товары» — и 2026-09-28 дала 0,00 ₽. Для «Денег» и «Товаров» это записано выше; для «Цены» чтение-доказательство в каноне не записано — Гипотеза (не проверена).
- Время прогона (бывший раздел 8 Skill): скрипт каждой из трёх книг «Цена», «Деньги», «Товары» на 2026-09-28 шёл 34–53 секунды. С 2026-10-14 прогоны «Денег» и «Товаров» срываются по лимиту 6 минут — `t-money-telegram.md`, раздел «Диагностика Н-18.10-01».
"""))
# --- labs/ozon-ue/t-goods-book-script.md : N() note
out.append(append('labs/ozon-ue/t-goods-book-script.md',
f"""## 2026-10-20 — факт книги, снятый из Skill apps-script-sheets синтезом ({SRC})

Колонка «Диагноз» книги «Товары»: E и F — числа, записанные скриптом, поэтому проверка знаменателя стоит без `N()` (по тексту Skill до синтеза, §3.3; зеркало на коммите aeb4b23; состояние на 2026-09-28). Если E или F станут формулами, возвращающими "", — обернуть в `N()` (Skill apps-script-sheets, references/book-traps.md, §3.3).
"""))
# --- registry/documents.md : WB_Аналитика book id
out.append(append('registry/documents.md',
f"""<!-- 2026-10-20 | синтез Skill apps-script-sheets: ID снят из references/samples.md Skill, в реестре его не было -->
WB_ANALITIKA_book: 1sBYaluh1NDkb0zVmbV-NX4jsNbawEpXlae8fRg2AiuI — Google Sheets «WB_Аналитика», старая книга юнит-экономики Wildberries (витрина «норма → отклонение → светофор», скрипт WB_Monitor.gs). Заморожена окончательно 2026-10-17 (запись Р-69 журнала projects/wb-ue/LOG.md, пункт 8); её заменила «WB · Деньги» (WB_MONEY_book). Не удалять, пока «WB · Деньги» читает из неё wb_reports_official."""))
# --- projects/wb-ue/PLAN.md line 44: names of the two documents
p = R / 'projects/wb-ue/PLAN.md'
t = p.read_text()
a = 'RU `10f6nbTUWMZQJm2dApneCuZEiLPCRE-CoukI3ihRCpoI`, EN `13uULDvR5l5aBUsEM7vR93_GXk_OvU7HZkBEyDQozvsw`.'
b = ('RU `10f6nbTUWMZQJm2dApneCuZEiLPCRE-CoukI3ihRCpoI` (имя документа «КОНСТРУКТОР_витрины_норма-светофор»; содержание: пять слоёв, разметка каждого листа, шаблон колонок, формула отклонения и правило сигнала, метод подбора порога, порядок сборки, чек-лист переноса на другую площадку; читать через gdocs-read), '
     'EN `13uULDvR5l5aBUsEM7vR93_GXk_OvU7HZkBEyDQozvsw` (имя DASHBOARD_BLUEPRINT_EN, компактная копия для агента; издание 1 от 2026-09-16, сверено с книгой WB_Аналитика до её заморозки 2026-10-17; имена сняты из Skill apps-script-sheets синтезом 2026-10-20).')
if b not in t:
    assert t.count(a) == 1
    p.write_text(t.replace(a, b, 1)); out.append('edit projects/wb-ue/PLAN.md')
else:
    out.append('skip projects/wb-ue/PLAN.md')
# --- projects/wb-ue/STATE.md : three neighbour lines
lines = (
"- ⚡ Это затрагивает WB_UE (от SYS, 2026-10-20, синтез Skill apps-script-sheets, отчёт `meta/SYNTHESIS_apps-script-sheets_2026-10-20.md`): две записи канона расходятся о разделителе формул книги Price Master — запись Р-64 журнала `projects/wb-ue/LOG.md` (2026-10-14) говорит «,», `meta/PRODUCT_DATA_HIERARCHY.md`, раздел 4в, строка 42 (2026-10-09) — «;». Проверить чтением любой многоаргументной формулы книги через `gsheets-read` с `render:\"FORMULA\"` и исправить неверную запись; если локаль книги менялась — записать дату смены. Skill теперь велит определять разделитель пробой в каждой книге (§0.2), значение книги живёт здесь.\n"
"- ⚡ Это затрагивает WB_UE (от SYS, 2026-10-20, тот же синтез): раздел «Открытый риск (2026-09-23, дополнен 2026-09-28; не закрыт…)» ниже противоречит записи Р-69 журнала `projects/wb-ue/LOG.md`, пункт (8): там риск weekly_history!11 и cost_monitor!B10 закрыт без исполнения (книга заморожена). Пометить раздел закрытым со ссылкой на Р-69.\n"
"- ⚡ Это затрагивает WB_UE (от SYS, 2026-10-20, тот же синтез; вопрос 3 пакета правок харвеста `meta/HARVEST_2026-10-18_edits/apps-script-sheets.md`): курьер Telegram WB проверяет возраст только по последней дате данных (LAST_DATA_DATE, порог 10 дней) и не читает метку последнего прогона книги «WB · Деньги»; если встанет ежедневный пересчёт самой книги, сообщение придёт не раньше чем через 10 дней после последней даты данных. Решить: добавить чтение метки прогона книги в существующий курьер (новый воркфлоу не нужен) — Skill apps-script-sheets, references/signal.md, §9.9.\n"
)
out.append(insert_after('projects/wb-ue/STATE.md', '## От соседнего проекта\n\n', lines))
print('\n'.join(out))
