# Master Capstone & Federal Competency Traceability Matrix

This matrix establishes direct, unambiguous traceability from each course module to the **BISI-201 Capstone Project**, the **4 Student Portfolio Repositories**, and the **Government of Canada Technical Competency Classifications** (IT-01, IT-02, EC-02, EC-04).

---

## 1. Traceability Architecture

```
+--------------------------------------------------------------------------------------------------+
| COURSE WORK MODULES (Weeks 1 to 28)                                                              |
| (Theory + Academic Literature + Guided Labs + Quizzes)                                           |
+--------------------------------------------------------------------------------------------------+
                                        |
                                        v
+--------------------------------------------------------------------------------------------------+
| STUDENT GITHUB PORTFOLIO PROJECTS (Continuous Engineering)                                       |
| - Project 1: Federal Open Data Lakehouse (PySpark + Delta + dbt + Airflow)                       |
| - Project 2: Bilingual WCAG 2.1 AA Executive Dashboard (Power BI)                                |
| - Project 3: Real-Time Municipal Telemetry Stream (Kafka + Spark Streaming)                      |
| - Project 4: Audited Public Service RAG Assistant (LangChain + AIA + Presidio)                   |
+--------------------------------------------------------------------------------------------------+
                                        |
                                        v
+--------------------------------------------------------------------------------------------------+
| BISI-201 PUBLIC SECTOR CAPSTONE (Final Synthesis - Real Client Deliverable)                      |
| S0: Charter & Architecture | S1: Ingestion | S2: ELT & Marts | S3: BI & Access | S4: AIA & Demo   |
+--------------------------------------------------------------------------------------------------+
                                        |
                                        v
+--------------------------------------------------------------------------------------------------+
| PUBLIC SECTOR HIRING & CO-OP BRIDGING                                                            |
| IT-01 / IT-02 Data Solutions Developer | EC-02 / EC-04 Policy Analytics Modeler                 |
+--------------------------------------------------------------------------------------------------+
```

---

## 2. Granular Module-to-Capstone & Career Traceability Table

| Course & Module | Technical Competency Acquired | Direct Linkage to Capstone (BISI-201) | Student Portfolio Artifact | Federal Classification Competency |
| :--- | :--- | :--- | :--- | :--- |
| **BISI-101: M1** Distributed Runtime Internals | Spark Driver/Executor allocation, RDD lineage, Tungsten off-heap memory | **Capstone Sprint 0:** Sizing compute cluster and configuring cluster resource allocation. | *Project 1:* `cluster_config.py` & execution plan profiler | **IT-02:** Ability to diagnose and optimize distributed compute memory bottlenecks. |
| **BISI-101: M2** DataFrame Optimization & Joins | Broadcast Hash vs. Sort-Merge joins, key salting, window aggregations | **Capstone Sprint 2:** Processing 50M+ raw client transaction rows with zero data skew. | *Project 1:* `pyspark_pipeline.py` with broadcast lookups | **IT-01/IT-02:** Experience developing production data transformations using PySpark. |
| **BISI-101: M3** Lakehouse & Delta Lake ACID | Transaction log (`_delta_log`), time-travel, vacuum, `MERGE INTO` upserts | **Capstone Sprint 1:** Ingesting Bronze delta tables with ACID transaction guarantees. | *Project 1:* Delta Lake storage layer with snapshot isolation | **IT-02:** Expertise in designing reliable modern cloud lakehouse storage formats. |
| **BISI-102: M1** Query Optimization & Indexing | PostgreSQL `EXPLAIN ANALYZE`, B-Tree vs. BRIN indexes, MVCC vacuum tuning | **Capstone Sprint 2:** Optimizing relational analytical stores for sub-second query latency. | *Course Repository:* `sql_benchmarking.sql` with query plans | **IT-01/IT-02:** Advanced relational database query optimization and performance tuning. |
| **BISI-102: M2** Multi-Tenant Security & RLS | Row-Level Security (RLS) policies, RBAC, least privilege, audit logging | **Capstone Sprint 3:** Restricting departmental data visibility based on user tenant roles. | *Course Repository:* `rls_security_policies.sql` | **IT-02:** Implementing data access security controls for multi-departmental systems. |
| **BISI-103: M1** PBMM Sovereign Cloud Architecture| CCCS ITSG-33, KMS envelope encryption, zero-ingress subnets, Terraform | **Capstone Sprint 0 & 1:** Deploying client landing zone in AWS/Azure Canada Central. | *Project 1 & 4:* Terraform IaC modules (`main.tf`, `kms.tf`) | **IT-02:** Knowledge of Government of Canada cloud security guardrails and ITSG-33. |
| **BISI-104: M1** Policy Analytics & Explainable AI | Scikit-Learn, XGBoost, SHAP global/local importance, fairness metrics | **Capstone Sprint 4:** Providing transparent predictive scorecards for client decision makers. | *Project 4:* `policy_model.py` with SHAP beeswarm visualizations | **EC-02/EC-04:** Quantitative statistical modeling and policy impact assessment. |
| **BISI-105: M1** WCAG 2.1 AA & Bilingual BI | Screen-reader alt-text, contrast ratios (>4.5:1), dynamic EN/FR DAX measures | **Capstone Sprint 3:** Delivering client executive dashboard compliant with Official Languages. | *Project 2:* Bilingual Power BI PBIX + JSON accessible theme | **IT-01/EC-02:** Building executive reporting solutions meeting federal accessibility standards. |
| **BISI-106: M1** Medallion dbt & Airflow Pipelines| Bronze/Silver/Gold data marts, dbt generic tests, Airflow DAG orchestration | **Capstone Sprint 2:** Orchestrating automated daily pipeline runs with quality gates. | *Project 1:* `dbt_project/` with 50+ assertions and Airflow DAG | **IT-01/IT-02:** Experience with modern ELT workflow orchestration and automated testing. |
| **BISI-202: M1** Real-Time Kafka & Spark Streaming | Pub/Sub event streaming, sliding windows, watermarks for late data | **Capstone (Optional Telematics Brief):** Processing live emergency transit streams. | *Project 3:* Real-time streaming pipeline consuming Kafka | **IT-02:** Real-time data streaming and event-driven architecture engineering. |
| **BISI-203: M1** Cloud Platforms (Databricks/Snowflake)| Unity Catalog 3-level namespace, Snowflake Zero-Copy, Snowpipe | **Capstone Enterprise Track:** Deploying multi-engine governance on enterprise data. | *Project 1:* Unity Catalog configuration and data lineage graph | **IT-02:** Enterprise data cloud platform administration and fine-grained access control. |
| **BISI-204: M1** Data Vault 2.0 & Data Mesh | Hubs, Links, Satellites, Record linkage, Data product contract definitions | **Capstone Sprint 2:** Unifying citizen identity records across disparate source systems. | *Course Repository:* `data_vault_model.sql` and JSON contracts | **IT-02:** Advanced enterprise data modeling and federated data mesh architecture. |
| **BISI-205: M1** TBS AIA & Private RAG Agents | Algorithmic Impact Assessment scoring, LangChain RAG, PII sanitization | **Capstone Sprint 4:** Delivering a fully audited, Privacy Act-compliant AI assistant. | *Project 4:* Audited RAG agent + signed TBS AIA Report | **IT-02/EC-04:** Compliance auditing under the TBS Directive on Automated Decision-Making. |

---

## 3. Federal Public Service Interview Demonstration Rubric

Graduates use their project portfolio directly during Government of Canada competency-based interviews:

### Interview Question 1 (IT-02 Competency: Data Engineering)
* **Prompt:** *"Describe a situation where a batch data pipeline failed due to data skew or memory overflow. How did you diagnose and remediate the issue?"*
* **Candidate Defense Evidence (From BISI-101 & BISI-106):**  
  Candidates present their *Project 1* repository:  
  1. Open the Spark UI Event Timeline to demonstrate diagnosing a severe shuffle read bottleneck where 95% of records hashed to executor partition 3.  
  2. Walk through the code implementation of salting the skewed join key with an integer range `[0..N-1]` to distribute records evenly across executors.  
  3. Show the benchmark result: execution time reduced from 42 minutes with memory spilling down to 3.8 minutes purely in-memory.

### Interview Question 2 (IT-01/EC-02 Competency: Client Reporting & Standards)
* **Prompt:** *"How do you ensure digital dashboards comply with Canadian federal accessibility and official language mandates?"*
* **Candidate Defense Evidence (From BISI-105):**  
  Candidates present their *Project 2* live Power BI dashboard:  
  1. Demonstrate the single-click dynamic language toggle: show how DAX measures dynamically switch all KPI cards, axis labels, and tooltip descriptions between French and English.  
  2. Run the NVDA screen-reader: show how the custom DAX narrative measure reads out an automated, context-aware verbal summary of the trend rather than raw unreadable chart data.  
  3. Validate against the WCAG 2.1 AA audit checklist verifying all elements exceed the 4.5:1 contrast ratio.

### Interview Question 3 (EC-04/IT-02 Competency: Responsible AI & Ethics)
* **Prompt:** *"Under the TBS Directive on Automated Decision-Making, what steps are mandatory before deploying a predictive model that impacts public benefits?"*
* **Candidate Defense Evidence (From BISI-104 & BISI-205):**  
  Candidates present their *Project 4* Algorithmic Impact Assessment (AIA) dossier:  
  1. Show the completed 60-question AIA questionnaire classifying the system at Impact Level II.  
  2. Walk through the SHAP explainability beeswarm plot demonstrating which socioeconomic variables drive model decisions.  
  3. Demonstrate the automated PII masking pipeline using Microsoft Presidio to scrub Social Insurance Numbers and personal identifiers before any data touches the analytical repository.
