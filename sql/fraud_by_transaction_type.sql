SELECT

    transaction_type,

    COUNT(*) AS total_transactions,

    SUM(is_fraud) AS total_frauds,

    ROUND(
        (SUM(is_fraud)::numeric / COUNT(*)) * 100,
        2
    ) AS fraud_rate_percentage,

    SUM(amount) AS total_amount

FROM fact_transactions

GROUP BY transaction_type

ORDER BY fraud_rate_percentage DESC;