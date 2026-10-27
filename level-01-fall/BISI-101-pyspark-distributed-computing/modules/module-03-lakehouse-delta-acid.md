# Module 03: Lakehouse Architecture, Delta Lake Internals & ACID Transactions

* **Course:** BISI-101: Big Data Programming & Distributed Computing with PySpark
* **Estimated Workload:** 6 Hours Lecture & Independent Study | 4 Hours Hands-on Laboratory
* **Prerequisites:** BISI-101 Modules 01 & 02
* **Instructional Design Standard:** University Postgraduate / Coursera MasterTrack Rigor

---

## 1. Module Learning Objectives (Bloom's Revised Taxonomy)

Upon successful completion of this module, students will be able to:
1. **[Bloom: Understand]** Contrast object store eventual consistency with ACID transactional lakehouse engines (Delta Lake, Apache Iceberg).
2. **[Bloom: Analyze]** Deconstruct the Delta Lake transaction log (`_delta_log`), explain optimistic concurrency control, and trace commit conflict resolution.
3. **[Bloom: Apply]** Implement `MERGE INTO` upserts on administrative datasets while preserving snapshot historical isolation.
4. **[Bloom: Create]** Engineer automated file compaction and vacuuming routines to eliminate the "small files problem" and optimize query latency.

---

## 2. In-Depth Theoretical Lecture

### 2.1 The Fundamental Flaw of Traditional Data Lakes on Object Storage
Cloud object stores (AWS S3, Azure Blob/ADLS Gen2, MinIO) are key-value systems, not POSIX-compliant file systems. Traditional Apache Spark operations over raw Parquet/CSV files suffered from critical architectural defects:
1. **Lack of ACID Guarantees:** A failed pipeline write left half-written files in storage, causing downstream jobs to read corrupted datasets.
2. **No Concurrency Control:** Simultaneous write operations overwrote each other's data (lost updates).
3. **Expensive Metadata Operations:** Listing millions of partitioned files required linear S3 `LIST` API calls, often taking hours just to plan a query.

### 2.2 Delta Lake Transaction Log (`_delta_log`) Mechanics
Delta Lake (Armbrust et al., 2020) solves these failures by placing a **Write-Ahead Transaction Log** over Parquet files. Every transaction produces an atomic JSON commit log:
```
my_delta_table/
├── _delta_log/
│   ├── 00000000000000000000.json   <- Commit 0 (Table created, 5 Parquet files added)
│   ├── 00000000000000000001.json   <- Commit 1 (Insert 2 new Parquet files)
│   ├── 00000000000000000002.json   <- Commit 2 (Update: 1 file tombstoned, 1 new written)
│   └── 00000000000000000010.checkpoint.parquet <- Checkpoint summarizing state up to Commit 10
├── part-00000-4b2a.snappy.parquet
└── part-00001-9c8d.snappy.parquet
```

* **Optimistic Concurrency Control (OCC):** When multiple writers attempt to commit, Delta verifies whether the files modified by writer $A$ overlap with those modified by writer $B$. If no conflict exists, both commit atomically. If a conflict occurs, Delta automatically retries the operation on the newly committed snapshot.
* **Time Travel:** Readers can query the exact state of the table at any historical timestamp or commit version:
  $$	ext{SELECT * FROM table TIMESTAMP AS OF '2026-04-01'}$$

---

## 3. Required Academic Literature & Readings

1. **Armbrust, M. et al. (2020).** *Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores.* Proceedings of the VLDB Endowment, 13(12), pp. 3411–3424.  
   *Reading Focus:* Section 3 (Storage System Architecture) and Section 4 (Concurrency Control Protocol).
2. **Armbrust, M., Ghodsi, A., Xin, R., & Zaharia, M. (2021).** *Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics.* In CIDR 2021.

---

## 4. Formative Self-Assessment Quiz

### Question 1
What occurs under the hood when a Delta Lake table executes an `UPDATE` or `DELETE` statement?
* A) The underlying Parquet files are opened, modified in-place on disk, and saved back.
* B) The existing Parquet files are marked as deleted (tombstoned) in the `_delta_log` JSON commit file, and new Parquet files containing the updated rows are written to storage.
* C) The table is dropped and completely recomputed from scratch.
* D) Changes are held in RAM and never written to persistent cloud storage.

> **Answer:** **B**  
> **Pedagogical Rationale:** Cloud object storage files are immutable. Delta Lake implements Copy-on-Write (or Merge-on-Read). It writes new Parquet files containing the updated values, and records the original files as "remove" actions in the transaction log. Historical queries can still read the original files via Time Travel until `VACUUM` is executed.

---

## 5. Direct Capstone & Federal Competency Traceability

* **Connection to BISI-201 Public Sector Capstone:**  
  Forms the foundational storage architecture for **Sprint 1 (Medallion Ingestion)**. Students establish the Bronze, Silver, and Gold layers on Delta Lake with ACID rollback capabilities.
* **Federal Classification Competency:**  
  * **Classification:** IT-02 (Data Solutions Developer) / IT-03 (Data Architect).
  * **Interview Drill Question:** *"How does Delta Lake guarantee ACID compliance over non-transactional cloud storage like AWS S3 or Azure ADLS, and what happens when two pipeline tasks attempt to write simultaneously?"*
