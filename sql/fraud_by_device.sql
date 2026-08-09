SELECT
    d.device_type,
    d.operating_system,
    d.browser,

    COUNT(f.transaction_id) AS total_transactions,

    SUM(f.is_fraud) AS total_frauds,

    ROUND(
        (
            SUM(f.is_fraud)::numeric
            / NULLIF(COUNT(f.transaction_id), 0)
        ) * 100,
        2
    ) AS fraud_rate_percentage

FROM fact_transactions f

JOIN dim_devices d
    ON f.device_id = d.device_id

GROUP BY
    d.device_type,
    d.operating_system,
    d.browser

ORDER BY fraud_rate_percentage DESC;