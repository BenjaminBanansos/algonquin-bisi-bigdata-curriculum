# BISI-101: Big Data Programming & Distributed Computing with PySpark

* **Course Code:** BISI-101
* **Contact Hours:** 56.0 Hours (4.0 hrs/week × 14 weeks)
* **Delivery Mode:** Hybrid / Lab-Intensive
* **Prerequisites:** Admission to Program

---

## 1. Course Description
Introduces distributed data processing using Apache Spark and PySpark. Students transition from in-memory single-node data structures to fault-tolerant distributed computing. Focuses on the internal execution mechanics of Spark (Driver, Executors, Catalyst Optimizer, Tungsten execution engine), Resilient Distributed Datasets (RDDs), Spark DataFrames, partitioning, broadcast variables, and broad transformations on administrative and census scale datasets.

---

## 2. Weekly Syllabus

| Week | Lecture Topics | Laboratory Work |
| :---: | :--- | :--- |
| **01** | Python vectorization, NumPy/Polars memory layouts, Gil considerations | Lab 01: Polars vs. Pandas Memory & Speed Benchmark |
| **02** | Distributed system fundamentals, Master/Worker topologies, RPC | Setup Dockerized Spark 3.5.1 Cluster |
| **03** | Spark Execution Architecture: Driver, Executors, Tasks, DAG scheduler | Lab 02: Spark RDD Internals & Lineage Graphs |
| **04** | Narrow vs. Wide dependencies, Shuffles, Partitions | RDD MapReduce word count and key-value pair operations |
| **05** | Introduction to PySpark DataFrames: Schemas, StructTypes | Lab 03: PySpark DataFrame Operations on Census Data |
| **06** | DataFrame transformations, actions, filter, select, withColumn | Complex nested JSON data parsing & normalization |
| **07** | Spark SQL and the Catalyst Optimizer: Logical & Physical plans | Lab 04: Catalyst Query Optimization & Broadcast Joins |
| **08** | Midterm Practical Examination | Practical coding benchmark on 50M records |
| **09** | Window functions in PySpark: rank, dense_rank, lead, lag, rolling sums | Analytical windowing on time-series telemetry |
| **10** | Advanced Join strategies: Sort-Merge vs. Broadcast Hash Joins | Optimizing skewed join keys with salting |
| **11** | Columnar file formats: Parquet, ORC, Snappy compression | Lab 05: Delta Lake Lakehouse & ACID Transactions |
| **12** | Delta Lake: Transaction logs (`_delta_log`), Time travel, vacuum, optimize | Implementing upserts (`MERGE INTO`) on administrative data |
| **13** | Tuning Spark Jobs: Dynamic allocation, executor memory, broadcast threshold | Diagnosing Spark UI event timeline and memory spills |
| **14** | Term Project Presentations & Peer Defense | Submission of Assignment 02 & Performance Review |

---

## 3. Directory Contents
* [`labs/`](labs/) - 5 Runnable laboratory exercises with unit tests.
* [`assignments/`](assignments/) - 2 Major graded assignments with rubrics.
* [`data/`](data/) - Synthetic data generators for Canadian public sector telemetry.
