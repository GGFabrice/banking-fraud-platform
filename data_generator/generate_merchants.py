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

NB_MERCHANTS = 5000


OUTPUT_FOLDER = Path("data/raw")
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


# ==========================
# LISTES DE VALEURS
# ==========================

MERCHANT_TYPES = [
    "SUPERMARKET",
    "RESTAURANT",
    "PHARMACY",
    "FUEL_STATION",
    "E_COMMERCE",
    "HOTEL",
    "TRANSPORT",
    "TELECOM",
    "ELECTRONICS",
    "CLOTHING"
]


RISK_LEVELS = [
    "LOW",
    "MEDIUM",
    "HIGH"
]


CITIES = [
    "Abidjan",
    "Bouake",
    "Yamoussoukro",
    "San Pedro",
    "Korhogo",
    "Man",
    "Daloa"
]


# ==========================
# GENERATION
# ==========================

merchants = []


for merchant_id in range(1, NB_MERCHANTS + 1):

    merchants.append({

        "merchant_id": merchant_id,

        "merchant_name": fake.company(),

        "merchant_type": random.choice(
            MERCHANT_TYPES
        ),

        "city": random.choice(
            CITIES
        ),

        "country": "Côte d'Ivoire",

        "registration_date": fake.date_between(
            start_date="-15y",
            end_date="today"
        ),

        "risk_level": random.choices(
            RISK_LEVELS,
            weights=[70,25,5],
            k=1
        )[0]

    })


# ==========================
# EXPORT CSV
# ==========================

df = pd.DataFrame(merchants)


output_file = OUTPUT_FOLDER / "merchants.csv"


df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)


print("=" * 50)
print("Génération des commerçants terminée")
print("=" * 50)
print(f"Nombre de commerçants : {len(df)}")
print(f"Fichier créé : {output_file}")