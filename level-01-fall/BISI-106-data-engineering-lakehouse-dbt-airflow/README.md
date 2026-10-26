# BISI-106: Big Data Engineering, Lakehouse Architecture & dbt/Airflow Pipelines

* **Course Code:** BISI-106
* **Contact Hours:** 42.0 Hours (3.0 hrs/week × 14 weeks)
* **Delivery Mode:** Pipeline Engineering Studio
* **Prerequisites:** Admission to Program

---

## 1. Course Description
Covers the architectural paradigm shift from traditional ETL to the modern **Lakehouse Medallion Architecture (Bronze, Silver, Gold)**. Students write declarative SQL transformation models using **dbt (data build tool)** incorporating data freshness tests, uniqueness constraints, and automated data documentation. Complex multi-node pipeline orchestration is implemented in **Apache Airflow 2.9**, scheduling distributed tasks with automated failure alerts, backfilling, and data contract validations.

---

## 2. Weekly Syllabus

| Week | Lecture Topics | Laboratory Work |
| :---: | :--- | :--- |
| **01** | Modern Data Stack overview: ETL vs. ELT, Cloud Data Lakehouses | Ingesting raw JSON into MinIO/S3 object storage |
| **02** | The Medallion Architecture: Bronze (Raw), Silver (Cleansed), Gold (Aggregated) | Structuring data lake partitions by ingestion date |
| **03** | Introduction to dbt-core: Project layout, profiles, connections | Setting up dbt with PostgreSQL/Snowflake adapters |
| **04** | dbt Models: `ref()` dependencies, ephemeral vs. view vs. table materializations | Building staging models for open data feeds |
| **05** | Incremental Models in dbt: `is_incremental()`, merge keys, unique keys | Lab 01: Incremental Processing of Procurement Feeds |
| **06** | dbt Testing Framework: Schema tests, custom generic assertions | Lab 02: Automated Data Quality Assurance with dbt |
| **07** | dbt Documentation & Data Lineage: Auto-generating enterprise DAG catalogs | Publishing interactive dbt data lineage graphs |
| **08** | Apache Airflow Core Concepts: DAGs, Operators, Sensors, Hooks | Deploying Airflow in Docker & configuring Connections |
| **09** | Writing Robust Airflow DAGs: Idempotency, backfilling, catchup configurations | Scheduling hourly data synchronization jobs |
| **10** | The Taskflow API (`@task`, `@dag`) in Airflow 2.x | Lab 03: Taskflow Orchestration with Failure Hooks |
| **11** | Orchestrating dbt runs within Airflow DAGs using `BashOperator` and Cosmos | Building an end-to-end Airflow + dbt pipeline |
| **12** | Data Contracts & Quality Gates: Great Expectations integration | Halting pipeline progression on schema drift |
| **13** | CI/CD for Data Pipelines: GitLab CI / GitHub Actions automated testing | Automating dbt test runs on pull requests |
| **14** | Pipeline Project Demos & Lineage Defense | Review of Assignment 01 Open Data Lakehouse |

---

## 3. Directory Contents
* [`airflow-dags/`](airflow-dags/) - Production Airflow DAGs for government open data ingestion.
* [`dbt_project/`](dbt_project/) - Runnable dbt project structure.
* [`labs/`](labs/) - 3 Hands-on pipeline engineering labs.
