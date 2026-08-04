from pipelines.extract import extract_data
from pipelines.transformation import transform_data
from pipelines.loading import load_data


def run_pipeline():

    print("\n🚀 DÉMARRAGE DU PIPELINE BANKING FRAUD PLATFORM\n")


    # ==========================
    # EXTRACTION
    # ==========================

    (
        customers,
        accounts,
        devices,
        merchants,
        transactions
    ) = extract_data()


    # ==========================
    # TRANSFORMATION
    # ==========================

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


    # ==========================
    # CHARGEMENT
    # ==========================

    load_data(
        dim_customers,
        dim_accounts,
        dim_devices,
        dim_merchants,
        dim_date,
        fact_transactions
    )


    print("\n🎉 PIPELINE TERMINÉ AVEC SUCCÈS")


if __name__ == "__main__":

    run_pipeline()