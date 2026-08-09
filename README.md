# 🏦 Banking Fraud Platform

## 📌 Présentation du projet

**Banking Fraud Platform** est une plateforme Data Engineering conçue pour collecter, transformer, stocker et analyser des données de transactions bancaires afin d'identifier et de suivre les comportements frauduleux.

Le projet simule un environnement bancaire comprenant notamment :

* des clients ;
* des comptes bancaires ;
* des appareils et terminaux ;
* des commerçants ;
* des transactions financières.

L'objectif est de construire une chaîne complète de traitement de données allant de l'ingestion des données jusqu'à leur exploitation analytique dans un **Data Warehouse PostgreSQL** et un **dashboard Power BI**.

---

## 🎯 Objectifs

Le projet permet de :

* construire un pipeline ETL avec Python ;
* nettoyer et transformer des données bancaires ;
* concevoir un Data Warehouse analytique ;
* implémenter un modèle dimensionnel de type **Star Schema** ;
* charger les données dans PostgreSQL ;
* créer des vues et des KPIs dédiés à la fraude ;
* analyser les fraudes selon plusieurs dimensions ;
* produire un dashboard Power BI interactif ;
* préparer la plateforme à de futures évolutions vers le Big Data et le Machine Learning.

---

# 🏗️ Architecture de la plateforme

```text
                  SOURCES DE DONNÉES
                         │
                         ▼
              Données bancaires
             CSV / données simulées
                         │
                         ▼
                 EXTRACTION
                    Python
                         │
                         ▼
                TRANSFORMATION
              Python / Pandas
                         │
                         ▼
                DATA WAREHOUSE
                  PostgreSQL
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
         Dimensions            Table de faits
              │                     │
              └──────────┬──────────┘
                         ▼
                   Vues SQL / KPIs
                         │
                         ▼
                    POWER BI
                         │
                         ▼
              Dashboard Fraude Bancaire
```

---

# 🔄 Pipeline ETL

## 1. Extraction

Le pipeline récupère les différentes sources de données nécessaires à l'analyse bancaire.

Les principales entités sont :

* Customers
* Accounts
* Devices
* Merchants
* Transactions

L'extraction constitue la première étape du pipeline avant le nettoyage et la transformation.

---

## 2. Transformation

Les données sont ensuite nettoyées et préparées pour leur intégration dans le Data Warehouse.

Les principales opérations comprennent :

* nettoyage des données ;
* traitement des valeurs manquantes ;
* contrôle des types de données ;
* transformation des attributs ;
* création des dimensions analytiques ;
* enrichissement des transactions ;
* création de la dimension temporelle ;
* préparation des indicateurs de fraude.

Les principales tables analytiques comprennent notamment :

```text
dim_customers
dim_accounts
dim_devices
dim_merchants
dim_date
fact_transactions
```

---

## 3. Chargement

Les données transformées sont chargées dans **PostgreSQL**.

Le processus de chargement suit le principe :

```text
Nettoyage / Transformation
          │
          ▼
   Chargement des
      dimensions
          │
          ▼
   Chargement de la
     table de faits
          │
          ▼
    Vues analytiques
          │
          ▼
       Power BI
```

---

# 🗄️ Data Warehouse

Le projet utilise une architecture dimensionnelle basée sur un **Star Schema**.

## Dimensions

### `dim_customers`

Informations relatives aux clients.

Exemples d'attributs :

* customer_id
* nom
* âge
* sexe
* ville
* pays

### `dim_accounts`

Informations relatives aux comptes bancaires.

Exemples :

* account_id
* type de compte
* solde
* statut

### `dim_devices`

Informations relatives aux appareils utilisés lors des transactions.

Exemples :

* device_id
* type d'appareil
* système d'exploitation
* navigateur

### `dim_merchants`

Informations relatives aux commerçants.

Exemples :

* merchant_id
* catégorie
* localisation
* niveau de risque

### `dim_date`

Dimension temporelle utilisée pour les analyses chronologiques.

Exemples :

* full_date
* day
* month
* year
* quarter

---

## Table de faits

### `fact_transactions`

La table de faits contient les événements transactionnels et les informations nécessaires à l'analyse des fraudes.

Exemples :

* transaction_id
* customer_id
* account_id
* merchant_id
* device_id
* transaction_type
* amount
* location
* is_fraud
* fraud_reason

---

# 📊 Analyse des fraudes

La plateforme permet de calculer plusieurs indicateurs clés.

## KPIs globaux

* nombre total de transactions ;
* montant total des transactions ;
* nombre total de fraudes ;
* montant total des fraudes ;
* taux de fraude.

---

## 📅 Analyse temporelle

Le dashboard permet d'analyser l'évolution des fraudes :

* par mois ;
* par trimestre ;
* évolution du taux de fraude ;
* montant des fraudes par mois ;
* montant des fraudes par trimestre.

Les filtres interactifs permettent également de sélectionner :

* une année ;
* un trimestre ;
* un mois.

---

## 📍 Analyse géographique

Les données permettent d'analyser les fraudes par ville.

Exemples de villes analysées :

* Abidjan ;
* Bouaké ;
* Korhogo ;
* Yamoussoukro ;
* San Pedro.

Les indicateurs disponibles comprennent :

* nombre de fraudes par ville ;
* taux de fraude par ville ;
* montant des fraudes par ville.

---

## 📱 Analyse comportementale

La plateforme est également préparée pour analyser les comportements selon :

* le type d'appareil ;
* le système d'exploitation ;
* le navigateur ;
* le commerçant ;
* le type de transaction.

---

# 📈 Dashboard Power BI

Le projet comprend un dashboard Power BI dédié à l'analyse des fraudes bancaires.

### Principaux éléments du dashboard

**KPIs :**

* Total Transactions
* Total Fraudes
* Taux de fraude

**Analyses temporelles :**

* Répartition des fraudes par mois
* Répartition des fraudes par trimestre
* Montant des fraudes par mois
* Montant des fraudes par trimestre
* Évolution du taux de fraude

**Analyses géographiques :**

* Fraudes par ville
* Taux de fraude par ville
* Montant des fraudes par ville

**Filtres interactifs :**

* Année
* Trimestre
* Mois

Le fichier Power BI est disponible dans :

```text
dashboards/ecommerce_dashboard.pbix
```

---

# 🧰 Technologies utilisées

## Langages

* Python 3.13
* SQL

## Data Engineering

* Pandas
* SQLAlchemy
* PostgreSQL
* ETL Pipeline

## Data Warehouse

* PostgreSQL
* Star Schema
* SQL Views

## Business Intelligence

* Microsoft Power BI

## Outils

* Visual Studio Code
* Git
* GitHub
* Python Virtual Environment

---

# 📂 Structure du projet

```text
banking-fraud-platform/
│
├── data/
│
├── database/
│   └── connection.py
│
├── pipelines/
│   ├── extraction.py
│   ├── transformation.py
│   ├── loading.py
│   └── run_pipeline.py
│
├── sql/
│   ├── schema.sql
│   ├── views_dashboard.sql
│   ├── kpi_fraud_global.sql
│   ├── kpi_fraud_customer.sql
│   ├── fraud_by_country.sql
│   ├── fraud_by_device.sql
│   └── fraud_by_merchant.sql
│
├── dashboards/
│   └── ecommerce_dashboard.pbix
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Cloner le projet

```bash
git clone https://github.com/GGFabrice/banking-fraud-platform.git
cd banking-fraud-platform
```

## 2. Créer l'environnement virtuel

```bash
python -m venv venv
```

### Windows

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

Configurer ensuite les paramètres de connexion dans :

```text
database/connection.py
```

Paramètres utilisés dans l'environnement du projet :

```text
Host     : localhost
Port     : 5433
Database : banking_dw
User     : postgres
```

---

# ▶️ Exécution du pipeline

Le pipeline peut être lancé avec :

```bash
python -m pipelines.run_pipeline
```

Le processus exécute les différentes étapes :

```text
Extraction
     ↓
Transformation
     ↓
Chargement
     ↓
Data Warehouse
     ↓
Vues SQL
     ↓
Power BI
```

---

# 🔮 Roadmap

## Phase 1 — Data Engineering

✅ Pipeline ETL Python

✅ Nettoyage et transformation des données

✅ Data Warehouse PostgreSQL

✅ Modèle Star Schema

✅ Vues SQL analytiques

---

## Phase 2 — Business Intelligence

✅ KPIs de fraude

✅ Analyse temporelle

✅ Analyse géographique

✅ Dashboard Power BI

✅ Filtres interactifs

---

## Phase 3 — Big Data

Prévoir l'intégration de :

* Apache Spark ;
* PySpark ;
* traitement de volumes importants ;
* optimisation des traitements ;
* Spark SQL.

---

## Phase 4 — Orchestration

Prévoir l'intégration de :

* Apache Airflow ;
* planification automatique des pipelines ;
* monitoring ;
* gestion des erreurs ;
* scheduling.

---

## Phase 5 — Machine Learning

Prévoir :

* modèle de détection automatique de fraude ;
* classification des transactions ;
* scoring du risque ;
* détection d'anomalies ;
* évaluation des performances du modèle.

---

## Phase 6 — Architecture temps réel

Évolution possible vers :

* Apache Kafka ;
* Spark Structured Streaming ;
* traitement des transactions en temps réel ;
* détection de fraude quasi temps réel ;
* architecture cloud AWS.

---

# 👨‍💻 Auteur

**Gnabo Fabrice**

Data Engineer / Data Analyst

GitHub : **GGFabrice**

---

# 📌 Conclusion

**Banking Fraud Platform** constitue un projet complet de Data Engineering appliqué au domaine bancaire.

Il couvre l'ensemble de la chaîne de valeur de la donnée :

```text
Données brutes
      ↓
Extraction
      ↓
Transformation
      ↓
Data Warehouse
      ↓
SQL / KPIs
      ↓
Power BI
      ↓
Analyse de la fraude
```

Le projet constitue également une base évolutive permettant d'intégrer ultérieurement **Spark, Airflow, Kafka, Machine Learning et AWS** afin de construire une plateforme de détection de fraude plus avancée.
