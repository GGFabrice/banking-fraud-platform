from pathlib import Path
import pandas as pd


class CleaningPipeline:

    def __init__(self, input_folder: str, output_folder: str):
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)

    def run(self):

        # Création du dossier de sortie
        self.output_folder.mkdir(parents=True, exist_ok=True)

        # Parcours de tous les fichiers CSV
        for file in self.input_folder.glob("*.csv"):

            print("=" * 60)
            print(f"Nettoyage de : {file.name}")

            # Lecture
            df = pd.read_csv(file)

            print(f"Lignes avant nettoyage : {len(df)}")

            # Suppression des doublons
            df = df.drop_duplicates()

            # Suppression des lignes totalement vides
            df = df.dropna(how="all")

            # Nettoyage des colonnes texte
            for column in df.select_dtypes(include="object").columns:
                df[column] = (
                    df[column]
                    .astype(str)
                    .str.strip()
                )

            # Nettoyage spécifique aux transactions
            if "amount" in df.columns:
                df = df[df["amount"] >= 0]

            # Conversion des dates si présentes
            if "transaction_date" in df.columns:
                df["transaction_date"] = pd.to_datetime(
                    df["transaction_date"],
                    errors="coerce"
                )

            if "birth_date" in df.columns:
                df["birth_date"] = pd.to_datetime(
                    df["birth_date"],
                    errors="coerce"
                )

            print(f"Lignes après nettoyage : {len(df)}")

            # Sauvegarde
            output_file = self.output_folder / file.name

            df.to_csv(
                output_file,
                index=False,
                encoding="utf-8-sig"
            )

            print(f"Fichier sauvegardé : {output_file}")

        print("\nPipeline de nettoyage terminé avec succès.")