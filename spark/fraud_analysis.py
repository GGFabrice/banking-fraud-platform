from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, year, month


def main():

    # ==========================================
    # 1. Création de la session Spark
    # ==========================================

    spark = (
        SparkSession.builder
        .appName("BankingFraudAnalysis")
        .master("local[*]")
        .getOrCreate()
    )

    print("\n========================================")
    print("       BANKING FRAUD ANALYSIS")
    print("========================================\n")

    # ==========================================
    # 2. Lecture des données cleansed
    # ==========================================

    input_path = "data/cleansed/transactions.csv"

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(input_path)
    )

    print("=== SCHÉMA DES TRANSACTIONS ===")
    df.printSchema()

    print("\n=== APERÇU DES TRANSACTIONS ===")
    df.show(10, truncate=False)

    # ==========================================
    # 3. KPI globaux
    # ==========================================

    total_transactions = df.count()

    total_frauds = (
        df
        .filter(col("is_fraud") == 1)
        .count()
    )

    fraud_amount = (
        df
        .filter(col("is_fraud") == 1)
        .agg(sum("amount").alias("fraud_amount"))
        .collect()[0]["fraud_amount"]
    )

    fraud_rate = (
        total_frauds / total_transactions * 100
        if total_transactions > 0
        else 0
    )

    print("\n=== KPI GLOBAUX ===")
    print(f"Nombre total de transactions : {total_transactions}")
    print(f"Nombre total de fraudes : {total_frauds}")
    print(f"Montant total des fraudes : {fraud_amount:.2f}")
    print(f"Taux de fraude : {fraud_rate:.2f}%")

    # ==========================================
    # 4. Fraudes par type
    # ==========================================

    fraud_by_type = (
        df
        .filter(col("is_fraud") == 1)
        .groupBy("transaction_type")
        .agg(
            count("*").alias("total_frauds"),
            sum("amount").alias("fraud_amount")
        )
        .orderBy(col("total_frauds").desc())
    )

    print("\n=== FRAUDES PAR TYPE ===")
    fraud_by_type.show(truncate=False)

    # ==========================================
    # 5. Fraudes par localisation
    # ==========================================

    fraud_by_location = (
        df
        .filter(col("is_fraud") == 1)
        .groupBy("location")
        .agg(
            count("*").alias("total_frauds"),
            sum("amount").alias("fraud_amount")
        )
        .orderBy(col("total_frauds").desc())
    )

    print("\n=== FRAUDES PAR LOCALISATION ===")
    fraud_by_location.show(truncate=False)

    # ==========================================
    # 6. Fraudes par raison
    # ==========================================

    fraud_by_reason = (
        df
        .filter(col("is_fraud") == 1)
        .groupBy("fraud_reason")
        .agg(
            count("*").alias("total_frauds"),
            sum("amount").alias("fraud_amount")
        )
        .orderBy(col("total_frauds").desc())
    )

    print("\n=== FRAUDES PAR RAISON ===")
    fraud_by_reason.show(truncate=False)

    # ==========================================
    # 7. Évolution mensuelle
    # ==========================================

    fraud_by_month = (
        df
        .filter(col("is_fraud") == 1)
        .withColumn("year", year("transaction_date"))
        .withColumn("month", month("transaction_date"))
        .groupBy("year", "month")
        .agg(
            count("*").alias("total_frauds"),
            sum("amount").alias("fraud_amount")
        )
        .orderBy("year", "month")
    )

    print("\n=== ÉVOLUTION MENSUELLE ===")
    fraud_by_month.show(100, truncate=False)

    # ==========================================
    # 8. Création du dossier curated
    # ==========================================

    curated_path = "data/curated"

    # ==========================================
    # 9. Sauvegarde des KPI
    # ==========================================

    fraud_kpis = spark.createDataFrame(
        [
            (
                total_transactions,
                total_frauds,
                float(fraud_amount),
                float(fraud_rate)
            )
        ],
        [
            "total_transactions",
            "total_frauds",
            "fraud_amount",
            "fraud_rate_percentage"
        ]
    )

    fraud_kpis.write.mode("overwrite").option(
        "header", True
    ).csv(f"{curated_path}/fraud_kpis")

    # ==========================================
    # 10. Sauvegarde par type
    # ==========================================

    fraud_by_type.write.mode("overwrite").option(
        "header", True
    ).csv(f"{curated_path}/fraud_by_type")

    # ==========================================
    # 11. Sauvegarde par localisation
    # ==========================================

    fraud_by_location.write.mode("overwrite").option(
        "header", True
    ).csv(f"{curated_path}/fraud_by_location")

    # ==========================================
    # 12. Sauvegarde par raison
    # ==========================================

    fraud_by_reason.write.mode("overwrite").option(
        "header", True
    ).csv(f"{curated_path}/fraud_by_reason")

    # ==========================================
    # 13. Sauvegarde mensuelle
    # ==========================================

    fraud_by_month.write.mode("overwrite").option(
        "header", True
    ).csv(f"{curated_path}/fraud_by_month")

    print("\n========================================")
    print("      DONNÉES CURATED CRÉÉES")
    print("========================================")

    print(f"\nDossier : {curated_path}")

    # ==========================================
    # 14. Arrêt Spark
    # ==========================================

    spark.stop()

    print("\n=== SPARK ARRÊTÉ ===")


if __name__ == "__main__":
    main()