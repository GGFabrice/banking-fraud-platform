SELECT
    location AS city,

    COUNT(*) AS total_transactions,

    SUM(is_fraud) AS total_frauds,

    ROUND(
        (SUM(is_fraud)::numeric / NULLIF(COUNT(*), 0)) * 100,
        2
    ) AS fraud_rate_percentage,

    SUM(
        CASE
            WHEN is_fraud = 1 THEN amount
            ELSE 0
        END
    ) AS fraud_amount

FROM fact_transactions

GROUP BY location

ORDER BY fraud_rate_percentage DESC;