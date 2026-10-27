# Module 01: Distributed Runtime Internals, Memory Management & Execution Graphs

* **Course:** BISI-101: Big Data Programming & Distributed Computing with PySpark
* **Estimated Workload:** 6 Hours Lecture & Independent Study | 4 Hours Hands-on Laboratory
* **Prerequisites:** Python OOP, Data Structures (Hash tables, trees), Bash CLI
* **Instructional Design Standard:** University Postgraduate / Coursera MasterTrack Rigor

---

## 1. Module Learning Objectives (Bloom's Revised Taxonomy)

Upon successful completion of this module, students will be able to:
1. **[Bloom: Understand]** Contrast the distributed memory execution paradigm of Apache Spark with traditional disk-bound MapReduce architectures.
2. **[Bloom: Analyze]** Deconstruct a Spark physical execution graph into Jobs, Stages, and Tasks based on narrow versus wide transformation dependencies.
3. **[Bloom: Evaluate]** Diagnose executor memory allocation, identifying root causes of garbage collection (GC) overhead and off-heap memory spills to disk.
4. **[Bloom: Apply]** Configure custom SparkSession driver and executor configurations for high-throughput batch processing of multi-gigabyte administrative datasets.
5. **[Bloom: Create]** Construct an execution plan profiler script that programmatic parses Spark DAG metrics to alert on partition skew.

---

## 2. In-Depth Theoretical Lecture

### 2.1 The Paradigm Shift: MapReduce vs. In-Memory Resilient Distributed Datasets (RDDs)
In early distributed computing models (such as Apache Hadoop MapReduce), every iterative computation required serializing data to persistent disk storage (HDFS), performing network replication, and re-reading data from disk in subsequent stages. As demonstrated by Zaharia et al. (2010), this introduced severe performance penalties—often spending over 80% of cluster execution time on disk I/O and serialization overhead.

Apache Spark overcomes this through **Resilient Distributed Datasets (RDDs)**: immutable, partitioned collections of records that reside in cluster RAM across worker nodes. Rather than replicating data across physical disks for fault tolerance, Spark maintains a deterministic **lineage graph** (a Directed Acyclic Graph, or DAG). If a worker node crashes mid-computation, Spark does not restore from disk backups; instead, it recomputes only the lost partition from the base lineage graph.

```
Traditional MapReduce (Disk-Bound):
[Input] -> [Map] -> (Disk Write/Replication) -> (Network Shuffle) -> [Reduce] -> (Disk Write) -> [Next Map]

Apache Spark (Memory-Centric Lineage Graph):
[Input] -> [Map] -> [Filter] -> [FlatMap] === (Pipelines In-Memory) ===> [Shuffle/Reduce] -> (Delta Sink)
                    ^
                    |-- Fault Occurs: Lost partition recomputed deterministically via DAG lineage
```

### 2.2 Spark Cluster Architecture & Runtime Topology
A running Spark application comprises two distinct processes:
1. **The Driver Node:**
   * Houses the `SparkSession` and user application code.
   * Converts user transformations into a logical execution plan.
   * Invokes the **DAGScheduler**, which breaks the logical plan into discrete **Stages** at shuffle boundaries.
   * Invokes the **TaskScheduler**, which dispatches individual **Tasks** to physical worker nodes via the cluster manager (Standalone, YARN, or Kubernetes).
2. **Executor Nodes:**
   * Worker processes responsible for executing assigned tasks in parallel worker threads.
   * House execution and storage memory buffers.
   * Stream intermediate shuffle data to local block managers.

### 2.3 Narrow vs. Wide Dependencies (Shuffle Boundaries)
The fundamental determinant of Spark scalability and performance is the classification of transformations:
* **Narrow Dependencies:** Each partition of the parent RDD is used by at most one partition of the child RDD (e.g., `map()`, `filter()`, `flatMap()`). Operations execute pipelined in-memory on the same physical node without network transmission.
* **Wide Dependencies:** Multiple child partitions depend on data from across all parent partitions (e.g., `groupByKey()`, `reduceByKey()`, `join()`, `distinct()`). This triggers a **Shuffle**: data must be serialized, partitioned by hash key, written to local disk, transmitted across the physical network switch, and sorted on target executors.

### 2.4 Tungsten Engine & Project Catalyst Optimization
Modern Spark applications do not execute raw Python bytecode on distributed nodes; they execute via the **Catalyst Optimizer** and **Tungsten Execution Engine** (Armbrust et al., 2015):
* **Catalyst Optimizer:** Performs rule-based and cost-based query optimization across four stages:
  1. *Analysis:* Resolves column names and data types against the catalog.
  2. *Logical Optimization:* Applies standard relational algebra optimizations, including **Predicate Pushdown** (filtering records at the storage layer before reading into memory) and **Column Pruning** (reading only requested fields).
  3. *Physical Planning:* Generates multiple physical plans and selects the lowest estimated cost (e.g., choosing Broadcast Hash Join over Sort-Merge Join).
  4. *Code Generation (Whole-Stage Java CodeGen):* Synthesizes compact JVM bytecode collapsing entire query stages into a single optimized loop.
* **Tungsten Engine:** Bypasses Java garbage collection (GC) overhead by managing memory explicitly **off-heap** in compact binary formats. It operates directly on raw memory bytes without deserializing into heavy Java object wrappers.

---

## 3. Required Academic Literature & Readings

Students must read the following canonical papers and textbook chapters prior to attempting the laboratory:

1. **Zaharia, M. et al. (2010).** *Spark: Cluster Computing with Working Sets.* USENIX HotCloud'10.  
   *Reading Focus:* Sections 1–3. Study the formal definition of RDDs and the mathematical rationale for in-memory lineage vs. check-pointing.
2. **Armbrust, M. et al. (2015).** *Spark SQL: Relational Data Processing in Spark.* ACM SIGMOD'15, pp. 1383–1394.  
   *Reading Focus:* Section 3 (The Catalyst Optimizer) and Section 4 (Tungsten Memory Layout).
3. **Kleppmann, M. (2017).** *Designing Data-Intensive Applications.* O'Reilly Media.  
   *Reading Focus:* Chapter 10: "Batch Processing" (pp. 389–438). Compare Unix pipes, MapReduce distributed file systems, and Spark dataflow engines.

---

## 4. Formative Self-Assessment Quiz

Test your conceptual mastery. Detailed rationales are provided below each question.

### Question 1
Why does Spark evaluate transformations lazily rather than executing them immediately when invoked?
* A) Because Python is an interpreted language and cannot execute distributed code synchronously.
* B) To allow the Catalyst Optimizer to construct a global DAG, combining filters and pushing down predicates before physical execution begins.
* C) To guarantee that all data is written to disk between each line of code.
* D) To bypass the Spark Driver and dispatch tasks directly to worker threads.

> **Answer:** **B**  
> **Pedagogical Rationale:** Lazy evaluation prevents Spark from executing unoptimized intermediate steps. By accumulating transformations into a DAG, Catalyst can inspect the entire workflow, prune unused columns, push filters down to the file scan layer (predicate pushdown), and collapse multiple operations into a single whole-stage codegen loop. Option A is incorrect because Spark's engine is JVM-based; Option C is the opposite of Spark's architecture; Option D is false because the Driver is always required to construct the execution plan.

### Question 2
Under which scenario does a Spark job encounter a "Shuffle Spill (Memory)" and "Shuffle Spill (Disk)" warning in the Spark UI?
* A) When a narrow transformation like `filter()` receives null values.
* B) When executor JVM heap memory is insufficient to hold the sorted key-value pairs during a wide dependency aggregation, forcing Spark to spill partitions to temporary local disk storage.
* C) When the Driver node runs out of disk space during application startup.
* D) When data is stored in Parquet format instead of CSV format.

> **Answer:** **B**  
> **Pedagogical Rationale:** During wide operations (e.g., `groupByKey`, Sort-Merge join), executors allocate memory buffers to sort and aggregate hash partitions. When the volume of data in a partition exceeds `spark.memory.fraction`, Spark spills the excess data to the executor's local scratch disk to avoid an OutOfMemoryError (OOM). This degrades pipeline throughput by several orders of magnitude.

---

## 5. Guided Laboratory Exercise: Memory Profiling & DAG Analysis

### Objective
Create a PySpark script that builds an unoptimized query and an optimized query over 1,000,000 administrative records, inspects their physical plans (`explain(extended=True)`), and profiles execution times.

```python
"""
BISI-101: Lab 01 - Execution Plan Analysis & Memory Profiling
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import time

# 1. Initialize SparkSession with Explicit Resource Limits
spark = (
    SparkSession.builder
    .appName("BISI-101-Module01-MemoryProfiling")
    .master("local[4]")
    .config("spark.driver.memory", "2g")
    .config("spark.executor.memory", "2g")
    .config("spark.sql.shuffle.partitions", "8")
    .getOrCreate()
)

# 2. Synthesize High-Cardinality Administrative Data
print("Generating 1,000,000 administrative expenditure transactions...")
df = (
    spark.range(0, 1_000_000)
    .select(
        F.col("id").alias("transaction_id"),
        (F.col("id") % 10).alias("dept_code"),
        (F.rand(seed=42) * 10000).cast("double").alias("expenditure_amount"),
        F.when(F.rand(seed=42) > 0.5, "EN").otherwise("FR").alias("language_code")
    )
)

# 3. Inspect Physical Execution Plan (Demonstrating Catalyst Whole-Stage Codegen)
query = (
    df.filter(F.col("expenditure_amount") > 5000.0)
    .groupBy("dept_code", "language_code")
    .agg(
        F.count("transaction_id").alias("total_tx"),
        F.round(F.avg("expenditure_amount"), 2).alias("avg_tx")
    )
    .orderBy("dept_code")
)

print("\n=== CATALYST PHYSICAL EXECUTION PLAN ===")
query.explain(mode="formatted")

# 4. Measure Execution Runtime
start_time = time.time()
results = query.collect()
duration = time.time() - start_time

print(f"\nQuery executed across 8 partitions in: {duration:.4f} seconds")
print(f"Aggregated Department Rows: {len(results)}")

spark.stop()
```

---

## 6. Direct Capstone & Federal Competency Traceability

* **Connection to BISI-201 Public Sector Capstone:**  
  In **Sprint 0 and Sprint 1**, students must configure cluster sizing, executor cores, and shuffle partition counts for their client's real-world ingestion engine. Misconfigured partition numbers lead directly to cluster failure or excessive cloud costs.
* **Government of Canada Classification Competency:**  
  * **Classification:** IT-02 (Data Solutions Developer) / CS-02.
  * **Federal Merit Criteria:** *"Demonstrated experience in tuning, diagnosing, and optimizing Apache Spark distributed computing jobs processing multi-gigabyte administrative datasets."*
  * **Interview Drill Question:** *"Explain how you distinguish between narrow and wide transformations in a PySpark DAG, and what metric in the Spark UI indicates that you need to adjust `spark.sql.shuffle.partitions`?"*
