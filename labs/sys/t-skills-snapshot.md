labs/sys/t-skills-snapshot.md

# Снимок n8n-workflow-registry отстал от канона

Суть: снимок Skill `n8n-workflow-registry` в Customize расходится с каноническим текстом — старая фраза подтверждения и самовложенный дубль frontmatter. Находка наряда Н-30.08-01, отчёт REPORT_skills-inventory_2026-08-30 (`1tK_h2G7v1gL1sktM3Xormgk41JPmxsJenaDk60EIiA0`).

Следующий шаг: сверить действующий снимок с каноном. Учесть, что снимок Skill внутри сессии не обновляется — расхождение, снятое в одной сессии, подтверждается только чтением из следующей.

Условие снятия: снимок перезалит (Save skill) и сверен с каноном.

Ссылки: REPORT_skills-inventory_2026-08-30 `1tK_h2G7v1gL1sktM3Xormgk41JPmxsJenaDk60EIiA0`; наряд Н-30.08-01; источник — Зона А SYS_INDEX, строка 132.
