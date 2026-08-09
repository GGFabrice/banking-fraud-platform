SELECT
    m.merchant_id,

    m.merchant_name,

    m.merchant_type,

    COUNT(f.transaction_id) AS total_transactions,

    SUM(f.is_fraud) AS total_frauds,

    ROUND(
        (
            SUM(f.is_fraud)::numeric
            / NULLIF(COUNT(f.transaction_id), 0)
        ) * 100,
        2
    ) AS fraud_rate_percentage,

    ROUND(
        SUM(f.amount),
        2
    ) AS total_amount,

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
    m.merchant_type

ORDER BY fraud_rate_percentage DESC;