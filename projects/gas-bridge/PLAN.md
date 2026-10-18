projects/gas-bridge/PLAN.md

# PLAN_gas-bridge — цель, границы, устройство, контракт вызова

Проект-инструмент. Единственный носитель — эта папка репозитория; Claude Project и INDEX в Google Docs нет. Заведён 2026-10-18 на месте проекта sku-cost, у которого цель Андрея была понята неверно (`LOG.md` Р-1). Правила записи — Skill `second-brain-git`.

Куда писать: сдвинулось состояние — `STATE.md`; решение или неудачная попытка — `LOG.md`; изменилось правило или устройство — этот файл.

## Цель

Этап А (принят 2026-10-18, `LOG.md` Р-2). Любая сессия Claude сама, без участия Андрея и без его включённого компьютера, читает, правит и откатывает код Google Apps Script его книг Google Sheets.

Этап Б. На этом инструменте расширять автономность системы: сессии проектов (юнит-экономика, учёт торговли на маркетплейсах) сами строят и чинят скрипты своих книг.

## Границы

- Сессия читает, записывает и откатывает код. Функции запускает Андрей: запуск меняет данные книги необратимо, а запуск через интерфейс Google требует перевести каждую книгу в проект Google Cloud. Запуск — этап Б, отдельным решением.
- Запись — только в скрипты, у которых в таблице данных n8n `gas_allowlist` стоит доступ `write`. Строка с `write` добавляется только после слова Андрея в чате. Чтение — любой скрипт, доступный аккаунту Андрея.
- Перед каждой записью и каждым откатом создаётся версия проекта скрипта; номер версии приходит в ответе.
- Код книг в репозиторий не пишется: репозиторий публичный, запись в него необратима (`second-brain-git`, инвариант И-7).
- Clasp на компьютере Андрея — ручной запасной путь (Skill `clasp-apps-script`), не основа.

## Устройство

- Воркфлоу «Claude → Google Apps Script Bridge», ID `38BkuLXhxXLTPpqQ`, не опубликован: сессии вызывают его через execute_workflow в режиме manual. Операции read, write, rollback, create.
- Подворкфлоу «Claude → Google Apps Script Bridge · Call», ID `j0DU23IXnp7xggX9`, опубликован, вызывать его может только `38BkuLXhxXLTPpqQ`. Делает один запрос к Apps Script API ключом «Google Apps Script (Andrei)». Вынесен отдельно, потому что узел HTTP Request оставляет сырой ответ Google в contextData своего исполнения, а сужение nodeNames этого не режет (`LOG.md` Р-2).
- Ключ «Google Apps Script (Andrei)» — тип Google OAuth2 API, право только `https://www.googleapis.com/auth/script.projects`, экран согласия проекта Google Cloud в статусе «In production». Права на Диск не нужно: привязка скрипта к книге, созданной другим приложением, работает с одним этим правом (исполнение 82243).
- `gas_allowlist` — таблица данных n8n, ID `LqcwS0U0B3spMaIk`: scriptId, spreadsheetId, title, access (`read` или `write`), added (кто и когда). Найти скрипт по идентификатору книги интерфейс Google не умеет. Для существующей книги идентификатор скрипта берётся из списка «Мои проекты» на script.google.com (встроенный браузер, вход уже выполнен) и проверяется ссылкой на книгу на странице «Описание проекта» скрипта (`LOG.md` Р-3).
- Отпечаток проекта (projectHash) — 16 шестнадцатеричных знаков, считается по именам, типам и текстам всех файлов; это проверка изменений, а не криптографическая защита.

## Ограничения Google — не дефект, не расследовать

- Запись (projects.updateContent) заменяет весь проект и версию не проверяет. Полной защиты от одновременной правки нет; сверка отпечатка основы сужает окно до секунд.
- Если Андрей правит код во вкладке редактора, открытой до записи сессии, его сохранение затрёт запись сессии. Без правок вкладка ничего не сохраняет.
- Файл манифеста appsscript.json Google переформатирует: при сверке после записи он сравнивается как разобранный JSON, а не побайтно.
- Выход узлов вызова в исполнении главного воркфлоу содержит ответ Google целиком, включая адрес почты автора правки. Поэтому ответ читается только с сужением до узла 90_Respond.

## Контракт вызова (для сессий, компактно)

```
execute_workflow workflowId=38BkuLXhxXLTPpqQ executionMode=manual triggerNodeName=01_Webhook
  inputs={webhookData:{method:"POST",body:{...}}}
get_workflow_execution workflowId=38BkuLXhxXLTPpqQ executionId=<id> includeData=true nodeNames=["90_Respond"] truncateData=1
  -> data...90_Respond[0].data.main[0][0].json.result ; status "running" -> wait 10 s, re-query, never re-execute
body:
  read     {op:"read", scriptId, mode?:"list"|"source", fileName?:str|str[], maxChars?:60000, versionNumber?}
           -> {success, projectHash, fileCount, files:[{name,type,chars,fileHash,source?,truncated?}], truncated, reason}
  write    {op:"write", scriptId, fileName, baseHash:<projectHash from fresh read>, description,
            source:<whole file> | oldStr+newStr:<one unique fragment>, fileType?:"SERVER_JS"|"HTML"|"JSON" (new file only)}
           -> {success, versionBefore, projectHashBefore, projectHashAfter, verifiedFiles, mismatches, rollbackHint, reason?}
  rollback {op:"rollback", scriptId, versionNumber, description} -> same as write + rolledBackTo, hashMatchesTarget
  create   {op:"create", spreadsheetId, title?} -> {success, scriptId, projectHash, files, allowlistUpdated}
refusals (nothing written): NOT ALLOWED (not write in gas_allowlist), STALE BASE (re-read, redo), oldStr count != 1,
  ALREADY BOUND, GOOGLE <code>: ... HINT (key, API switch, wrong id)
rules: always read -> write with that projectHash; truncated:true file is incomplete, never edit from it;
  fileName has no extension (as listed by read); report versionBefore so the change can be undone.
```

## Контракт автопилота этапа А (исполнен)

Согласован Андреем 2026-10-18 словом «да» в чате SYS после ревизии denken уровня 2. Критерий приёмки — шесть пунктов: чтение, привязка, запись с версией, откат, две защиты, описание проекта. Итог по каждому пункту — `LOG.md` Р-2. Разрешённые правки контракта исполнены; правка gscript-read не понадобилась — чтение перенесено в новый воркфлоу (Р-2).
