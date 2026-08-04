from pathlib import Path
import random
import pandas as pd
from faker import Faker

fake = Faker("fr_FR")

Faker.seed(42)
random.seed(42)

# ==========================
# PARAMÈTRES
# ==========================

NB_CUSTOMERS = 10000

OUTPUT_FOLDER = Path("data/raw")
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

ACCOUNT_TYPES = [
    "CHECKING",     # Compte courant
    "SAVINGS",      # Épargne
    "BUSINESS"      # Professionnel
]

STATUS = [
    "ACTIVE",
    "BLOCKED",
    "CLOSED"
]

accounts = []
account_id = 1

for customer_id in range(1, NB_CUSTOMERS + 1):

    # Chaque client possède entre 1 et 3 comptes
    nb_accounts = random.randint(1, 3)

    for _ in range(nb_accounts):

        accounts.append({
            "account_id": account_id,
            "customer_id": customer_id,
            "account_number": fake.bban(),
            "account_type": random.choices(
                ACCOUNT_TYPES,
                weights=[60, 30, 10],
                k=1
            )[0],
            "currency": "XOF",
            "balance": round(random.uniform(5000, 10000000), 2),
            "open_date": fake.date_between(
                start_date="-10y",
                end_date="today"
            ),
            "status": random.choices(
                STATUS,
                weights=[92, 5, 3],
                k=1
            )[0]
        })

        account_id += 1

df = pd.DataFrame(accounts)

output_file = OUTPUT_FOLDER / "accounts.csv"

df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("=" * 50)
print("Génération des comptes terminée")
print("=" * 50)
print(f"Nombre de comptes : {len(df)}")
print(f"Fichier créé : {output_file}")