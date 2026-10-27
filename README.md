# Big Data Engineering & Public Sector Business Intelligence Systems Infrastructure (BISI)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Credential](https://img.shields.io/badge/Credential-Ontario%20College%20Graduate%20Certificate-blue.svg)](00-program-handbook/PROGRAM_MONOGRAPH.md)
[![Standard](https://img.shields.io/badge/Framework-TBS%20PBMM%20%26%20CCCS%20ITSG--33-red.svg)](level-01-fall/BISI-103-government-cloud-pbmm-architecture/)
[![Spark](https://img.shields.io/badge/Apache%20Spark-3.5.1%20PySpark-E25A1C.svg)](level-01-fall/BISI-101-pyspark-distributed-computing/)
[![PowerBI](https://img.shields.io/badge/Power%20BI-WCAG%202.1%20AA%20Bilingual-F2C811.svg)](level-01-fall/BISI-105-accessible-bilingual-bi-visualization/)
[![Live Portal](https://img.shields.io/badge/Live%20Portal-GitHub%20Pages-brightgreen.svg)](https://benjaminbanansos.github.io/algonquin-bisi-bigdata-curriculum/)

> **Institutional Reference:** Modeled after Algonquin College's *Business Intelligence System Infrastructure (BISI)* (Program Code `1514X03FWO`), School of Advanced Technology, Ottawa, Canada.  
> **Course Website & Interactive LMS:** [https://benjaminbanansos.github.io/algonquin-bisi-bigdata-curriculum/](https://benjaminbanansos.github.io/algonquin-bisi-bigdata-curriculum/)

---

## 🏛️ Program Executive Summary & Instructional Design

The **Big Data Systems & Public Sector Business Intelligence Infrastructure** program is a high-rigor, one-year post-graduate certificate program (two academic terms plus an optional 14-week paid co-op work term). Designed with Coursera / edX MasterTrack academic depth, this curriculum integrates **enterprise Big Data engineering (PySpark, Delta Lake, Snowflake, Kafka)** with the specialized architectural and legislative requirements of the **Government of Canada (GoC), Crown agencies, and defense/public sector contractors**.

Every module adheres to strict instructional design standards:
* **Academic & Regulatory Attribution:** Grounded in peer-reviewed computer science literature (ACM, USENIX, VLDB, O'Reilly) and official Government of Canada directives.
* **Granular Learning Outcomes:** Explicitly mapped using Bloom's Revised Taxonomy (Understand, Analyze, Evaluate, Apply, Create).
* **Direct Project Traceability:** Every theoretical concept directly links to milestone deliverables in the culminating **BISI-201 Public Sector Capstone Project** and student portfolio repositories.
* **Federal Competency Alignment:** Directly prepares graduates for competitive appointment into Canadian public service classifications: **IT-01/IT-02 (Data Solutions Developer)** and **EC-02/EC-04 (Quantitative Policy Analyst)**.

---

## 🧭 Master Academic & Curriculum Documentation Index

* 📖 **[Academic Sources & Master Bibliography](00-program-handbook/ACADEMIC_SOURCES_AND_BIBLIOGRAPHY.md)**  
  Full peer-reviewed citations: Zaharia et al. (Spark), Armbrust et al. (Spark SQL & Delta Lake), Kleppmann (DDIA), Silberschatz (Database Systems), Kimball (Dimensional Modeling), Dehghani (Data Mesh), TBS Directives, and CCCS ITSG-33 standards.
* 🎯 **[Capstone & Federal Competency Traceability Matrix](00-program-handbook/CAPSTONE_AND_COMPETENCY_TRACEABILITY_MATRIX.md)**  
  End-to-end mapping from every weekly module to Capstone Sprints, student GitHub portfolios, and Federal Public Service interview rubrics.
* 📜 **[Official Academic Program Monograph](00-program-handbook/PROGRAM_MONOGRAPH.md)**  
  Institutional charter, 10 Vocational Learning Outcomes (VLOs), admission prerequisites, and Ontario Qualifications Framework (OQF Level 8) compliance.
* 💻 **[BYOD Hardware & Software Specifications](00-program-handbook/BYOD_HARDWARE_SOFTWARE_SPECS.md)**  
  Hardware specifications (RAM/CPU), Docker Desktop cluster configurations, and development tool installation guides.
* ⚖️ **[Academic Policies, Evaluation & AI Integrity](00-program-handbook/ACADEMIC_POLICIES_AND_EVALUATION.md)**  
  Grading rubrics, late penalties, and mandatory AI disclosure standards aligned with the TBS Directive on Automated Decision-Making.

---

## 📚 Curriculum Course Architecture & Deep Chapters

```
+-------------------------------------------------------------------------------------------------+
| LEVEL 01 (FALL TERM) - 14 WEEKS - 336 CONTACT HOURS                                             |
+-------------+-------------------------------------------------------------------------+---------+
| Course Code | Course Title & Chapters                                                 | Hours   |
+-------------+-------------------------------------------------------------------------+---------+
| BISI-101    | Big Data Programming & Distributed Computing with PySpark               | 56 hrs  |
|             | -> Module 01: Distributed Runtime Internals & Memory Layouts            |         |
|             | -> Module 02: Advanced Join Mechanics & Key Salting                     |         |
|             | -> Module 03: Lakehouse Delta Lake ACID Transactions                    |         |
| BISI-102    | Advanced Enterprise Database Analytics & SQL for Big Data               | 70 hrs  |
|             | -> Module 01: Relational Query Optimization & BRIN Indexing             |         |
|             | -> Module 02: Multi-Tenant Row-Level Security (RLS)                     |         |
| BISI-103    | Government Cloud Infrastructure & PBMM Secure Architecture              | 56 hrs  |
|             | -> Module 01: Sovereign Cloud & Envelope Encryption (CCCS ITSG-33)      |         |
| BISI-104    | Machine Learning 1: Predictive Modeling & Policy Analytics              | 56 hrs  |
|             | -> Module 01: Policy Analytics & Explainable AI with SHAP               |         |
| BISI-105    | Accessible & Bilingual BI Visualization (Power BI / WCAG 2.1 AA)        | 42 hrs  |
|             | -> Module 01: Accessible Dashboards & Dynamic Bilingual DAX             |         |
| BISI-106    | Big Data Engineering, Lakehouse Architecture & dbt/Airflow Pipelines    | 42 hrs  |
|             | -> Module 01: Lakehouse Medallion Architecture & dbt/Airflow            |         |
| GEP-1001    | Public Sector Co-op Readiness & Security Clearance Prep                 | 21 hrs  |
|             | -> Dossier Preparation for TBS 330-23 (Reliability) & 330-60 (Secret)   |         |
+-------------+-------------------------------------------------------------------------+---------+
                                              |
                                              v
+-------------------------------------------------------------------------------------------------+
| LEVEL 02 (WINTER TERM) - 14 WEEKS - 318 CONTACT HOURS                                           |
+-------------+-------------------------------------------------------------------------+---------+
| Course Code | Course Title & Chapters                                                 | Hours   |
+-------------+-------------------------------------------------------------------------+---------+
| BISI-201    | Public Sector Big Data Capstone Project (Client Sponsored)              | 84 hrs  |
|             | -> Agile Sprint Roadmap (S0 to S4) & Client Delivery Framework         |         |
| BISI-202    | Real-Time Analytics & Streaming Architectures (Kafka & Spark Streaming) | 56 hrs  |
|             | -> Event-Driven Telemetry & Sliding Window Watermarking                 |         |
| BISI-203    | Enterprise Cloud Data Platforms (Databricks, Snowflake & IaC)           | 56 hrs  |
|             | -> Unity Catalog Governance & Snowflake Zero-Copy Cloning               |         |
| BISI-204    | Big Data Modelling, Data Mesh & Master Data Management (MDM)            | 56 hrs  |
|             | -> Data Vault 2.0 (Hubs/Links/Satellites) & Federated Data Mesh         |         |
| BISI-205    | ML 2: TBS Algorithmic Impact Assessment, Responsible AI & LLMs          | 56 hrs  |
|             | -> Module 01: Formal AIA Audits & Sovereign Private RAG with Presidio   |         |
| GEP-2001    | Co-op Competition, Federal Pool Match & Technical Interviews            | 10 hrs  |
|             | -> Student Bridging Mechanics & 100+ Public Service Interview Bank      |         |
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
| **Distributed Big Data** | Apache Spark 3.5.1, PySpark, Delta Lake 3.2, Parquet, DuckDB | Statistics Canada open data protocols, Census microdata |
| **Enterprise Databases** | PostgreSQL 16, Snowflake, Azure Synapse, DuckDB | ACID Isolation, Row-Level Security (RLS), RBAC |
| **Pipeline Automation** | dbt-core 1.8, Apache Airflow 2.9, Docker, Make, Git | Data Lineage, Test Driven Development (TDD) for data |
| **Real-Time Streaming** | Apache Kafka 7.5, Zookeeper, Spark Structured Streaming | Event-driven microservices, Schema Registry (Avro) |
| **Government Cloud** | AWS Canada Central, Azure Canada Central, Terraform | **PBMM (Protected B, Medium Integrity/Availability)**, CCCS ITSG-33 |
| **BI & Analytics UX** | Microsoft Power BI Service, Tableau Desktop, DAX, Tabular Editor | **WCAG 2.1 Level AA Accessibility**, **Official Languages Act (FR/EN)** |
| **Public Sector AI** | Scikit-Learn, XGBoost, SHAP, LangChain, ChromaDB, Presidio | **TBS Directive on Automated Decision-Making (AIA)**, Privacy Act |

---

## 🚀 Rapid Local Multi-Container Lab Setup

The repository includes a complete local multi-container environment replicating the enterprise big data stack.

```bash
# 1. Clone repository
git clone https://github.com/BenjaminBanansos/algonquin-bisi-bigdata-curriculum.git
cd algonquin-bisi-bigdata-curriculum

# 2. Launch Dockerized Services (Spark Master/Worker, Postgres, Kafka, MinIO, Airflow)
make up

# 3. Check status of running services
make status
```

### Accessing Local Services
* **Interactive Course Portal:** [http://localhost:8000](index.html) or [Live on GitHub Pages](https://benjaminbanansos.github.io/algonquin-bisi-bigdata-curriculum/)
* **JupyterLab (PySpark):** [http://localhost:8888](http://localhost:8888) (Token: `bisi2026`)
* **Spark Master Web UI:** [http://localhost:8081](http://localhost:8081)
* **Apache Airflow Orchestrator:** [http://localhost:8080](http://localhost:8080) (`admin` / `admin`)
* **MinIO S3 Storage Console:** [http://localhost:9001](http://localhost:9001) (`minio_gov_admin` / `MinioSecurePassword2026!`)
* **PostgreSQL Database:** `localhost:5432` (DB: `public_sector_analytics`, User: `bisi_admin`, Password: `GovPassword2026!`)

---

## 📜 Academic Integrity & License

This curriculum is published under the [MIT License](LICENSE). Academic institutions, instructors, and government training units are free to adopt, modify, and deploy these materials with appropriate attribution.
