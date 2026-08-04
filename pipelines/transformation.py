import pandas as pd


def transform_data(
    customers,
    accounts,
    devices,
    merchants,
    transactions
):

    print("=" * 50)
    print("Début transformation")
    print("=" * 50)


    # Dimensions

    dim_customers = customers.copy()

    dim_accounts = accounts.copy()

    dim_devices = devices.copy()

    dim_merchants = merchants.copy()


    # ==========================
    # DIM DATE
    # ==========================

    transactions["transaction_date"] = pd.to_datetime(
        transactions["transaction_date"]
    )


    dim_date = pd.DataFrame()

    dim_date["full_date"] = (
        transactions["transaction_date"]
        .dt.date
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
    )


    dim_date["day"] = pd.to_datetime(
        dim_date["full_date"]
    ).dt.day

    dim_date["month"] = pd.to_datetime(
        dim_date["full_date"]
    ).dt.month

    dim_date["year"] = pd.to_datetime(
        dim_date["full_date"]
    ).dt.year

    dim_date["quarter"] = pd.to_datetime(
        dim_date["full_date"]
    ).dt.quarter


    dim_date.insert(
        0,
        "date_id",
        range(1, len(dim_date)+1)
    )


    # ==========================
    # FACT TRANSACTIONS
    # ==========================

    fact_transactions = transactions.copy()


    fact_transactions["transaction_day"] = (
        fact_transactions["transaction_date"]
        .dt.date
    )


    fact_transactions = fact_transactions.merge(
        dim_date,
        left_on="transaction_day",
        right_on="full_date",
        how="left"
    )


    fact_transactions.drop(
        columns=[
            "transaction_day",
            "full_date"
        ],
        inplace=True
    )


    print("dim_customers :", dim_customers.shape)
    print("dim_accounts :", dim_accounts.shape)
    print("dim_devices :", dim_devices.shape)
    print("dim_merchants :", dim_merchants.shape)
    print("dim_date :", dim_date.shape)
    print("fact_transactions :", fact_transactions.shape)


    print("=" * 50)
    print("Transformation terminée")
    print("=" * 50)


    return (
        dim_customers,
        dim_accounts,
        dim_devices,
        dim_merchants,
        dim_date,
        fact_transactions
    )