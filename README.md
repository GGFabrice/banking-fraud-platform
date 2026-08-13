# 🏦 Banking Fraud Platform

## 📌 Description

Banking Fraud Platform est une plateforme Data Engineering dédiée à l'analyse des transactions bancaires et à l'identification des transactions frauduleuses.

Le projet met en place un pipeline complet permettant de :

- collecter les données de transactions ;
- nettoyer et préparer les données ;
- analyser les transactions avec PySpark ;
- produire des données agrégées ;
- stocker les données dans un Data Warehouse PostgreSQL ;
- exposer des indicateurs via des vues SQL ;
- visualiser les résultats dans Power BI.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │   Données sources   │
                    │       CSV           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      PySpark        │
                    │ Data Processing     │
                    │ & Fraud Analysis    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Data Cleansed     │
                    │   & Data Curated    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     PostgreSQL      │
                    │    banking_dw       │
                    │   Data Warehouse    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      SQL Views      │
                    │ Fraud Analytics     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Power BI       │
                    │ Fraud Dashboard     │
                    └─────────────────────┘

                    🛠️ Technologies utilisées
Technologie	Utilisation
Python	Développement et traitement des données
PySpark 4.2.0	Traitement distribué et analyse des données
Hadoop 3.5.0	Composants Hadoop utilisés par Spark
PostgreSQL	Data Warehouse
SQL	Transformation et analyse
Power BI	Dashboard et visualisation
Docker	Conteneurisation
WSL2 / Ubuntu 22.04	Environnement d'exécution Spark

📂 Structure du projet

banking-fraud-platform/
│
├── data/
│   ├── cleansed/
│   └── curated/
│
├── spark/
│   └── fraud_analysis.py
│
├── sql/
│   └── ...
│
├── database/
│   └── ...
│
├── dashboards/
│   └── banking_fraud_dashboard.pbix
│
├── pipelines/
│   └── ...
│
├── tests/
│   └── ...
│
├── docs/
│   └── ...
│
├── config/
│   └── ...
│
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .gitignore
└── README.md

📊 Données

Le dataset contient :

100 000 transactions
plusieurs clients
plusieurs comptes bancaires
plusieurs commerçants
plusieurs appareils
différents types de transactions
différentes localisations
différentes raisons de fraude

Les données couvrent une période allant de juillet 2024 à juillet 2026.

🔎 Analyse des fraudes

Le pipeline PySpark permet notamment d'analyser :

Fraudes par type de transaction
DEPOSIT
WITHDRAWAL
TRANSFER
PAYMENT
Fraudes par localisation
Korhogo
Abidjan
Bouake
Yamoussoukro
San Pedro
Fraudes par raison
Unusual location
Multiple transactions
Large amount
Suspicious merchant
Unknown device
Évolution temporelle

Les fraudes sont également agrégées par mois afin d'identifier les périodes présentant les niveaux de fraude les plus élevés.

📈 Résultats principaux
Indicateur	Résultat
Transactions analysées	100 000
Transactions frauduleuses	4 910
Taux de fraude	4,91 %
Montant total frauduleux	2 472 794 415,31 FCFA
Principales observations

Localisation avec le plus de fraudes :

Korhogo — 1 060 fraudes

Principale raison de fraude :

Unusual location — 1 012 fraudes

Type de transaction avec le plus de fraudes :

DEPOSIT — 1 271 fraudes

🗄️ Data Warehouse

Le Data Warehouse PostgreSQL utilise la base :
banking_dw

Les principales tables sont :
dim_accounts
dim_customers
dim_date
dim_devices
dim_merchants
fact_transactions

La table de faits contient :
100 000 transactions

👁️ Vues SQL

Le projet utilise des vues analytiques permettant notamment de suivre :
vw_fraud_global
vw_fraud_by_date
vw_fraud_by_device
vw_fraud_by_location
vw_fraud_by_merchant
vw_fraud_by_transaction_type

Ces vues servent de source aux analyses et au dashboard Power BI

📊 Power BI Dashboard

Le dashboard permet de suivre les principaux indicateurs de fraude :

nombre total de transactions ;
nombre total de fraudes ;
taux de fraude ;
montant total des fraudes ;
évolution mensuelle ;
fraudes par type ;
fraudes par localisation ;
fraudes par raison.

Le fichier Power BI est disponible dans :
dashboards/banking_fraud_dashboard.pbix

🚀 Installation
1. Cloner le projet

git clone git@github.com:GGFabrice/banking-fraud-platform.git
cd banking-fraud-platform

2. Créer l'environnement Python

Sous Linux / WSL :
python3 -m venv .venv-linux
source .venv-linux/bin/activate

3. Installer les dépendances
pip install -r requirements.txt

4. Lancer l'analyse PySpark
python spark/fraud_analysis.py

🧪 Vérification

Pour vérifier le fonctionnement de PySpark :
python -c "from pyspark.sql import SparkSession; s=SparkSession.builder.master('local[1]').getOrCreate(); print(s.version); s.stop()"

🔄 Pipeline de traitement

Source CSV
    ↓
Data Cleansing
    ↓
PySpark
    ↓
Fraud Analysis
    ↓
Data Curated
    ↓
PostgreSQL Data Warehouse
    ↓
SQL Analytics
    ↓
Power BI

🎯 Objectifs du projet

Ce projet a été conçu pour mettre en pratique plusieurs compétences Data Engineering :

Data ingestion
Data cleansing
Data transformation
Big Data processing
PySpark
Data Warehouse
SQL analytics
ETL / ELT
Data visualization
Business Intelligence
Git / GitHub
Docker
Linux / WSL

🔮 Perspectives d'amélioration

Les évolutions possibles comprennent :

intégration de Kafka pour le streaming ;
détection de fraude en temps réel ;
ajout d'un modèle Machine Learning ;
orchestration avec Apache Airflow ;
déploiement cloud sur AWS ;
ajout d'un système d'alertes ;
automatisation complète du pipeline ETL.
👤 Auteur

Fabrice Gnabo

Data Engineering / Data Analytics

GitHub :
https://github.com/GGFabrice

📜 Licence

Projet réalisé dans un objectif de démonstration et de portfolio Data Engineering.

