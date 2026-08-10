from pipelines.extract import extract_data
from pipelines.transformation import transform_data


(
    customers,
    accounts,
    devices,
    merchants,
    transactions
) = extract_data()


(
    dim_customers,
    dim_accounts,
    dim_devices,
    dim_merchants,
    dim_date,
    fact_transactions
) = transform_data(
    customers,
    accounts,
    devices,
    merchants,
    transactions
)


print("\nTest transformation OK")