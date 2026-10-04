projects/wb-logistics/PLAN.md

# PLAN_wb-logistics — цель, архитектура, инструменты (правила проекта)

Перенесено из WB_LOGISTICS_INDEX (Google Doc `1mxYgiK9X4qOId2vNF7xnne-cQszTqPpJZHux_AuDZjQ`), снимок на дату переноса 2026-10-04: экспорт Docs, 85 812 Б (UTF-8, CRLF), 760 строк, sha256 c383cb39cf965de7690e03feaf127b7d8f0e35928325502ce3be2c6cecd92713, исполнение gdocs-read 74959, по протоколу `meta/PROTOCOL_file-migration.md`, этап 0в. Строки источника перенесены без перенабора моделью (сборка скриптом). Что не взято и почему — `projects/wb-logistics/NOT_TAKEN.md`. Состояние и открытые задачи — `STATE.md`, решения и опыт — `LOG.md`.

## ПРОЕКТ

ПРОЕКТ: Автоматическая система логистических решений WB FBS «Везти сегодня или нет?»
СТАТУС: Активен
ВЕС: 7

## ЦЕЛЬ

Каждые 15 минут в окне 12–16 МСК: забрать заказы из WB API, посчитать тариф, сравнить с поездкой, пушить решение в Telegram. Отдельно — трекинг каждого заказа (время сборки → зона скорости → бонус/штраф).

## СВЯЗИ

Price Master (1mntwAaplJSn3bHczqGDrzmBjotrsHe3MZ78ChViCDVk) → источник цен и объёмов для всех воркфлоу
Ozon FBS → следующий проект после стабилизации WB

## ПРАВИЛО НАВИГАЦИИ

ПРАВИЛО НАВИГАЦИИ (2026-07-18): при технической задаче по воркфлоу сначала читать карту WB_LOGISTICS_SYSTEM-MAP (1VcFVj9PxL-UiQW4I0wuIwUOkaVBT53H-htxfD8Jcxa8) — она укажет единственный нужный паспорт; НЕ читать все паспорта подряд.

## ДОКУМЕНТЫ

Карта системы WB_LOGISTICS_SYSTEM-MAP: 1VcFVj9PxL-UiQW4I0wuIwUOkaVBT53H-htxfD8Jcxa8

## ИНСТРУМЕНТЫ

WB_FBS_Logistics_Calculator (Sheets): 1AhgaspMQl3wLsVT7Iub0d195r8DwwUarhQAWwjBO8xE
WB_FBS_Performance_Monitor (Sheets): 1iGMBRgdt8GqKnJU4yhJAfpG-_w-9f8q_G51w5myxlSw
Мастер-промпт: 1jGfkSpMLZ3kMCRmlU8IjxsT_3vzlM0ikpUb4CU-0sQM
Справочник тарифов: 1YczbMKezk7YHLLvJTXaySuRmtRoex0UK1FoVOyS95H8
Документация Ozon FBS: 1DRHbgipyu40AoLFd_z_qvycaQPMvHnoG4PAjRej6P5E
DOCS папка: 1H_JNBn7PrtUQomzS-xjGsMXYsGKLctZB

Паспорт decision-engine → 1shad9S_zIlYsWY3ih98WE-X9YfPtdchXZvXeDsTW1gs
Паспорт morning-forecast → 1NL5z2zhEpk6T6m8tFRe_QykS1UOY3y09jam1wxrJ1Vc
Паспорт evening-report → 1rCP1BQNiHpGYLNSdBG1I0xgumMZExn9t2hmrs2snm_c
Паспорт order-intake → 1Nv_cRmCDwcPvFKofQ9gtPZv3e7umUlIuwYNMkH0TinQ
Паспорт order-close → 1ikcY36iGUjVX5fKkuXf1XwYOI2brHHH9-y4efd6v5jo
Паспорт order-close-v2 → 18eYTDWMfoGvt71VUXMfwDhTalIH4IS2EqezNjWRUPZU
Паспорт supply-close → 1fRL27a6QZEH6GYRgO3VfmqjTmOZnfG0JxQxozwlJecY
Паспорт telegram-router → 1TH958D_ryD7rAyDwxMZzTFRfo8Q0t74sjyy57Cj6P-Q
Паспорт supply-accepted → 1cpIRUdaBFWklCfBNTxOfW2WNd4ikAZOMwB7tQCGepS4
Паспорт supply-tracking-sync → 1V97fXuLHJmuPw2ElVJvdi5vc4oJSCXZRF65MWg8an4k

wb_fbs_orders_tracking (Sheets, включает performance_log + monitor_params, подтверждено кодом 7 воркфлоу, SYSTEM-MAP 18.07): 1qdefReY1qHfWdwroorbxz2Bi20_3dsGHuDBiYy2W_XQ. NB 2026-10-04: книга 1qdefReY… называется WB_FBS_Performance_Monitor — это она. ID 1iGMBRgdt… в Drive не существует (not found), строку WB_FBS_Performance_Monitor выше не использовать.

Воркфлоу — полный состав, роли, статусы и паспорта: см. карту WB_LOGISTICS_SYSTEM-MAP, разделы 3-4. (2026-07-18: список ниже устарел — не расширять, для навигации не использовать: Supply Close и Order Close v1 там без пометки о реальном статусе, подтверждённом живым кодом.):
  Decision Engine: S4rZMUkI21dVu3ML
  Order Intake: kNg2uEoYlaGOLC82
  Order Close v1: cscGFbFuz55DZJCw — ОСТАНОВЛЕН 2026-06-28 (unpublish, заменён v2)
  Order Close v2 [Supply Summary]: DM26WhTJyCV0DhkP
  Morning Forecast: 6M9nS9iKQzMdztUs
  Evening Report: 0fesM63M92naAnOl
  Supply Close: W1CRVcAN2gFHRY01
  Telegram Router: YQBfmS0fC7IPcsbz
Supply Accepted: 7x9wPrugdbseaEp2

## Правила, записанные опытом (указатель; текст — в `LOG.md`, не дублируется)

- Процессное правило про момент отправки /supply и урок о ручных правках кода ноды (полная замена кода, обязательный Publish) — `LOG.md`, запись Р-89 (блок 2026-07-06).
- Опыт update_workflow через MCP (сброс settings.timezone, errorWorkflow и waitBetweenTries) и парсинга дат из Sheets — `LOG.md`, запись Р-95 (блок 2026-10-02).
- Паттерны n8n, Sheets и WB API — `LOG.md`, записи Р-47…Р-62; ошибки и решения — Р-63…Р-70.
