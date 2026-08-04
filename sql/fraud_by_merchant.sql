SELECT

    m.merchant_id,

    m.merchant_name,

    m.merchant_type,

    COUNT(f.transaction_id) AS total_transactions,

    SUM(f.is_fraud) AS total_frauds,

    ROUND(
        (SUM(f.is_fraud)::numeric 
        / COUNT(f.transaction_id)) * 100,
        2
    ) AS fraud_rate_percentage,

    SUM(f.amount) AS total_amount


FROM fact_transactions f

JOIN dim_merchants m
ON f.merchant_id = m.merchant_id


GROUP BY
    m.merchant_id,
    m.merchant_name,
    m.merchant_type


ORDER BY fraud_rate_percentage DESC;