labs/ozon-ue/t-n8n-ozon-workflow-defects.md

# Открытые дефекты воркфлоу n8n цепочки Ozon

Суть: набор независимых дефектов воркфлоу, найденных сканом 2026-09-28 и не закрытых: формат дат адаптера против `sales_raw_operations`; ссылка на несуществующий узел в NTNN2Kvqg09yoRKi; сбой SKU Category Weekly Snapshot qZWrl0MkRnZBipXA; литеральный ключ Ozon — два найденных воркфлоу переведены Андреем на Custom Auth, третий (nE7FZhsy4V3yxB0f) архивирован (строки 782–783), остальные ~78 без Ozon в имени не проверены; ночь, упавшая в адаптере BPVFEmZF6QxXuTB6, не догоняется; узел 08_Write_To_Sheets_TEST у aVpgEnYBAgIIss4k всё ещё с onError continueRegularOutput; manual-прогон MPzPrtsnPtf0sVQo и IHn3Bmyh1VeHf4Ya для 11 неверифицированных узлов (запись строки 641 — устаревшая: часть про дашборд Ozon_Analytics_Dashboard снята 2026-09-28, строка 692; MPzPrtsnPtf0sVQo мёртв, строка 568); аудит паспортов 24.07 нашёл расхождения без записи об устранении. Правки воркфлоу через MCP небезопасны для credentials (опыт 2026-08-08) — только «да» Андрея на каждый шаг или правка в интерфейсе. Расписание мёртвого MPzPrtsnPtf0sVQo решается в лаборатории SYS, задача `labs/sys/t-ozon-ue-parked-active.md`.

Следующий шаг: взять дефекты по одному; для каждого сначала перечитать живой воркфлоу (get_workflow_details), затем «да» Андрея.

Условие снятия: каждый дефект исправлен и перечитан либо снят решением Андрея.

Ссылки: воркфлоу: BPVFEmZF6QxXuTB6 (адаптер), NTNN2Kvqg09yoRKi, qZWrl0MkRnZBipXA, aVpgEnYBAgIIss4k, MPzPrtsnPtf0sVQo, IHn3Bmyh1VeHf4Ya, FnB2Imp7thMKuwnD, M5BLqclKBjGTpz33 (Error Notifier); `registry/n8n-map.md`; `labs/sys/t-ozon-ue-parked-active.md`.

Записи источника, на которых стоит задача, — дословно (Зона Б OZON_UE_INDEX, «строка» — номер строки источника; статус на конец документа 2026-09-30 — «не закрыто» по сводке сессии переноса и по сверке Контролёра; закрытие позже по тексту документа исполнитель мог пропустить — сверять с источником):

- (строка 239) [2026-07-24] Проведён аудит всех паспортов воркфлоу OZON_UE на соответствие текущему состоянию n8n. Найдены расхождения.
- (строка 252) [2026-09-19] ОТКРЫТ: формат дат в адаптере расходится с форматом в sales_raw_operations — приводит к ошибкам сравнения при дедупликации по operation_id.
- (строка 568) [2026-09-28] ОТКРЫТ: OzonRawАналитика MPzPrtsnPtf0sVQo мёртв. Исполнение 63904 от 2026-09-17: узел 03_Ozon_Transaction_List получил {"code":9,"message":"obsolete method cannot be used"}, исполнение при этом success с нулём строк. Воркфлоу активен, расписание 02:00. OzonRawАналитика_Monat FnB2Imp7thMKuwnD ходит на тот же эндпоинт. Решение о расписании — лаборатория SYS, задача t-ozon-ue-parked-active.md.
- (строка 572) [2026-09-28] ОТКРЫТ: NTNN2Kvqg09yoRKi, узел 04_Ozon_Request ссылается на $('02_Set_Dates'), а узла с таким именем нет (есть 02_Generate_Date_Range).
- (строка 579) [2026-09-28] ОТКРЫТ: SKU Category Weekly Snapshot qZWrl0MkRnZBipXA — единственное сохранённое исполнение 66175 от 21.09 упало на узле 02_Read_SKU_Cost (Google 503); в нём же 01_Read_Sales_Unit_Economics отдаёт в строке 2 date = «#VALUE! (Unable to parse query string for Function QUERY…)».
- (строка 677) [2026-09-28] Скан литерального ключа Ozon по n8n: литерал в трёх активных воркфлоу — SElTcMg3BpY6pmdo (узел 03_Ozon_Analytics_Request, credential не выбран), NTNN2Kvqg09yoRKi (узел 04_Ozon_Request, credential выбран и заголовки оставлены), nE7FZhsy4V3yxB0f (узел 02_Fetch_All_Reviews, Code-узел в опубликованной версии; черновик чистый). Ключ во всех трёх один и тот же. Чистые: aVpgEnYBAgIIss4k, c7TIdv32dHV3MBRU, H5XqX4xXyaFuRVHb, J0v5swjXLfiANJa2, MPzPrtsnPtf0sVQo, FnB2Imp7thMKuwnD, nNNJuafLqTX7g8TU, XG4gzxtqPJXafBXN, IHn3Bmyh1VeHf4Ya, XFEhjlkrXXnl1bpU, tZ4NrzdAAurD4GQH, oJrg4XY0HZwPCq59, PWFVE0UbM3ajvVFc. Не проверены: NsOOnadQGNlbxf6g (доступ из MCP закрыт) и около 78 воркфлоу без Ozon в имени и описании.
- (строка 685) [2026-09-28] ОТКРЫТ: адаптер BPVFEmZF6QxXuTB6 — узел 05_Write_To_sales_raw_operations стоит с onError continueRegularOutput: сбой записи даёт исполнение success без данных; errorWorkflow у адаптера и у aVpgEnYBAgIIss4k не задан; дата упавшей ночи не догоняется — узел 01C_Set_Business_Date берёт «вчера».
- (строка 869) [2026-09-28] [перенесено из Зоны А 2026-09-28] [x] РУТИНА: Адаптер BPVFEmZF6QxXuTB6 — решено 2026-09-28 (Андрей): retryOnFail на Sheets-узлах оставить. Осталось сделать в интерфейсе n8n (правка через MCP пересобирает все узлы и уже сносила привязки учётных записей на Sheets-узлах, опыт 2026-08-08): узел 05_Write_To_sales_raw_operations → Settings → On Error → «Stop Workflow» вместо «Continue»; Workflow Settings → Error Workflow → «🚨 Error Notifier» (M5BLqclKBjGTpz33) у адаптера и у aVpgEnYBAgIIss4k. Готово = get_workflow_details показывает у узла 05 onError не continueRegularOutput и errorWorkflow M5BLqclKBjGTpz33 у обоих воркфлоу (переформулировано 2026-09-28) → выполнена Андреем 2026-09-28: get_workflow_details показывает у BPVFEmZF6QxXuTB6 и aVpgEnYBAgIIss4k errorWorkflow M5BLqclKBjGTpz33, у узла 05_Write_To_sales_raw_operations onError не задан (остановка). Остаток: у aVpgEnYBAgIIss4k узел 08_Write_To_Sheets_TEST по-прежнему onError continueRegularOutput.
- (строка 641) [2026-09-28] [прежний текст поля СЛЕДУЮЩИЙ ШАГ, заменён 2026-09-28, часть 1 из 5] [OZON_UE-4] закрыт 08.08 — decision layer Ozon_Analytics_Dashboard работает (90 SKU, SCALE 3). Остаток по дашборду: проверить шаг колонок блока «Слабая_прибыль» и снять/пересмотреть рычаг «Col12». Ротация API-ключа Ozon закрыта 08.08: дедлайн опровергнут (ключ бессрочный), ключ переведён на credential Custom Auth в 16 узлах. Остаток: manual-прогон MPzPrtsnPtf0sVQo и IHn3Bmyh1VeHf4Ya для проверки 11 неверифицированных узлов. Дальше по приоритету: weekly_commissions.

## 2026-10-18 — сверка списка с живым состоянием и наряды

Прочитано 2026-10-18 в снимке registry/n8n-map.md (instance_last_change 2026-10-17T16:50:52Z): BPVFEmZF6QxXuTB6 и aVpgEnYBAgIIss4k активны (ежедневно 02:20 и 02:00); NTNN2Kvqg09yoRKi активен, но расписание раз в 100 месяцев — фактически запускается только вручную; SElTcMg3BpY6pmdo неактивен; IHn3Bmyh1VeHf4Ya «OZON Fetch Reviews → Queue» неактивен; qZWrl0MkRnZBipXA снят с публикации 2026-10-17 (запись в задаче, закрытой 17.10).
Предложение сессии (решения Андрея нет): снять из списка (1) «manual-прогон IHn3Bmyh1VeHf4Ya для 11 неверифицированных узлов» — это воркфлоу отзывов, к юнит-экономике не относится, выключен, запись от 08.08 без списка узлов; (2) «аудит паспортов 24.07 нашёл расхождения» — в записи нет ни одного расхождения, проверять нечего; живое состояние воркфлоу проверяет наряд Н-18.10-02. MPzPrtsnPtf0sVQo и FnB2Imp7thMKuwnD по-прежнему ведёт labs/sys/t-ozon-ue-parked-active.md.
Выданы 2026-10-18 в чате OZON_UE: Н-18.10-02 — аудит шести дефектов в четырёх воркфлоу (BPVFEmZF6QxXuTB6, aVpgEnYBAgIIss4k, NTNN2Kvqg09yoRKi, SElTcMg3BpY6pmdo) только чтением, с вердиктом и предложением правки по каждому; Н-18.10-03 — разовый скан всех неархивированных воркфлоу на литеральный ключ Ozon воркфлоу-инструментом (создание — по «да» Андрея). Результаты — разделы «Аудит Н-18.10-02» и «Скан Н-18.10-03» в этом файле. Правки воркфлоу — после результатов, отдельным «да» на каждую.

## Аудит Н-18.10-02 (2026-10-18)

Прочитано в этой сессии 2026-10-18: get_workflow_details четырёх воркфлоу; листы через gsheets-read. Ничего не менялось, не публиковалось, не запускалось. У BPVFEmZF6QxXuTB6, aVpgEnYBAgIIss4k, NTNN2Kvqg09yoRKi опубликованная версия совпадает с черновиком (activeVersion.sameAsDraft = true); у SElTcMg3BpY6pmdo опубликованной версии нет (activeVersion = null, active = false).

D1 — ИСПРАВЛЕН. Адаптер пишет даты серийным числом: узел 03_Map_To_New_Schema, функция toSerial для business_date и operation_date (комментарий в коде: «Дату в sales_raw_operations пишем серийным числом Google Sheets»). В листе sales_raw_operations колонка B — числа (строки 2–3 и 48000–49900; исполнения gsheets-read 82136 и 82152). Записанного следствия в коде нет и не было: узел 05_Write_To_sales_raw_operations сопоставляет строки только по operation_id (parameters.columns.matchingColumns = ["operation_id"]), а operation_id — это raw_key или raw_key#sku, даты в нём нет. Не проверено: нет ли текстовых дат в строках, записанных до перевода на toSerial.

D2 — ЖИВ. Узел 01C_Set_Business_Date без входа business_date берёт $now.minus({ days: 1 }) — одна дата на прогон; у aVpgEnYBAgIIss4k узел 02_Set_Date устроен так же. Пропущенная дата — 2026-10-01 (серийное 46296): в колонке B sales_raw_operations после 46295 сразу идёт 46297 (исполнение 82152); лист «Деньги по неделям» книги «Деньги», неделя 28.09–04.10 — «Дней с данными» 6 (исполнение 82135). Исполнение адаптера в ту ночь (запуск 2026-10-02 около 00:20 UTC) — НЕ ПРОВЕРЯЕМО: инстанс хранит у обоих воркфлоу только 10 последних исполнений, самые старые — 77331 и 77326 от 2026-10-09.
Правка, способ — интерфейс n8n (правка через MCP пересобирает узлы и сносила привязки ключей доступа 08.08). Узел 01C_Set_Business_Date, две последние строки кода.
было: const business_date = override !== '' ? override : $now.minus({ days: 1 }).toFormat('yyyy-MM-dd'); return [{ json: { business_date: business_date, date_source: override !== '' ? 'override' : 'yesterday' } }];
стало: if (override !== '') return [{ json: { business_date: override, date_source: 'override' } }]; return [1, 2].map(d => ({ json: { business_date: $now.minus({ days: d }).toFormat('yyyy-MM-dd'), date_source: 'back_' + d } }));
Та же правка в узле 02_Set_Date воркфлоу aVpgEnYBAgIIss4k — код узла целиком.
было: блок от const business_date = override !== '' до конца узла (return [ { json: { business_date: business_date, date_source: … } } ];)
стало: if (override !== '') return [{ json: { business_date: override, date_source: 'override' } }]; return [1, 2].map(d => ({ json: { business_date: $now.minus({ days: d }).toFormat('yyyy-MM-dd'), date_source: 'back_' + d } }));
Без неё адаптеру нечего догонять: он читает только то, что записано в ozon_raw_accrual_TEST. Почему безопасно: обе записи — appendOrUpdate по ключу (operation_id, raw_key), повтор дня обновляет строки, а не дублирует. Риск: прогон aVpgEnYBAgIIss4k длится 5–7 минут (исполнения 77326–81840), с двумя днями — примерно вдвое дольше, а адаптер стартует через 20 минут; сдвинуть расписание адаптера с 02:20 на 02:40. Проверка после правки: в первом исполнении узел 02_Read_RAW_Accrual отдаёт строки обоих дней.
Догнать 01.10 отдельно: сначала проверить строки business_date = 2026-10-01 в ozon_raw_accrual_TEST; нет — ручной запуск aVpgEnYBAgIIss4k с этой датой; затем адаптер с business_date = 2026-10-01 через 00_Execute_Workflow_Trigger; готово = неделя 28.09–04.10 на листе «Деньги по неделям» показывает 7 дней после пересчёта книги.

D3 — ИСПРАВЛЕН. Узел 08_Write_To_Sheets_TEST: ключа onError нет (действует остановка), retryOnFail = true; у соседних узлов 03 и 05 ключ onError в той же выдаче есть — отсутствие не артефакт. Пишет в книгу RAW 1P-GgiFm3067U_sgC2Dojos3BbT_-au6v-mT52vVT3y4, лист ozon_raw_accrual_TEST, appendOrUpdate по raw_key. Нужен: это единственный источник адаптера — его узел 02_Read_RAW_Accrual читает тот же лист. Суффикс _TEST у узла и листа вводит в заблуждение: запись боевая.

D4 — ЖИВ. Узел 04_Ozon_Request, parameters.body: «"date_from": "{{ $('02_Set_Dates').item.json.date_from }}"», так же date_to; узла 02_Set_Dates нет, вход идёт из 02_Generate_Date_Range. Узел стоит с onError = continueRegularOutput, поэтому запуск даёт success с нулём строк. На данные сейчас не действует только потому, что воркфлоу запускается вручную (Schedule Trigger, monthsInterval = 100).
Правка, способ — интерфейс n8n. Узел 04_Ozon_Request, поле Body: было $('02_Set_Dates').item.json.date_from → стало $json.date_from; было $('02_Set_Dates').item.json.date_to → стало $json.date_to.

D5 — ИСПРАВЛЕН. Узел 04_Ozon_Request: authentication = genericCredentialType, genericAuthType = httpCustomAuth, ключ доступа выбран; в parameters нет sendHeaders и headerParameters — литерала нет. Черновик и опубликованная версия одна и та же (versionId = activeVersionId).

D6 — ИСПРАВЛЕН (черновик); опубликованной версии нет. Узел 03_Ozon_Analytics_Request: authentication = genericCredentialType, genericAuthType = httpCustomAuth, ключ доступа выбран; заголовков в parameters нет — литерала нет. Остаток: в поле credentials узла привязан второй ключ доступа другого (заголовочного) типа; при genericAuthType = httpCustomAuth он не используется. Старые версии истории воркфлоу не проверялись — они не исполняются.

### Находки вне рамки

1. aVpgEnYBAgIIss4k, узлы 03_Ozon_Accrual_By_Day и 05_Ozon_FBS_Posting_Get: onError = continueRegularOutput и options.response.response.neverError = true. Отказ Ozon (429, 5xx, 401) проходит дальше как обычный ответ без accruals: 04_Flatten_Accruals даёт ноль строк, 08 пишет ноль, исполнение success, Error Notifier не срабатывает. Тот же класс, что D3, одним узлом выше. Гипотеза (не проверена): ночь 01.10 потеряна так. Проверить: строки 2026-10-01 в ozon_raw_accrual_TEST. Правка — по решению Андрея: у узла 03 снять neverError и onError; узел 05 — обогащение, его отказ теряет только order_date и имя.
2. Там же, 03_Ozon_Accrual_By_Day: пагинация maxRequests = 20 при limitPagesFetched = true — день длиннее 20 страниц обрежется молча. Гипотеза (не проверена): бывает ли больше 20 страниц. Проверить: число страниц на выходе узла 03 в свежем исполнении.
3. NTNN2Kvqg09yoRKi: описание обещает загрузку с 2026-01-01, а 02_Generate_Date_Range жёстко отдаёт одну дату 2026-06-21 — инструмент перенастраивается руками перед каждым запуском.
4. SElTcMg3BpY6pmdo, узел 06_IF_Is_429: leftValue «{{ $json.error.httpCode }}» без знака «=» — выражение не вычисляется, сравнивается литеральный текст, ветка повтора на 429 не срабатывает никогда; второе условие с leftValue = null. Воркфлоу выключен — на данные не действует.
5. Боевые адаптер и aVpgEnYBAgIIss4k хранят только 10 последних исполнений: пропуск старше 10 дней по исполнениям не расследуется.


## Скан Н-18.10-03 (2026-10-18)

Результат: находок 0. Просмотрено 244 воркфлоу, из них неархивированных 146; 98 архивных пропущены по условию наряда.

Прочитано в этой сессии:
- Инструмент: воркфлоу «Ozon key literal scan», ID 2g4zVTcfYLLwrF73, три узла (ручной запуск, запрос списка воркфлоу к API n8n с ключом доступа «n8n API - monitor_key_v2», Code-узел с самопроверкой и сканом). Не опубликован, расписания нет, остаётся как инструмент. Привязку ключа к HTTP-узлу показал get_workflow_details (поле credentials).
- Исполнение 82163, статус success, ручной режим. Самопроверка в нём прошла: 8 синтетических случаев — литерал в заголовке Api-Key находится; выражение в заголовке не находится; литерал в Code-узле рядом с Api-Key находится; UUID внутри выражения не находится; UUID в теле запроса к api-seller.ozon.ru находится как «прочее»; UUID без контекста Ozon не находится; литерал только в опубликованной версии находится; архивный воркфлоу пропускается. Поддельный UUID собирается в коде из кусков. Проверка самой самопроверки: при намеренно сломанной регулярке заголовка локальный прогон падал на трёх случаях, прогон с исправной регуляркой проходил.
- Счёт: 244 воркфлоу всего, 146 неархивированных, 98 архивных, 3 страницы выдачи, курсор в конце пуст. Снимок registry/n8n-map.md насчитывал 243 и 145: разница в один — сам инструмент, созданный до запуска. Число просмотренных не меньше числа неархивированных в снимке, условие опровержения замысла не сработало.
- Находок по видам: заголовок 0, код 0, прочее 0. Узлов с UUID внутри выражения ={{…}}: 0.
- Версии: 70 воркфлоу ни разу не публиковались; у 76 опубликованных versionId равен activeVersionId; воркфлоу с расхождением черновика и опубликованной версии нет. Поэтому вопрос «отдаёт ли API узлы опубликованной версии» в этом прогоне не возник и не проверялся: ответ на него неизвестен. Для 76 опубликованных версия совпадает с черновиком по идентификатору, скан покрывает обе.

Независимый контроль (частичный): в сохранённой части выдачи — 100 воркфлоу из 244 — 21 HTTP-узел с Api-Key или адресом api-seller.ozon.ru имеют привязанный ключ доступа и не содержат UUID в параметрах; 2 Code-узла с такими признаками тоже без UUID. Остальные 144 воркфлоу этим контролем не покрыты.

Прецеденты скана 28.09: nE7FZhsy4V3yxB0f теперь архивирован (get_workflow_details ответил «archived and cannot be accessed»), поэтому вне области скана; состояние его опубликованной версии не проверено. По SElTcMg3BpY6pmdo и NTNN2Kvqg09yoRKi находок нет — согласуется с вердиктами D6 и D5 аудита Н-18.10-02.

Границы метода: находка «заголовок» или «код» требует признака Api-Key или api-seller.ozon.ru в том же узле; литерал в одном узле (например Set) с выражением-ссылкой в другом не находится; ключ, не похожий на UUID, не находится; архивные воркфлоу не сканировались.

### Находки вне рамки

1. Литерал ключа Ozon стоял в трёх воркфлоу (скан 28.09, один ключ во всех). Скан смотрит текущие версии, не историю версий. Гипотеза (не проверена): в истории версий этих воркфлоу остался старый литерал. Проверить: get_workflow_history и get_workflow_version по трём воркфлоу, считать только число UUID, значения не выводить. Ротация ключа — решение Андрея; по тексту Skill n8n-engineering-manual (пункт 2.1, редакция 2026-10-09) ключ тогда ещё не ротирован, с живым состоянием не сверено.

## Приёмка Н-18.10-02 и Н-18.10-03 (2026-10-18, сессия OZON_UE)

Приняты оба. Сверено отдельным посредником по живым воркфлоу (get_workflow_details 2026-10-18, только чтение): aVpgEnYBAgIIss4k — у узла 03_Ozon_Accrual_By_Day onError = continueRegularOutput и options.response.response.neverError = true, опубликованная версия равна черновику; у 08_Write_To_Sheets_TEST ключа onError нет, retryOnFail = true, лист ozon_raw_accrual_TEST; BPVFEmZF6QxXuTB6 узел 01C_Set_Business_Date и aVpgEnYBAgIIss4k узел 02_Set_Date — «$now.minus({ days: 1 })»; NTNN2Kvqg09yoRKi узел 04_Ozon_Request — «$('02_Set_Dates')», узла с таким именем нет; 2g4zVTcfYLLwrF73 «Ozon key literal scan» — active false, не архивирован, только ручной запуск. updatedAt адаптера и сборщика 2026-10-08 — после аудита их не правили. Пропуск 01.10 (исполнение gsheets-read 82152) и скан 244 воркфлоу (исполнение 82163) — ПРОЧИТАНО ПОСРЕДНИКОМ (исполнители нарядов), сессией не перечитывались.
Закрыто вердиктами: D1, D3, D5, D6 (исправлены до аудита); литеральный ключ в текущих версиях — 0 находок.
Остаётся (порядок — предложение сессии, решения Андрея нет):
1. Узел 03_Ozon_Accrual_By_Day сборщика aVpgEnYBAgIIss4k (находка вне рамки 1 аудита) — первым: пока отказ Ozon превращается в успешный прогон с нулём строк, догонялка D2 тоже получит ноль и пропуск не будет виден. Правка: снять neverError и поставить onError в остановку — тогда отказ уронит прогон и Error Notifier сообщит.
2. D2 — догон двух дней (текст «было → стало» выше в разделе аудита) и сдвиг адаптера на 02:40; затем догнать 01.10.
3. D4 — по случаю, инструмент ручной.
4. Пагинация 20 страниц (находка 2) — проверить число страниц в свежем исполнении узла 03 до решения.
Историю версий и ротацию ключа предлагается не делать: литерал жил только внутри инстанса n8n, в публичный репозиторий не попадал, а доступ к истории версий есть только у того, у кого уже есть доступ к инстансу и к самим ключам доступа. Это мнение сессии; решение Андрея.
Предлагается снять из списка задачи (решения Андрея нет, запись 2026-10-18 выше): ручной прогон IHn3Bmyh1VeHf4Ya и «аудит паспортов 24.07».

## 2026-10-18 (автопилот OZON_UE) — правка узла 03 выдана Андрею

Сборщик aVpgEnYBAgIIss4k не правился после аудита: get_workflow_details 2026-10-18, updatedAt 2026-10-08T11:09:22Z, versionId = activeVersionId a3f06d9b. Андрею выдан текст правки в интерфейсе n8n: узел 03_Ozon_Accrual_By_Day → Options → Response → Never Error выключить; Settings → On Error «Continue (regular output)» → «Stop Workflow»; сохранить и опубликовать. Не внесено до чтения объекта.
