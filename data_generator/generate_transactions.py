from pathlib import Path
import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta


# ==========================
# CONFIGURATION
# ==========================

fake = Faker("fr_FR")

Faker.seed(42)
random.seed(42)

NB_TRANSACTIONS = 100000


INPUT_FOLDER = Path("data/raw")
OUTPUT_FOLDER = Path("data/raw")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


# ==========================
# CHARGEMENT DES DONNEES
# ==========================

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


# ==========================
# LISTES
# ==========================

TRANSACTION_TYPES = [
    "PAYMENT",
    "TRANSFER",
    "WITHDRAWAL",
    "DEPOSIT"
]


LOCATIONS = [
    "Abidjan",
    "Bouake",
    "Yamoussoukro",
    "San Pedro",
    "Korhogo"
]


FRAUD_REASONS = [
    "Large amount",
    "Unknown device",
    "Unusual location",
    "Multiple transactions",
    "Suspicious merchant"
]


# ==========================
# GENERATION TRANSACTIONS
# ==========================

transactions = []


for transaction_id in range(1, NB_TRANSACTIONS + 1):

    # Sélection d'un compte bancaire
    account = accounts.sample(1).iloc[0]

    customer_id = account["customer_id"]


    # Sélection commerçant et appareil
    merchant = merchants.sample(1).iloc[0]

    device = devices.sample(1).iloc[0]


    # Montant transaction
    amount = round(
        random.uniform(500, 1000000),
        2
    )


    # Type transaction
    transaction_type = random.choice(
        TRANSACTION_TYPES
    )


    # ==========================
    # SIMULATION FRAUDE
    # ==========================

    is_fraud = random.choices(
        [0, 1],
        weights=[95, 5],
        k=1
    )[0]


    if is_fraud == 1:

        fraud_reason = random.choice(
            FRAUD_REASONS
        )

    else:

        fraud_reason = None



    # ==========================
    # CREATION TRANSACTION
    # ==========================

    transactions.append({

        "transaction_id": transaction_id,

        "customer_id": customer_id,

        "account_id": account["account_id"],

        "merchant_id": merchant["merchant_id"],

        "device_id": device["device_id"],


        "transaction_date": fake.date_time_between_dates(
            datetime_start=datetime.now() - timedelta(days=730),
            datetime_end=datetime.now()
        ),


        "transaction_type": transaction_type,

        "amount": amount,


        "location": random.choice(
            LOCATIONS
        ),


        "is_fraud": is_fraud,


        "fraud_reason": fraud_reason

    })



# ==========================
# SAUVEGARDE
# ==========================

df = pd.DataFrame(transactions)


output_file = OUTPUT_FOLDER / "transactions.csv"



df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)



print("=" * 50)
print(" Génération des transactions terminée ")
print("=" * 50)

print(f"Nombre de transactions : {len(df)}")

print(f"Fichier créé : {output_file}")