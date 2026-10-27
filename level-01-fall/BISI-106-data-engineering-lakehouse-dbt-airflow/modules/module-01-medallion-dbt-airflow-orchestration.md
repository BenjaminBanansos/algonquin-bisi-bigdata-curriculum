# Module 01: Lakehouse Medallion Architecture, dbt Transformations & Airflow Orchestration

* **Course:** BISI-106: Big Data Engineering, Lakehouse Architecture & dbt/Airflow Pipelines
* **Estimated Workload:** 6 Hours Lecture & Independent Study | 4 Hours Hands-on Laboratory
* **Prerequisites:** BISI-101 (PySpark), BISI-102 (SQL Analytics)
* **Instructional Design Standard:** University Postgraduate / Coursera MasterTrack Rigor

---

## 1. Module Learning Objectives (Bloom's Revised Taxonomy)

Upon successful completion of this module, students will be able to:
1. **[Bloom: Understand]** Contrast the Medallion Data Architecture (Bronze, Silver, Gold) with traditional Kimball dimensional data warehousing.
2. **[Bloom: Analyze]** Deconstruct a dbt project DAG, tracing lineage dependencies across sources, staging views, incremental models, and mart tables.
3. **[Bloom: Evaluate]** Implement automated data quality gates using dbt generic tests (uniqueness, referential integrity, accepted values) to prevent corrupt data from reaching production reporting.
4. **[Bloom: Create]** Author idempotent Apache Airflow Directed Acyclic Graphs (DAGs) using the Taskflow API with automated failure alerting and retry backoff.

---

## 2. In-Depth Theoretical Lecture

### 2.1 The Medallion Lakehouse Architecture
In modern big data engineering (Armbrust et al., 2021), data transitions through three distinct logical and physical stages:
* **Bronze Layer (Raw Ingestion / Landing):**
  * Exact historical copy of source transaction logs, Kafka streaming payloads, or Statistics Canada dumps.
  * Append-only; no schema transformations or data filtering allowed. Preserves raw fidelity for auditing.
* **Silver Layer (Cleaned & Conformed):**
  * Schema enforcement, deduplication, timezone normalization (UTC), data type casting, and de-identification.
  * Represents an enterprise-wide single source of truth ("Clean Data").
* **Gold Layer (Curated Business Marts):**
  * Dimensional star schemas (Kimball & Ross, 2013) optimized for reporting performance, KPI metrics, aggregations, and feature stores for machine learning.

```
[Raw Sources: APIs, Kafka, Open Gov]
                |
                v
+-------------------------------+
|      BRONZE LAYER (Raw)       |  <- Append-only, schema as ingested, full historical audit
+-------------------------------+
                |  (dbt transformations + Great Expectations schema tests)
                v
+-------------------------------+
|     SILVER LAYER (Cleaned)    |  <- Deduplicated, standardized types, PII masked
+-------------------------------+
                |  (dbt dimensional aggregation models)
                v
+-------------------------------+
|       GOLD LAYER (Marts)      |  <- Star schemas, KPI aggregations, sub-second Power BI queries
+-------------------------------+
```

### 2.2 dbt (Data Build Tool): Software Engineering Best Practices for SQL
Traditionally, SQL transformations in ETL tools were stored in unversioned stored procedures or opaque drag-and-drop interfaces. **dbt** brings software engineering rigor to data:
* **Code as Versioned SQL:** Transformations are modular `SELECT` statements version-controlled in Git.
* **Declarative Lineage (`ref()`):** Instead of hardcoding table names, models reference dependencies via `{{ ref('stg_departments') }}`. dbt automatically compiles the dependency graph and determines execution order.
* **Automated Testing:** Every model is accompanied by schema assertions:
  ```yaml
  models:
    - name: fct_procurement_contracts
      columns:
        - name: contract_id
          tests:
            - unique
            - not_null
        - name: contract_value
          tests:
            - dbt_expectations.expect_column_values_to_be_between:
                min_value: 0.00
  ```

---

## 3. Required Academic Literature & Readings

1. **Armbrust, M. et al. (2021).** *Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics.* In CIDR 2021.
2. **Kimball, R., & Ross, M. (2013).** *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling.* John Wiley & Sons.  
   *Reading Focus:* Chapter 1 (Elements of Dimensional Design) & Chapter 2 (Retail/Procurement Case Studies).
3. **Kleppmann, M. (2017).** *Designing Data-Intensive Applications.* O'Reilly Media.  
   *Reading Focus:* Chapter 10: "Batch Processing Workflows".

---

## 4. Formative Self-Assessment Quiz

### Question 1
In an Apache Airflow DAG, why is it critical that every task be **idempotent**?
* A) Because Airflow cannot execute tasks that take more than 5 minutes.
* B) Because network failures, worker crashes, or backfilling can cause Airflow to re-run a task multiple times; an idempotent task guarantees that re-executing it yields the exact same state without producing duplicate records.
* C) Idempotency is only required for machine learning models.
* D) It allows tasks to bypass database security checks.

> **Answer:** **B**  
> **Pedagogical Rationale:** If a pipeline fails midway through a daily run, Airflow retries the task. If the task simply executes an `INSERT INTO`, re-running it creates duplicate rows. By designing idempotent operations (e.g., partition overwrites, Delta `MERGE INTO`, or truncating temporary staging tables), subsequent runs produce the correct state without side effects.

---

## 5. Direct Capstone & Federal Competency Traceability

* **Connection to BISI-201 Public Sector Capstone:**  
  Directly implemented in **Sprint 2 (Pipelines & Orchestration)**. Teams deliver their dbt repository with at least 30 generic tests and a production Airflow DAG.
* **Federal Classification Competency:**  
  * **Classification:** IT-01 / IT-02 (Data Solutions Developer / Analytics Engineer).
  * **Interview Drill Question:** *"Describe the Medallion Architecture and explain why raw data is preserved in Bronze storage rather than cleaned immediately during extraction."*
