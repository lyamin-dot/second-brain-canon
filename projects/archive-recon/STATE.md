projects/archive-recon/STATE.md

## Статус фаз

Ф1 (обход тестовой папки Google Drive, сбор правил организации) — завершён по всем тематическим подпапкам корня (25 штук: Sepsis из предыдущего прохода плюс 24 остальных).
Ф2, Ф3 — не начаты.

## Сделано в Ф1

- Пройдены все 24 оставшиеся тематические подпапки корня: Kardiologie, Notarzt, ANTIBIOTIKA, Delir, Regionale A, Facharzt Anästhesie ZUM LESEN, 2025 CME Artikel, 00 ZERTIFIKATE, 00 Ziele, 00 SONO, 2024 CME Artikel, Fortbildungen, H3A Persoenlich, Beatmung, TransfusuonsMedizin, SchockRaum, Sedierung, Thorax, Allgemeine Chirurgie, Leitender NA, Neurochirurgie, Meine Vorträge, Medikamente, ÜberstundenKontrolle — по правилам из «Параметры обхода» PLAN.md: выборка до 5 элементов, глубина до 2 уровней, без read_file_content.
- Обход выполнен 24 вызовами search_files (по одному на подпапку), без единого read_file_content — подтверждает вывод Т-1 LOG.md: обход структуры дешёвый, если не читать содержимое статей.

## Таблица правил (по итогам Ф1)

| паттерн | где встречен | число подтверждений | пример пути |
|---|---|---|---|
| дата-папка на статью, статус OHNE MM, пара MM.pdf+.mom при готовности | Sepsis, Delir, ANTIBIOTIKA, TransfusuonsMedizin, Neurochirurgie, SchockRaum, Beatmung, Notarzt, 2024 CME Artikel | 9 из 25 подпапок корня (частично или полностью) | Sepsis/2024.08 OHNE MM .../ |
| плоские PDF прямо в тематической папке, без подпапок и без OHNE MM | Regionale A, 2025 CME Artikel, Thorax, Allgemeine Chirurgie, Leitender NA, Sedierung, Medikamente, TransfusuonsMedizin (частично) | 8 из 25 | 2025 CME Artikel/*.pdf |
| нетематические (не по датам) под-папки второго уровня — категория/книга/курс | Facharzt Anästhesie ZUM LESEN, 00 SONO, Beatmung, Notarzt («Rea»), Meine Vorträge | 5 из 25 | 00 SONO/01 POCUS Buch/ |
| одиночные Google Docs «gpt …» вперемешку с любым из паттернов выше — заметки/конспекты из сессий с ChatGPT, размер от нескольких КБ до >2 МБ | корень, Sepsis, Kardiologie, TransfusuonsMedizin, Sedierung, Thorax, Neurochirurgie, Medikamente, SchockRaum | 9 из 25 | TransfusuonsMedizin/gpt ROTEM |
| папка целиком вне темы специальности (сертификаты, личные цели, конспекты выступлений, учёт рабочего времени, материалы курсов по месту/дате) | 00 ZERTIFIKATE, 00 Ziele, Fortbildungen, H3A Persoenlich, Meine Vorträge, ÜberstundenKontrolle | 6 из 25 подпапок корня целиком вне предмета | H3A Persoenlich/BettenPlan.pdf |

## Нераспознанные случаи

- Файлы-ярлыки (.lnk и нативные ярлыки Google Диска) вместо самого документа — указывают на внешний Leitlinie-файл, не содержат текста сами. Встречены в Regionale A, Sedierung, 00 ZERTIFIKATE.
- Дубликаты одного и того же файла в разных тематических папках (пример: «Nicht-traumatologisches Schockraummanagement…» лежит и в 2025 CME Artikel, и в SchockRaum, оба с суффиксом «- kopie»).
- Файл с расширением .pdf, но mimeType text/plain и размером 102 байта («Pharmacologic treatment of agitation in traumatic brain injuries.pdf», Neurochirurgie) — расширение не соответствует содержимому, похоже на битый файл или заглушку, не на статью.
- Отдельный служебный документ-трекер «CME Gelesen aber kein MindMap» (2024 CME Artikel) — вручную ведённый список статуса обработки на уровне папки, отдельно от маркера OHNE MM в имени файла.

## Следующий шаг

Ф1 закрыта по всем подпапкам корня. Следующий шаг — Ф2: проверка этих правил за пределами тестовой папки (ждёт доступа к фрагменту главного архива — И-6 PLAN.md запрещает считать тестовую папку представительной без проверки).

## Открытые вопросы владельцу

Нет открытых.

## Блокеры

Ф2 не может начаться без доступа к части главного архива (сейчас недоступен — см. Основание PLAN.md).