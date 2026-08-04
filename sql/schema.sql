-- ===========================================
-- SUPPRESSION DES TABLES SI ELLES EXISTENT
-- ===========================================

DROP TABLE IF EXISTS fact_transactions CASCADE;

DROP TABLE IF EXISTS dim_customers CASCADE;

DROP TABLE IF EXISTS dim_accounts CASCADE;

DROP TABLE IF EXISTS dim_devices CASCADE;

DROP TABLE IF EXISTS dim_merchants CASCADE;

DROP TABLE IF EXISTS dim_date CASCADE;


-- ===========================================
-- DIM_CUSTOMERS
-- ===========================================

CREATE TABLE dim_customers (

    customer_id INT PRIMARY KEY,

    first_name VARCHAR(100),

    last_name VARCHAR(100),

    gender VARCHAR(5),

    birth_date DATE,

    email VARCHAR(255),

    phone VARCHAR(50),

    city VARCHAR(100),

    country VARCHAR(100),

    profession VARCHAR(100),

    risk_level VARCHAR(20)

);


-- ===========================================
-- DIM_ACCOUNTS
-- ===========================================

CREATE TABLE dim_accounts (

    account_id INT PRIMARY KEY,

    customer_id INT,

    account_number VARCHAR(50),

    account_type VARCHAR(50),

    currency VARCHAR(10),

    opening_date DATE,

    balance NUMERIC(18,2),

    status VARCHAR(30)

);


-- ===========================================
-- DIM_DEVICES
-- ===========================================

CREATE TABLE dim_devices (

    device_id INT PRIMARY KEY,

    customer_id INT,

    device_type VARCHAR(50),

    operating_system VARCHAR(50),

    browser VARCHAR(50),

    ip_address VARCHAR(100)

);


-- ===========================================
-- DIM_MERCHANTS
-- ===========================================

CREATE TABLE dim_merchants (

    merchant_id INT PRIMARY KEY,

    merchant_name VARCHAR(150),

    merchant_category VARCHAR(100),

    city VARCHAR(100),

    country VARCHAR(100)

);


-- ===========================================
-- DIM_DATE
-- ===========================================

CREATE TABLE dim_date (

    date_id SERIAL PRIMARY KEY,

    full_date DATE UNIQUE,

    day INT,

    month INT,

    year INT,

    quarter INT

);


-- ===========================================
-- FACT_TRANSACTIONS
-- ===========================================

CREATE TABLE fact_transactions (

    transaction_id INT PRIMARY KEY,

    customer_id INT,

    account_id INT,

    merchant_id INT,

    device_id INT,

    date_id INT,

    transaction_type VARCHAR(50),

    amount NUMERIC(18,2),

    location VARCHAR(100),

    is_fraud INT,

    fraud_reason VARCHAR(255),

    FOREIGN KEY (customer_id)
        REFERENCES dim_customers(customer_id),

    FOREIGN KEY (account_id)
        REFERENCES dim_accounts(account_id),

    FOREIGN KEY (merchant_id)
        REFERENCES dim_merchants(merchant_id),

    FOREIGN KEY (device_id)
        REFERENCES dim_devices(device_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)

);