# Assignment 01: Canadian Census Big Data Wrangling & Stratification

* **Weight:** 15% of Final Grade
* **Due Date:** Week 6, Sunday 23:59 EST
* **Submission Format:** Python script (`census_pipeline.py`) + Markdown Technical Report (`REPORT.md`)

---

## 1. Problem Statement
Statistics Canada processes multi-terabyte demographic files containing individual and household microdata. As a Junior Big Data Engineer in the Data Architecture division, you are tasked with engineering a distributed PySpark pipeline to ingest, clean, validate, and compute demographic indicators across Canada's economic regions.

## 2. Requirements & Deliverables
1. **Explicit Schema Enforcement:** Ingest 10 million raw CSV records using a strongly-typed `StructType`.
2. **Data Cleansing & Validation:**
   * Filter invalid negative income values and impute missing education statuses using statistical mode per province.
   * Standardize province codes to ISO 3166-2:CA standards (e.g., "Ontario" -> "ON").
3. **Optimized Distributed Joins:**
   * Broadcast join the cleansed census records with a small reference table containing regional cost-of-living adjustments (COLA).
4. **Calculations:**
   * Compute median adjusted household income by economic region and age cohort.
   * Calculate the Gini coefficient approximation per province.
5. **Output Format:**
   * Write final cleansed output to partitioned Parquet files (`partitionBy("province", "fiscal_year")`) with Snappy compression.

## 3. Evaluation Rubric

| Criteria | Description | Marks |
| :--- | :--- | :---: |
| **Schema & Ingestion** | Robust schema definition without auto-inference; correct null handling | 20 |
| **Spark Optimization** | Effective use of Broadcast joins, partition pruning, and cache management | 30 |
| **Analytical Calculations**| Accurate metric calculations (Income quantiles, Gini index) | 30 |
| **Code Quality & PEP8**| Modular functions, docstrings, type hinting, and unit tests | 20 |
| **Total** | | **100** |
