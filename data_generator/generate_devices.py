from pathlib import Path
import random
import pandas as pd
from faker import Faker

fake = Faker("fr_FR")

Faker.seed(42)
random.seed(42)

NB_CUSTOMERS = 10000

OUTPUT_FOLDER = Path("data/raw")
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

DEVICE_TYPES = [
    "MOBILE",
    "LAPTOP",
    "TABLET",
    "DESKTOP"
]

OS = [
    "Android",
    "iOS",
    "Windows",
    "macOS"
]

BROWSERS = [
    "Chrome",
    "Edge",
    "Firefox",
    "Safari"
]

devices = []

device_id = 1

for customer_id in range(1, NB_CUSTOMERS + 1):

    # chaque client possède entre 1 et 3 appareils
    nb_devices = random.randint(1, 3)

    for _ in range(nb_devices):

        devices.append({

            "device_id": device_id,

            "customer_id": customer_id,

            "device_type": random.choice(DEVICE_TYPES),

            "operating_system": random.choice(OS),

            "browser": random.choice(BROWSERS),

            "ip_address": fake.ipv4(),

            "country": "Côte d'Ivoire",

            "trusted_device": random.choices(
                ["YES", "NO"],
                weights=[90, 10],
                k=1
            )[0],

            "first_seen": fake.date_between(
                start_date="-5y",
                end_date="-30d"
            ),

            "last_seen": fake.date_between(
                start_date="-30d",
                end_date="today"
            )

        })

        device_id += 1

df = pd.DataFrame(devices)

output_file = OUTPUT_FOLDER / "devices.csv"

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("=" * 50)
print("Génération des appareils terminée")
print("=" * 50)
print(f"Nombre d'appareils : {len(df)}")
print(f"Fichier créé : {output_file}")