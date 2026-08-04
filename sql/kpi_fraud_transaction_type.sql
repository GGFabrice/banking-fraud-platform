CREATE OR REPLACE VIEW vw_fraud_by_transaction_type AS

SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount,
    SUM(is_fraud) AS fraud_transactions,
    SUM(
        CASE 
            WHEN is_fraud = 1 THEN amount 
            ELSE 0 
        END
    ) AS fraud_amount,
    ROUND(
        (SUM(is_fraud)::numeric / COUNT(*)) * 100,
        2
    ) AS fraud_rate_percent

FROM fact_transactions

GROUP BY transaction_type;