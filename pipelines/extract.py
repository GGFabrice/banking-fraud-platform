from pathlib import Path
import pandas as pd


# Dossier source
INPUT_FOLDER = Path("data/cleansed")


def extract_data():

    print("=" * 50)
    print("Début extraction des données")
    print("=" * 50)


    customers = pd.read_csv(
        INPUT_FOLDER / "customers.csv"
    )

    accounts = pd.read_csv(
        INPUT_FOLDER / "accounts.csv"
    )

    devices = pd.read_csv(
        INPUT_FOLDER / "devices.csv"
    )

    merchants = pd.read_csv(
        INPUT_FOLDER / "merchants.csv"
    )

    transactions = pd.read_csv(
        INPUT_FOLDER / "transactions.csv"
    )


    print("Customers :", customers.shape)
    print("Accounts :", accounts.shape)
    print("Devices :", devices.shape)
    print("Merchants :", merchants.shape)
    print("Transactions :", transactions.shape)


    print("=" * 50)
    print("Extraction terminée")
    print("=" * 50)


    return (
        customers,
        accounts,
        devices,
        merchants,
        transactions
    )


if __name__ == "__main__":

    extract_data()