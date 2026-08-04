SELECT
    location,
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN is_fraud = 1 THEN 1 ELSE 0 END) AS fraud_count,
    ROUND(
        SUM(CASE WHEN is_fraud = 1 THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS fraud_rate,
    ROUND(
        SUM(CASE WHEN is_fraud = 1 THEN amount ELSE 0 END),
        2
    ) AS fraud_amount
FROM fact_transactions
GROUP BY location
ORDER BY fraud_count DESC;