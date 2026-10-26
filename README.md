# Big Data Engineering & Public Sector Business Intelligence Systems Infrastructure (BISI)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Credential](https://img.shields.io/badge/Credential-Ontario%20College%20Graduate%20Certificate-blue.svg)](00-program-handbook/PROGRAM_MONOGRAPH.md)
[![Standard](https://img.shields.io/badge/Framework-TBS%20PBMM%20%26%20CCCS%20ITSG--33-red.svg)](level-01-fall/BISI-103-government-cloud-pbmm-architecture/)
[![Spark](https://img.shields.io/badge/Apache%20Spark-3.5.1%20PySpark-E25A1C.svg)](level-01-fall/BISI-101-pyspark-distributed-computing/)
[![PowerBI](https://img.shields.io/badge/Power%20BI-WCAG%202.1%20AA%20Bilingual-F2C811.svg)](level-01-fall/BISI-105-accessible-bilingual-bi-visualization/)
[![Co-op](https://img.shields.io/badge/Co--op-14%20Weeks%20Paid%20Placement-success.svg)](level-03-coop/WKT-8001-work-term-i/)

> **Institutional Reference:** Modeled after Algonquin College's *Business Intelligence System Infrastructure (BISI)* (Program Code `1514X03FWO`), School of Advanced Technology, Ottawa, Canada.

---

## 🏛️ Program Executive Summary

The **Big Data Systems & Public Sector Business Intelligence Infrastructure** program is a high-rigor, one-year post-graduate certificate program (two academic terms plus an optional 14-week paid co-op work term). Situated in Canada's National Capital Region (NCR), this curriculum integrates **enterprise Big Data engineering (PySpark, Delta Lake, Snowflake, Kafka)** with the specialized architectural and legislative requirements of the **Government of Canada (GoC), crown agencies, and defense/public sector contractors**.

Graduates develop end-to-end competencies across the entire data lifecycle: distributed data extraction, high-throughput streaming pipelines, PBMM-hardened sovereign cloud design, bilingual WCAG-compliant analytics storytelling, and Algorithmic Impact Assessments (AIA) under Treasury Board Secretariat (TBS) mandates.

---

## 🧭 Curriculum Architecture & Academic Course Map

```
+-------------------------------------------------------------------------------------------------+
| LEVEL 01 (FALL TERM) - 14 WEEKS - 336 CONTACT HOURS                                             |
+-------------+-------------------------------------------------------------------------+---------+
| Course Code | Course Title                                                            | Hours   |
+-------------+-------------------------------------------------------------------------+---------+
| BISI-101    | Big Data Programming & Distributed Computing with PySpark               | 56 hrs  |
| BISI-102    | Advanced Enterprise Database Analytics & SQL for Big Data               | 70 hrs  |
| BISI-103    | Government Cloud Infrastructure & PBMM Secure Architecture              | 56 hrs  |
| BISI-104    | Machine Learning 1: Predictive Modeling & Policy Analytics              | 56 hrs  |
| BISI-105    | Accessible & Bilingual BI Visualization (Power BI / WCAG 2.1 AA)        | 42 hrs  |
| BISI-106    | Big Data Engineering, Lakehouse Architecture & dbt/Airflow Pipelines    | 42 hrs  |
| GEP-1001    | Public Sector Co-op Readiness & Security Clearance Prep                 | 21 hrs  |
+-------------+-------------------------------------------------------------------------+---------+
                                              |
                                              v
+-------------------------------------------------------------------------------------------------+
| LEVEL 02 (WINTER TERM) - 14 WEEKS - 318 CONTACT HOURS                                           |
+-------------+-------------------------------------------------------------------------+---------+
| Course Code | Course Title                                                            | Hours   |
+-------------+-------------------------------------------------------------------------+---------+
| BISI-201    | Public Sector Big Data Capstone Project (Client Sponsored)              | 84 hrs  |
| BISI-202    | Real-Time Analytics & Streaming Architectures (Kafka & Spark Streaming) | 56 hrs  |
| BISI-203    | Enterprise Cloud Data Platforms (Databricks, Snowflake & IaC)           | 56 hrs  |
| BISI-204    | Big Data Modelling, Data Mesh & Master Data Management (MDM)            | 56 hrs  |
| BISI-205    | ML 2: TBS Algorithmic Impact Assessment, Responsible AI & LLMs          | 56 hrs  |
| GEP-2001    | Co-op Competition, Federal Pool Match & Technical Interviews            | 10 hrs  |
+-------------+-------------------------------------------------------------------------+---------+
                                              |
                                              v
+-------------------------------------------------------------------------------------------------+
| LEVEL 03 (SUMMER TERM) - 14 WEEKS - 420 TO 560 HOURS                                            |
+-------------+-------------------------------------------------------------------------+---------+
| Course Code | Course Title                                                            | Type    |
+-------------+-------------------------------------------------------------------------+---------+
| WKT-8001    | Cooperative Education Work Term I (Government / Crown Corp / High-Tech) | Paid    |
+-------------+-------------------------------------------------------------------------+---------+
```

---

## 🛠️ Technology Stack & Regulatory Standards

| Domain | Core Tools & Frameworks | Regulatory & Governance Standards |
| :--- | :--- | :--- |
| **Distributed Big Data** | Apache Spark 3.5.1, PySpark, Delta Lake 3.2, Parquet, DuckDB | Statistics Canada open data protocols, Census formatting |
| **Enterprise Databases** | PostgreSQL 16, Snowflake, Azure Synapse, DuckDB | ACID Isolation, Row-Level Security (RLS), RBAC |
| **Pipeline Automation** | dbt-core 1.8, Apache Airflow 2.9, Docker, Make, Git | Data Lineage, Test Driven Development (TDD) for data |
| **Real-Time Streaming** | Apache Kafka 7.5, Zookeeper, Spark Structured Streaming | Event-driven microservices, Schema Registry (Avro) |
| **Government Cloud** | AWS Canada Central, Azure Canada Central, Terraform | **PBMM (Protected B, Medium Integrity/Availability)**, ITSG-33 |
| **BI & Analytics UX** | Microsoft Power BI Service, Tableau Desktop, DAX, Tabular Editor | **WCAG 2.1 Level AA Accessibility**, **Official Languages Act (FR/EN)** |
| **Public Sector AI** | Scikit-Learn, XGBoost, SHAP, LangChain, ChromaDB, Presidio | **TBS Directive on Automated Decision-Making (AIA)**, ATIP |

---

## 🎯 Program Vocational Learning Outcomes (VLOs)

The graduate has reliably demonstrated the ability to:
1. **Analyze and resolve enterprise big data engineering problems** using distributed compute clusters, vectorization, and memory-optimized pipelines.
2. **Design, implement, and maintain secure, multi-tenant databases and data warehouses** applying role-based access control (RBAC) and row-level security (RLS).
3. **Provision hardened cloud infrastructure** in compliance with Canadian sovereign data residency and Treasury Board Protected B (PBMM) security guardrails.
4. **Develop automated, tested, and containerized ELT/ETL pipelines** using dbt, Apache Airflow, and Docker.
5. **Engineer accessible, bilingual executive dashboards** adhering to WCAG 2.1 AA screen-reader requirements and dynamic English/French localization.
6. **Deploy supervised and unsupervised machine learning models** that satisfy ethical AI mandates, model interpretability (SHAP/LIME), and bias auditing.
7. **Construct streaming analytics pipelines** capable of processing continuous event streams with watermarking and exactly-once processing guarantees.
8. **Architect modern data fabrics** utilizing Data Vault 2.0, Master Data Management (MDM), and domain-driven Data Mesh paradigms.
9. **Conduct formal Algorithmic Impact Assessments (AIA)** and deploy private Retrieval-Augmented Generation (RAG) agents with automated PII masking.
10. **Deliver complex, client-facing capstone solutions** under an Agile/Scrum framework with version-controlled continuous integration.

---

## 🚀 Rapid Local Environment Setup

This repository contains a complete local multi-container laboratory replicating the enterprise big data stack.

### Prerequisites
* Docker Engine 24.0+ and Docker Compose v2.20+
* 16GB RAM minimum (32GB recommended)
* Python 3.10+ and Git

### Launching the Stack
```bash
# 1. Clone repository
git clone https://github.com/BenjaminBanansos/algonquin-bisi-bigdata-curriculum.git
cd algonquin-bisi-bigdata-curriculum

# 2. Launch Dockerized Services (Spark Master/Worker, Postgres, Kafka, MinIO, Airflow)
make up

# 3. Check status of running services
make status
```

### Accessing Services
* **JupyterLab (PySpark):** [http://localhost:8888](http://localhost:8888) (Token: `bisi2026`)
* **Spark Master UI:** [http://localhost:8081](http://localhost:8081)
* **Apache Airflow Orchestrator:** [http://localhost:8080](http://localhost:8080) (`admin` / `admin`)
* **MinIO S3 Storage Console:** [http://localhost:9001](http://localhost:9001) (`minio_gov_admin` / `MinioSecurePassword2026!`)
* **PostgreSQL Database:** `localhost:5432` (DB: `public_sector_analytics`, User: `bisi_admin`, Password: `GovPassword2026!`)

---

## 📂 Repository Directory Index

* [`00-program-handbook/`](00-program-handbook/) - Official Academic Monograph, VLO Matrix, BYOD Specs, and Grading Policies.
* [`level-01-fall/`](level-01-fall/) - Term 1 Courses, Work Labs, Datasets, and Assignments.
  * [`BISI-101: PySpark Distributed Computing`](level-01-fall/BISI-101-pyspark-distributed-computing/)
  * [`BISI-102: Enterprise Database Analytics & SQL`](level-01-fall/BISI-102-enterprise-database-analytics-sql/)
  * [`BISI-103: Government Cloud & PBMM Architecture`](level-01-fall/BISI-103-government-cloud-pbmm-architecture/)
  * [`BISI-104: Machine Learning & Policy Analytics`](level-01-fall/BISI-104-machine-learning-policy-analytics/)
  * [`BISI-105: Accessible & Bilingual BI (Power BI)`](level-01-fall/BISI-105-accessible-bilingual-bi-visualization/)
  * [`BISI-106: Lakehouse Engineering (dbt & Airflow)`](level-01-fall/BISI-106-data-engineering-lakehouse-dbt-airflow/)
  * [`GEP-1001: Co-op Readiness & Security Clearances`](level-01-fall/GEP-1001-coop-readiness-security-clearance/)
* [`level-02-winter/`](level-02-winter/) - Term 2 Courses, Advanced Labs, and Capstone Project.
  * [`BISI-201: Public Sector Capstone Project`](level-02-winter/BISI-201-public-sector-capstone-project/)
  * [`BISI-202: Real-Time Streaming (Kafka & Spark)`](level-02-winter/BISI-202-realtime-streaming-kafka-spark/)
  * [`BISI-203: Cloud Platforms (Databricks & Snowflake)`](level-02-winter/BISI-203-cloud-data-platforms-databricks-snowflake/)
  * [`BISI-204: Data Modelling & Data Mesh`](level-02-winter/BISI-204-data-modelling-datamesh-mdm/)
  * [`BISI-205: Responsible AI & LLM Governance (AIA)`](level-02-winter/BISI-205-responsible-ai-aia-llm-governance/)
  * [`GEP-2001: Federal Pool Match & Technical Interviews`](level-02-winter/GEP-2001-coop-competition-federal-pool/)
* [`level-03-coop/`](level-03-coop/) - 14-Week Paid Co-op Work Term Protocols, Deliverables & Report Rubrics.

---

## 💼 Co-op & Public Service Career Bridging

Graduates are directly qualified for Canadian public service and enterprise classifications:
* **Government of Canada:** IT-01 / IT-02 (Data Solutions Developer / Database Analyst), EC-02 to EC-04 (Quantitative Data Analyst / Modeler), CS-01 / CS-02 (Crown Corporations).
* **Private & Consulting Sector:** Big Data Engineer, Analytics Engineer (dbt/Snowflake), BI Specialist (Power BI/Tableau), Cloud Platform Engineer.
* **Security Clearance Support:** Includes formal step-by-step guidance for **Reliability Status** and **Secret Level II** screening via the Departmental Security Officer (DSO) process.

---

## 📜 Academic Integrity & License

This curriculum is published under the [MIT License](LICENSE). Academic institutions, instructors, and government training units are free to adopt, modify, and deploy these materials with appropriate attribution.
