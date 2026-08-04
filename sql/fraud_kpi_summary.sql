SELECT
    COUNT(*) AS total_transactions,

    SUM(amount) AS total_amount,

    SUM(is_fraud) AS total_frauds,

    ROUND(
        (SUM(is_fraud)::numeric / COUNT(*)) * 100,
        2
    ) AS fraud_rate_percentage,

    SUM(
        CASE 
            WHEN is_fraud = 1 THEN amount
            ELSE 0
        END
    ) AS fraud_amount,

    ROUND(
        AVG(
            CASE 
                WHEN is_fraud = 1 THEN amount
            END
        ),
        2
    ) AS average_fraud_amount

FROM fact_transactions;