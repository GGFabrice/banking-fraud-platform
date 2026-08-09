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
        ) * 100.0 / NULLIF(COUNT(*), 0),
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

    ROUND(
        AVG(amount),
        2
    ) AS average_transaction_amount

FROM fact_transactions;