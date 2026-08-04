SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.risk_level,

    COUNT(f.transaction_id) AS total_transactions,

    SUM(
        CASE WHEN f.is_fraud = 1 
        THEN 1 ELSE 0 END
    ) AS fraud_count,

    ROUND(
        SUM(
            CASE WHEN f.is_fraud = 1 
            THEN f.amount ELSE 0 END
        ),
        2
    ) AS fraud_amount

FROM fact_transactions f

JOIN dim_customers c
ON f.customer_id = c.customer_id

GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.risk_level

ORDER BY fraud_amount DESC;