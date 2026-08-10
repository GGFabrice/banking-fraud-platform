from sqlalchemy import text
from database.connection import engine


def load_data(
    dim_customers,
    dim_accounts,
    dim_devices,
    dim_merchants,
    dim_date,
    fact_transactions
):

    print("=" * 50)
    print("Début chargement Data Warehouse")
    print("=" * 50)

    # Vider les tables avant le chargement
    print("🗑️ Suppression des anciennes données...")

    with engine.begin() as conn:
        conn.execute(text("""
            TRUNCATE TABLE
                fact_transactions,
                dim_date,
                dim_devices,
                dim_merchants,
                dim_accounts,
                dim_customers
            RESTART IDENTITY CASCADE;
        """))

    print("✅ Tables vidées")

    # Chargement de la dimension clients
    dim_customers.to_sql(
        "dim_customers",
        engine,
        if_exists="append",
        index=False
    )
    print("✅ dim_customers chargée")

    # Chargement de la dimension comptes
    dim_accounts.to_sql(
        "dim_accounts",
        engine,
        if_exists="append",
        index=False
    )
    print("✅ dim_accounts chargée")

    # Chargement de la dimension appareils
    dim_devices.to_sql(
        "dim_devices",
        engine,
        if_exists="append",
        index=False
    )
    print("✅ dim_devices chargée")

    # Chargement de la dimension commerçants
    dim_merchants.to_sql(
        "dim_merchants",
        engine,
        if_exists="append",
        index=False
    )
    print("✅ dim_merchants chargée")

    # Chargement de la dimension dates
    dim_date.to_sql(
        "dim_date",
        engine,
        if_exists="append",
        index=False
    )
    print("✅ dim_date chargée")

    # Chargement de la table de faits
    fact_transactions.to_sql(
        "fact_transactions",
        engine,
        if_exists="append",
        index=False
    )
    print("✅ fact_transactions chargée")

    print("=" * 50)
    print("🎉 Chargement terminé avec succès")
    print("=" * 50)