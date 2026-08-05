# 🏦 Banking Fraud Platform - Data Engineering Project

## 📌 Description du projet

**Banking Fraud Platform** est une plateforme Data Engineering permettant de collecter, transformer, stocker et analyser des données de transactions bancaires afin d'identifier les comportements frauduleux.

Ce projet simule un environnement bancaire réel avec :

- des clients,
- des comptes bancaires,
- des terminaux utilisés,
- des commerçants,
- des transactions financières.

L'objectif principal est de construire une chaîne complète de traitement de données (**ETL Pipeline**) permettant d'alimenter un **Data Warehouse analytique** utilisé pour le suivi des indicateurs de fraude.

---

# 🎯 Objectifs du projet

Les objectifs principaux sont :

✅ Construire un pipeline ETL complet avec Python

✅ Nettoyer et transformer des données bancaires brutes

✅ Concevoir un Data Warehouse dimensionnel

✅ Implémenter un modèle en étoile (Star Schema)

✅ Charger les données dans PostgreSQL

✅ Produire des KPIs de fraude bancaire

✅ Préparer les données pour une future détection automatique de fraude avec Machine Learning

---

# 🏗️ Architecture Data Platform

             Sources de données
                   |
                   |
          CSV / Synthetic Data
                   |
                   |
            Extraction (Python)
                   |
                   |
          Transformation (Pandas)
                   |
                   |
            Data Warehouse
            PostgreSQL
                   |
    --------------------------------
    |              |               |
    Dimensions Fact Table KPIs
                   |
                   |
           Analyse & Reporting

    
---

# 🔄 Pipeline ETL

## 1. Extraction

Les données sources comprennent :

- Customers
- Accounts
- Devices
- Merchants
- Transactions


Volumes traités :

| Dataset | Nombre de lignes |
|---|---:|
| Customers | 10 000 |
| Accounts | 20 111 |
| Devices | 19 925 |
| Merchants | 5 000 |
| Transactions | 100 000 |


---

## 2. Transformation

Les opérations réalisées :

- nettoyage des données,
- gestion des types,
- création des dimensions analytiques,
- enrichissement des transactions,
- création d'une dimension temps.


Tables générées :
dim_customers
dim_accounts
dim_devices
dim_merchants
dim_date
fact_transactions



---

## 3. Chargement

Les données transformées sont chargées dans PostgreSQL avec SQLAlchemy et Pandas.


Processus :

TRUNCATE tables
      |
      |
Chargement dimensions
      |
      |
Chargement table de faits


---

# 🗄️ Modèle Data Warehouse

Le projet utilise un modèle en étoile (**Star Schema**).


## Tables Dimensions


### dim_customers

Informations clients :

- customer_id
- nom
- âge
- sexe
- ville
- pays


### dim_accounts

Informations comptes :

- account_id
- type de compte
- solde
- statut


### dim_devices

Informations appareils :

- device_id
- type appareil
- système exploitation
- navigateur


### dim_merchants

Informations commerçants :

- merchant_id
- catégorie
- localisation
- niveau de risque


### dim_date

Dimension temporelle :

- date
- jour
- mois
- année
- trimestre


---

## Table de faits


### fact_transactions


Contient les événements financiers :

- transaction_id
- customer_id
- account_id
- merchant_id
- device_id
- transaction_type
- amount
- location
- is_fraud
- fraud_reason


---

# 📊 Résultats obtenus

## Volume chargé

| Indicateur | Valeur |
|-|-:|
| Transactions analysées | 100 000 |
| Montant total traité | 49,9 milliards |
| Transactions frauduleuses | 4 910 |
| Taux de fraude | 4,91 % |
| Montant frauduleux | 2,47 milliards |


---

# 📈 KPIs développés

## Analyse globale fraude

- Nombre total transactions
- Montant total transactions
- Nombre transactions frauduleuses
- Montant fraude
- Taux de fraude


## Analyse par type de transaction

Exemple :

| Type | Fraude |
|-|-:|
| Deposit | 5,09 % |
| Withdrawal | 4,93 % |
| Transfer | 4,87 % |
| Payment | 4,75 % |


## Analyse géographique

Analyse fraude par ville :

- Abidjan
- Bouaké
- Korhogo
- Man
- Yamoussoukro


## Analyse comportementale

Analyse selon :

- type appareil,
- système d'exploitation,
- navigateur.


---

# 🛠️ Technologies utilisées


## Langages

- Python 3.13
- SQL


## Data Engineering

- Pandas
- SQLAlchemy
- PostgreSQL


## Data Warehouse

- PostgreSQL
- Star Schema


## Versioning

- Git
- GitHub


---

# 📂 Structure du projet

banking-fraud-platform/

│
├── data/
│
├── database/
│ └── connection.py
│
├── pipelines/
│ ├── extraction.py
│ ├── transformation.py
│ ├── loading.py
│ └── run_pipeline.py
│
├── sql/
│ ├── fraud_kpi.sql
│ ├── transaction_analysis.sql
│ └── device_analysis.sql
│
├── requirements.txt
│
├── README.md
│
└── .gitignore


---

# ▶️ Installation


## Cloner le projet

```bash
git clone https://github.com/GGFabrice/banking-fraud-platform.git

Créer l'environnement virtuel

python -m venv venv

Activation :

Windows :

venv\Scripts\activate

Installer les dépendances

pip install -r requirements.txt

▶️ Exécution du pipeline

Lancer :

python -m pipelines.run_pipeline

Résultat attendu :

🚀 DÉMARRAGE DU PIPELINE BANKING FRAUD PLATFORM

Extraction terminée

Transformation terminée

Chargement terminé avec succès

🚀 Roadmap
Phase 1 ✅
Pipeline ETL Python
Data Warehouse PostgreSQL
KPIs fraude
Phase 2 🔄
Dockerisation
Orchestration avec Apache Airflow
Phase 3 🔄
Spark / PySpark
Traitement Big Data
Phase 4 🔄
Machine Learning
Modèle de détection fraude
Phase 5 🔄
Dashboard Power BI
Monitoring
👤 Auteur

Fabrice GNABO

Data Engineer / Data Analyst

Compétences :

Data Pipeline
Data Warehouse
Python
SQL
PostgreSQL
ETL

GitHub :

https://github.com/GGFabrice


⭐ Projet Portfolio Data Engineering

Ce projet démontre la capacité à concevoir une plateforme Data complète :

Source → ETL → Data Warehouse → KPI → Analytics