from pathlib import Path
import random
import pandas as pd
from faker import Faker

# Initialisation de Faker en français
fake = Faker("fr_FR")

# Pour obtenir toujours les mêmes données à chaque exécution
Faker.seed(42)
random.seed(42)

# Nombre de clients à générer
NB_CUSTOMERS = 10000

# Dossier de sortie
OUTPUT_FOLDER = Path("data/raw")
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Listes de valeurs
PROFESSIONS = [
    "Ingénieur",
    "Enseignant",
    "Médecin",
    "Commerçant",
    "Étudiant",
    "Comptable",
    "Banquier",
    "Informaticien",
    "Avocat",
    "Entrepreneur"
]

RISK_LEVELS = [
    "LOW",
    "MEDIUM",
    "HIGH"
]

customers = []

for customer_id in range(1, NB_CUSTOMERS + 1):

    gender = random.choice(["M", "F"])

    if gender == "M":
        first_name = fake.first_name_male()
    else:
        first_name = fake.first_name_female()

    last_name = fake.last_name()

    customers.append({
        "customer_id": customer_id,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "birth_date": fake.date_of_birth(
            minimum_age=18,
            maximum_age=80
        ),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "city": fake.city(),
        "country": "Côte d'Ivoire",
        "profession": random.choice(PROFESSIONS),
        "risk_level": random.choices(
            RISK_LEVELS,
            weights=[70, 25, 5],
            k=1
        )[0]
    })

df = pd.DataFrame(customers)

output_file = OUTPUT_FOLDER / "customers.csv"

df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("=" * 50)
print(" Génération des clients terminée")
print("=" * 50)
print(f"Nombre de clients : {len(df)}")
print(f"Fichier créé : {output_file}")