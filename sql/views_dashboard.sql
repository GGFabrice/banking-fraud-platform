-- =========================================================
-- VUES DASHBOARD - BANKING FRAUD PLATFORM
-- =========================================================

-- =========================================================
-- 1. KPI FRAUDE GLOBAL
-- =========================================================

CREATE OR REPLACE VIEW vw_fraud_global AS
SELECT
    COUNT(*) AS total_transactions,

    SUM(
        CASE
            WHEN is_fraud = 1 THEN 1
            ELSE 0
        END
    ) AS total_fraud,

    ROUND(
        SUM(
            CASE
                WHEN is_fraud = 1 THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS fraud_rate,

    ROUND(
        SUM(
            CASE
                WHEN is_fraud = 1 THEN amount
                ELSE 0
            END
        ),
        2
    ) AS fraud_amount,

    ROUND(AVG(amount), 2) AS average_transaction_amount

FROM fact_transactions;


-- =========================================================
-- 2. FRAUDE PAR DATE
-- =========================================================

CREATE OR REPLACE VIEW vw_fraud_by_date AS
SELECT
    d.full_date,
    d.day,
    d.month,
    d.year,
    d.quarter,

    COUNT(f.transaction_id) AS total_transactions,

    SUM(f.is_fraud) AS total_frauds,

    ROUND(
        SUM(f.is_fraud)::numeric
        / COUNT(f.transaction_id) * 100,
        2
    ) AS fraud_rate_percentage,

    ROUND(
        SUM(
            CASE
                WHEN f.is_fraud = 1 THEN f.amount
                ELSE 0
            END
        ),
        2
    ) AS fraud_amount

FROM fact_transactions f

JOIN dim_date d
    ON f.date_id = d.date_id

GROUP BY
    d.full_date,
    d.day,
    d.month,
    d.year,
    d.quarter;


-- =========================================================
-- 3. FRAUDE PAR LOCALISATION
-- =========================================================

CREATE OR REPLACE VIEW vw_fraud_by_location AS
SELECT
    location,

    COUNT(*) AS total_transactions,

    SUM(is_fraud) AS total_frauds,

    ROUND(
        SUM(is_fraud)::numeric
        / COUNT(*) * 100,
        2
    ) AS fraud_rate_percentage,

    ROUND(
        SUM(
            CASE
                WHEN is_fraud = 1 THEN amount
                ELSE 0
            END
        ),
        2
    ) AS fraud_amount

FROM fact_transactions

GROUP BY location;


-- =========================================================
-- 4. FRAUDE PAR TYPE DE TRANSACTION
-- =========================================================

CREATE OR REPLACE VIEW vw_fraud_by_transaction_type AS
SELECT
    transaction_type,

    COUNT(*) AS total_transactions,

    SUM(is_fraud) AS total_frauds,

    ROUND(
        SUM(is_fraud)::numeric
        / COUNT(*) * 100,
        2
    ) AS fraud_rate_percentage,

    ROUND(SUM(amount), 2) AS total_amount,

    ROUND(
        SUM(
            CASE
                WHEN is_fraud = 1 THEN amount
                ELSE 0
            END
        ),
        2
    ) AS fraud_amount

FROM fact_transactions

GROUP BY transaction_type;


-- =========================================================
-- 5. FRAUDE PAR DEVICE
-- =========================================================

CREATE OR REPLACE VIEW vw_fraud_by_device AS
SELECT
    d.device_type,
    d.operating_system,
    d.browser,

    COUNT(f.transaction_id) AS total_transactions,

    SUM(f.is_fraud) AS total_frauds,

    ROUND(
        SUM(f.is_fraud)::numeric
        / COUNT(f.transaction_id) * 100,
        2
    ) AS fraud_rate_percentage,

    ROUND(
        SUM(
            CASE
                WHEN f.is_fraud = 1 THEN f.amount
                ELSE 0
            END
        ),
        2
    ) AS fraud_amount

FROM fact_transactions f

JOIN dim_devices d
    ON f.device_id = d.device_id

GROUP BY
    d.device_type,
    d.operating_system,
    d.browser;


-- =========================================================
-- 6. FRAUDE PAR MARCHAND
-- =========================================================

CREATE OR REPLACE VIEW vw_fraud_by_merchant AS
SELECT
    m.merchant_id,
    m.merchant_name,
    m.merchant_type,

    COUNT(f.transaction_id) AS total_transactions,

    SUM(f.is_fraud) AS total_frauds,

    ROUND(
        SUM(f.is_fraud)::numeric
        / COUNT(f.transaction_id) * 100,
        2
    ) AS fraud_rate_percentage,

    ROUND(SUM(f.amount), 2) AS total_amount,

    ROUND(
        SUM(
            CASE
                WHEN f.is_fraud = 1 THEN f.amount
                ELSE 0
            END
        ),
        2
    ) AS fraud_amount

FROM fact_transactions f

JOIN dim_merchants m
    ON f.merchant_id = m.merchant_id

GROUP BY
    m.merchant_id,
    m.merchant_name,
    m.merchant_type;