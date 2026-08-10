# 🏦 Banking Fraud Platform

## 📌 Présentation du projet

**Banking Fraud Platform** est une plateforme Data Engineering conçue pour collecter, nettoyer, transformer, stocker et analyser des données de transactions bancaires afin de suivre les comportements frauduleux.

Le projet simule un environnement bancaire comprenant :

* des clients ;
* des comptes bancaires ;
* des appareils et terminaux ;
* des commerçants ;
* des transactions financières.

L'objectif est de construire une chaîne complète de traitement des données allant de la génération des données jusqu'à leur exploitation analytique dans un **Data Warehouse PostgreSQL** et un **dashboard Power BI**.

---

# 🎯 Objectifs

Le projet permet de :

* générer des données bancaires simulées ;
* construire un pipeline ETL avec Python ;
* nettoyer et transformer les données avec Pandas ;
* concevoir un Data Warehouse analytique ;
* implémenter un modèle dimensionnel de type **Star Schema** ;
* charger les données dans PostgreSQL ;
* développer des requêtes, KPIs et vues SQL dédiés à la fraude ;
* analyser les fraudes selon plusieurs dimensions ;
* construire un dashboard Power BI interactif ;
* versionner le projet avec Git et GitHub.

---

# 🏗️ Architecture de la plateforme

```text
                 DONNÉES SIMULÉES
                        │
                        ▼
                 Data Generator
                        │
                        ▼
                   Extraction
                      Python
                        │
                        ▼
               Cleaning / Transformation
                   Python / Pandas
                        │
                        ▼
              DATA WAREHOUSE POSTGRESQL
                        │
              ┌─────────┴─────────┐
              │                   │
              ▼                   ▼
         Dimensions          Fact Transactions
              │                   │
              └─────────┬─────────┘
                        ▼
                  SQL / KPIs
                        │
                        ▼
                 Power BI Dashboard
                        │
                        ▼
               Analyse de la fraude
```

---

# 🔄 Pipeline Data Engineering

## 1. Génération des données

Le projet contient un module `data_generator/` permettant de générer des données bancaires simulées.

Les principaux générateurs sont :

* `generate_customers.py`
* `generate_accounts.py`
* `generate_devices.py`
* `generate_merchants.py`
* `generate_transactions.py`

Ces scripts permettent de créer les différentes sources nécessaires au pipeline.

---

## 2. Extraction

L'extraction est réalisée avec Python.

Le module principal est :

```text
pipelines/extract.py
```

Il constitue le point d'entrée pour récupérer les données sources avant leur transformation.

---

## 3. Nettoyage et transformation

Les données sont préparées avec Python et Pandas.

Les traitements comprennent notamment :

* nettoyage des données ;
* suppression des doublons ;
* traitement des valeurs manquantes ;
* contrôle des types de données ;
* transformation des attributs ;
* préparation des données analytiques.

Les principaux modules sont :

```text
pipelines/cleaning.py
pipelines/transformation.py
pipelines/run_cleaning.py
```

Le pipeline global est exécuté avec :

```text
pipelines/run_pipeline.py
```

---

# 🗄️ Data Warehouse

Le Data Warehouse est construit avec **PostgreSQL**.

Le projet utilise une modélisation dimensionnelle de type **Star Schema**.

## Dimensions

Les principales dimensions sont :

```text
dim_customers
dim_accounts
dim_devices
dim_merchants
dim_date
```

Elles permettent d'analyser les transactions selon différents axes :

* client ;
* compte ;
* appareil ;
* commerçant ;
* temps.

## Table de faits

La table centrale du modèle est :

```text
fact_transactions
```

Elle contient les événements transactionnels utilisés pour les analyses de fraude.

---

# 🐘 Couche PostgreSQL

Le dossier `database/` contient les éléments nécessaires à la gestion de la base :

```text
database/
├── connection.py
├── create_tables.py
└── __init__.py
```

Le schéma du Data Warehouse est défini dans :

```text
sql/schema.sql
```

---

# 📊 Analyse SQL

Le dossier `sql/` contient les requêtes utilisées pour produire les indicateurs et analyses.

Principaux fichiers :

```text
sql/
├── schema.sql
├── views_dashboard.sql
├── fraud_kpi_summary.sql
├── kpi_fraud_global.sql
├── kpi_fraud_customer.sql
├── kpi_fraud_location.sql
├── kpi_fraud_transaction_type.sql
├── fraud_by_device.sql
├── fraud_by_merchant.sql
└── fraud_by_transaction_type.sql
```

Ces requêtes permettent notamment d'analyser :

* les KPIs globaux ;
* les fraudes par client ;
* les fraudes par localisation ;
* les fraudes par type de transaction ;
* les fraudes par appareil ;
* les fraudes par commerçant.

---

# 📈 KPIs de fraude

La plateforme permet notamment de suivre :

* nombre total de transactions ;
* nombre total de fraudes ;
* montant total des transactions ;
* montant total des fraudes ;
* taux de fraude.

Les indicateurs peuvent être analysés selon plusieurs dimensions.

---

# 📅 Analyse temporelle

Les données permettent d'étudier l'évolution des fraudes :

* par mois ;
* par trimestre ;
* dans le temps.

La dimension `dim_date` permet notamment de travailler avec :

```text
full_date
day
month
year
quarter
```

---

# 📍 Analyse géographique

La plateforme permet d'analyser les fraudes selon la localisation.

Les principaux indicateurs comprennent :

* nombre de transactions frauduleuses ;
* taux de fraude ;
* montant frauduleux.

---

# 📱 Analyse comportementale

Les données peuvent également être analysées selon :

* le type d'appareil ;
* le système d'exploitation ;
* le navigateur ;
* le commerçant ;
* le type de transaction.

---

# 📊 Dashboard Power BI

Le projet comprend un dashboard Power BI dédié au suivi des fraudes bancaires.

Le dashboard permet notamment de :

* suivre les principaux KPIs ;
* analyser l'évolution des fraudes ;
* analyser les montants frauduleux ;
* comparer les différentes localisations ;
* filtrer les données selon les dimensions temporelles.

Le fichier Power BI est disponible dans :

```text
dashboards/ecommerce_dashboard.pbix
```

---

# 🧰 Technologies utilisées

## Data Engineering

* Python 3.13
* Pandas
* SQL
* SQLAlchemy
* PostgreSQL

## Business Intelligence

* Microsoft Power BI

## Conteneurisation

* Docker
* Docker Compose

## Versionnement

* Git
* GitHub

## Environnement de développement

* Visual Studio Code
* Python Virtual Environment

---

# 📂 Structure du projet

```text
banking-fraud-platform/
│
├── config/
│
├── dashboards/
│   └── ecommerce_dashboard.pbix
│
├── data/
│
├── data_generator/
│   ├── generate_accounts.py
│   ├── generate_all.py
│   ├── generate_customers.py
│   ├── generate_devices.py
│   ├── generate_merchants.py
│   ├── generate_transactions.py
│   └── __init__.py
│
├── database/
│   ├── connection.py
│   ├── create_tables.py
│   └── __init__.py
│
├── docs/
│
├── pipelines/
│   ├── cleaning.py
│   ├── extract.py
│   ├── fraud_detection.py
│   ├── loading.py
│   ├── run_cleaning.py
│   ├── run_pipeline.py
│   ├── test_transformation.py
│   ├── transformation.py
│   └── __init__.py
│
├── sql/
│   ├── fraud_by_device.sql
│   ├── fraud_by_merchant.sql
│   ├── fraud_by_transaction_type.sql
│   ├── fraud_kpi_summary.sql
│   ├── kpi_fraud_customer.sql
│   ├── kpi_fraud_global.sql
│   ├── kpi_fraud_location.sql
│   ├── kpi_fraud_transaction_type.sql
│   ├── kpi_transactions.sql
│   ├── schema.sql
│   └── views_dashboard.sql
│
├── tests/
│
├── warehouse/
│   ├── models/
│   └── __init__.py
│
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
├── requirements.txt
└── test_connection.py
```

---

# ⚙️ Installation

## 1. Cloner le repository

```bash
git clone https://github.com/GGFabrice/banking-fraud-platform.git
cd banking-fraud-platform
```

## 2. Créer l'environnement virtuel

```bash
python -m venv venv
```

Sous Windows :

```bash
venv\Scripts\activate
```

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# 🐘 Configuration PostgreSQL

Créer la base de données :

```sql
CREATE DATABASE banking_dw;
```

Les paramètres de connexion sont configurés dans :

```text
database/connection.py
```

Configuration utilisée dans l'environnement du projet :

```text
Host     : localhost
Port     : 5433
Database : banking_dw
User     : postgres
```

> Les informations sensibles telles que les mots de passe doivent être conservées dans les variables d'environnement et ne doivent pas être publiées sur GitHub.

---

# ▶️ Exécution du pipeline

Le pipeline principal peut être lancé avec :

```bash
python -m pipelines.run_pipeline
```

Le processus suit la chaîne :

```text
Génération des données
        ↓
Extraction
        ↓
Cleaning
        ↓
Transformation
        ↓
Chargement PostgreSQL
        ↓
Data Warehouse
        ↓
Vues SQL / KPIs
        ↓
Power BI
```

---

# 🧪 Tests

Le projet contient également des éléments dédiés aux tests :

```text
tests/
pipelines/test_transformation.py
test_connection.py
```

Ils permettent notamment de vérifier la connexion et certains traitements du pipeline.

---

# 🐳 Docker

Le projet contient également :

```text
Dockerfile
docker-compose.yml
```

Cette couche permet de préparer le projet à une exécution dans un environnement conteneurisé.

---

# 🚀 Roadmap

## Phase 1 — Data Engineering

✅ Génération des données

✅ Pipeline ETL Python

✅ Nettoyage et transformation

✅ Data Warehouse PostgreSQL

✅ Star Schema

✅ Vues SQL

---

## Phase 2 — Business Intelligence

✅ KPIs de fraude

✅ Analyse temporelle

✅ Analyse géographique

✅ Dashboard Power BI

✅ Filtres interactifs

---

## Phase 3 — Big Data

Prochaine évolution :

* Apache Spark ;
* PySpark ;
* Spark SQL ;
* traitement de volumes plus importants ;
* optimisation des traitements.

---

## Phase 4 — Orchestration

Évolution prévue avec :

* Apache Airflow ;
* planification automatique ;
* monitoring ;
* gestion des erreurs ;
* scheduling des pipelines.

---

## Phase 5 — Machine Learning

Évolution possible vers :

* détection automatique de fraude ;
* classification des transactions ;
* scoring du risque ;
* détection d'anomalies ;
* évaluation des performances du modèle.

---

## Phase 6 — Temps réel et Cloud

Évolution possible vers :

* Apache Kafka ;
* Spark Structured Streaming ;
* traitement des transactions en temps réel ;
* détection de fraude quasi temps réel ;
* architecture AWS.

---

# 👨‍💻 Auteur

**Gnabo Fabrice**

Data Engineer / Data Analyst

GitHub : **GGFabrice**

---

# 📌 Conclusion

**Banking Fraud Platform** est un projet Data Engineering appliqué au domaine bancaire.

Il couvre une grande partie de la chaîne de valeur de la donnée :

```text
Données simulées
      ↓
Extraction
      ↓
Transformation
      ↓
Data Warehouse PostgreSQL
      ↓
SQL / KPIs
      ↓
Power BI
      ↓
Analyse de la fraude
```

Le projet constitue également une base évolutive vers une architecture plus avancée intégrant **Spark, Airflow, Kafka, Machine Learning et AWS**.
