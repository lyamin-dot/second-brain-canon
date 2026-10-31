projects/marketplace-rebuild/DATA_MODEL.en.md

# Pilot data model — agent digest (additional file role of marketplace-rebuild)

Moved from `PLAN.en.md` section 13 on 2026-10-31 by script, text unchanged; role declared in `PLAN.md` section 10; decision — LOG Р-36. Full Russian text: `DATA_MODEL.md`.

## 13 Pilot data model (accepted by separate reviewer, round 2, 2026-10-25; LOG Р-14). Full Russian text = DATA_MODEL.md (was PLAN.md §13 until 2026-10-31); this is the agent digest.
DB mkt2 (PostgreSQL 16 on server), roles mkt2_writer (owner) / mkt2_reader (read-only), schemas ref + raw.
ref: legal_entity; cabinet (4 rows, collection on only ip_ozon, ip_wb); cabinet_api (PK cabinet+api_scope+purpose; api_proxy_workflow_id; NO credential IDs/rights — binding lives in proxy node, rights/expiry in key book N8N_CREDENTIALS); article = full-rebuild mirror of Price Master!Artikel A,F,G,H only (not brand AA, not status N — both derived from Кипарис cards); v_article_item = view article↔MP item from newest raw cards, first word of vendorCode/offer_id; is_live only from runs status ok.
raw: common cols cabinet_code, source_method, payload jsonb (one response element whole), payload_hash, load_run_id, first/last_loaded_at. Modes: versions (PK cabinet+natural_key+payload_hash; current = max last_loaded_at); day snapshot (PK cabinet+snapshot_date+natural_key; delete+insert one transaction only on ok run). raw.load_run = one row per run (exec number = proof).
Tables WB ИП: wb_sale, wb_order (stats; key category Статистика missing), wb_finance_row (raw_key as Кипарис wb_raw_report_V2), wb_finance_report (report_id), wb_stock_seller, wb_stock_wb, wb_card (nmID; key exists), wb_price (nmID; category «Цены и скидки» hypothesis — not in Andrei key list). Ozon ИП: ozon_posting_fbs/_fbo, ozon_accrual (raw_key as Кипарис ozon_raw_accrual_TEST), ozon_accrual_type, ozon_stock_product, ozon_stock_analytics, ozon_product, ozon_product_attr, ozon_price. Do not use WB supplier/stocks, supplier/incomes, v5 reportDetailByPeriod. Ozon total→total_items 23.11.2026: paginate by last_id.
Which table answers: ops (orders/sales/returns daily) = wb_order/wb_sale, ozon_posting; money and accounted sales/returns = wb_finance_row, ozon_accrual; listed price = *_price; actual sale price = finance/accrual payload; never reconcile ops vs money as truth vs truth.
Purchase price home = book «Закупка» 1GZSACQW… (wb-ue Р-73), out of DB in pilot; robot 2UsyP3q5Jd9OafJD manual-only.
Open for Andrei (pilot runs without): article brand + Lopal article list (options: brand reference by hand [rec.] / «Закупка» brand col / defer). ИП target price: no home, out of pilot.
Old homes to disable at switch-over (after reconciliation + yes, never delete): 2 cost_price_history sheets, Ozon_IP_SKU_Staging + PWFVE0UbM3ajvVFc (workflow archived 26.10, Р-21), WB_Cards_Staging_IP + vIteQxGrqI7kLkb0, Artikel!N, Artikel!AA, MASTER_MAP.
Builder notes: snapshot date = run start Moscow; «Закупка» key uniqueness unverified; Ozon warehouse stock truth rule (stock_product vs analytics) to set from first response; natural keys marked hypothesis must be fixed in contract row before load.
Builder deviations accepted (LOG Р-18): collector = thin scheduled wrapper `MKT2 Collect <method>` + shared `MKT2 Collect Engine` pd2K2KtImWlFfueW; WB stock element = one size on one warehouse, key nmId_chrtId_warehouseId; called sub-workflows (engine, proxies) must be published; load window from 2026-10-01 (history depth = Andrei question).

