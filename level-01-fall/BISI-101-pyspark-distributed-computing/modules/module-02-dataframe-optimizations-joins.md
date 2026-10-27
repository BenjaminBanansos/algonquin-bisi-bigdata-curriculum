# Module 02: Advanced DataFrame Optimizations, Join Mechanics & Data Skew

* **Course:** BISI-101: Big Data Programming & Distributed Computing with PySpark
* **Estimated Workload:** 6 Hours Lecture & Independent Study | 4 Hours Hands-on Laboratory
* **Prerequisites:** BISI-101 Module 01 (Spark Internals)
* **Instructional Design Standard:** University Postgraduate / Coursera MasterTrack Rigor

---

## 1. Module Learning Objectives (Bloom's Revised Taxonomy)

Upon successful completion of this module, students will be able to:
1. **[Bloom: Analyze]** Deconstruct physical join mechanics (Broadcast Hash Join, Shuffle Hash Join, Sort-Merge Join) to evaluate time and space complexity.
2. **[Bloom: Evaluate]** Detect data skew in distributed partitions using executor task duration histograms and summary statistics.
3. **[Bloom: Apply]** Implement key salting techniques to redistribute skewed join keys evenly across cluster worker nodes.
4. **[Bloom: Create]** Design high-performance analytical windowing workflows calculating multi-period moving averages and running balances.

---

## 2. In-Depth Theoretical Lecture

### 2.1 The Mathematics of Distributed Joins
When joining two distributed datasets ($R$ and $S$) with $|R| = M$ and $|S| = N$ rows, distributed architectures must ensure that records sharing the same join key reside on the same physical worker node:

| Join Algorithm | Mechanism | Time Complexity | Network Overhead | Best Applicable Scenario |
| :--- | :--- | :---: | :---: | :--- |
| **Broadcast Hash Join (BHJ)** | Copies the smaller table entirely to every worker node; probe table is scanned locally without shuffling. | $O(M + N)$ | Minimal ($O(N)$ broadcast once) | One table is small ($< 10$ MB default, or configured up to $1$ GB). |
| **Shuffle Hash Join (SHJ)** | Hashes both tables by join key and shuffles matching partitions; builds in-memory hash table for each partition. | $O(M + N)$ | High (Full network shuffle of $R$ and $S$) | Tables are large, but individual partitions fit in worker RAM. |
| **Sort-Merge Join (SMJ)** | Hashes both tables, shuffles partitions, sorts keys on disk/memory, and merges sorted streams. | $O(M \log M + N \log N)$ | High (Full network shuffle + local sort) | Default engine join for very large datasets that exceed executor memory. |

```
Broadcast Hash Join (Zero Shuffle on Big Table):
Driver Node ---> [Small Dimension Table (10 MB)] 
                      |
                      v (Broadcasted across cluster network once)
Worker 1: [Big Partition 1] <--- In-Memory Lookup Hash Table
Worker 2: [Big Partition 2] <--- In-Memory Lookup Hash Table
Worker 3: [Big Partition 3] <--- In-Memory Lookup Hash Table
```

### 2.2 The Data Skew Bottleneck & The Salting Remediation
In public sector administrative datasets, data is rarely uniformly distributed. For example, in federal procurement records, 70% of all national spending may be concentrated in a single department code (`PWGSC`), or in tax filings, a single postal area may represent millions of filings.

When performing a standard join or aggregation on a skewed key, Spark hashes identical keys to the **same executor partition**. While 9 out of 10 workers complete their tasks in 10 seconds, the single worker assigned the skewed key runs out of memory or takes 45 minutes to finish, straggling the entire application.

#### Mathematical Salting Formula:
To resolve data skew:
1. Append an artificial random integer salt $s \in [0, K-1]$ to the skewed key of the large table:
   $$	ext{Key}_{	ext{salted}} = 	ext{Concat}(	ext{OriginalKey}, 	ext{"\_"}, 	ext{Random}(0, K-1))$$
2. Replicate the lookup dimension table rows $K$ times, once for every possible salt value $k \in [0, K-1]$:
   $$	ext{DimensionRow}_{	ext{replicated}} = (	ext{Concat}(	ext{OriginalKey}, 	ext{"\_"}, k), 	ext{Attributes})$$
3. Join on $	ext{Key}_{	ext{salted}}$. The skewed data is now divided evenly across $K$ separate physical partitions, restoring parallel execution!

---

## 3. Required Academic Literature & Readings

1. **Armbrust, M. et al. (2015).** *Spark SQL: Relational Data Processing in Spark.* ACM SIGMOD'15.  
   *Reading Focus:* Section 3.2 on Join strategies and cost-based plan generation.
2. **Kleppmann, M. (2017).** *Designing Data-Intensive Applications.* O'Reilly Media.  
   *Reading Focus:* Chapter 10, "MapReduce Workflows: Handling Skewed Data and Hotspots" (pp. 407–412).

---

## 4. Formative Self-Assessment Quiz

### Question 1
Under what conditions will Spark automatically choose a **Broadcast Hash Join (BHJ)** over a **Sort-Merge Join (SMJ)**?
* A) Whenever the join is performed on a string column.
* B) When the estimated size of one of the participating tables is smaller than the threshold defined by `spark.sql.autoBroadcastJoinThreshold` (default 10 MB).
* C) Only when the user explicitly provides an SQL hint `/*+ MERGE() */`.
* D) When both tables have identical primary keys.

> **Answer:** **B**  
> **Pedagogical Rationale:** The Catalyst cost-based planner checks table statistics. If the relation size is below `spark.sql.autoBroadcastJoinThreshold`, it automatically avoids the expensive shuffle and broadcast copies the relation to all worker nodes.

---

## 5. Guided Laboratory Exercise: Salting Skewed Keys

```python
"""
BISI-101: Lab 02 - Remediating Data Skew via Key Salting
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("BISI-101-Module02-Salting").master("local[4]").getOrCreate()

# 1. Synthesize Skewed Dataset (90% of rows have dept_code = 'PWGSC')
skewed_data = (
    spark.range(0, 500_000)
    .select(
        F.when(F.rand() < 0.90, "PWGSC").otherwise("STATCAN").alias("dept_code"),
        (F.rand() * 1000).alias("amount")
    )
)

# 2. Add Salt (0 to 3) to the Skewed Big Table
SALT_FACTOR = 4
salted_big_df = skewed_data.withColumn("salt", (F.rand() * SALT_FACTOR).cast("int")).withColumn(
    "salted_key", F.concat_ws("_", F.col("dept_code"), F.col("salt"))
)

# 3. Replicate Dimension Reference Table with all Salts (0..3)
dept_dim = spark.createDataFrame([
    ("PWGSC", "Public Services and Procurement Canada"),
    ("STATCAN", "Statistics Canada")
], ["dept_code", "dept_name"])

salt_df = spark.range(0, SALT_FACTOR).select(F.col("id").alias("salt"))
replicated_dim = dept_dim.crossJoin(salt_df).withColumn(
    "salted_key", F.concat_ws("_", F.col("dept_code"), F.col("salt"))
)

# 4. Perform Balanced Join with Zero Skew
balanced_joined_df = salted_big_df.join(replicated_dim, on="salted_key", how="inner")
print(f"Balanced Join Completed: {balanced_joined_df.count()} rows processed without executor stragglers.")

spark.stop()
```

---

## 6. Direct Capstone & Federal Competency Traceability

* **Connection to BISI-201 Public Sector Capstone:**  
  In **Sprint 2 (Core ELT Transformations)**, capstone teams must join massive transaction logs against small agency reference lookups. Employing Broadcast joins and key salting is a graded evaluation criterion in the Capstone Code Audit.
* **Federal Classification Competency:**  
  * **Classification:** IT-02 (Senior Data Solutions Engineer) / EC-04.
  * **Interview Drill Question:** *"In a Spark pipeline with 100 million records, 80% belong to one customer. How do you prevent this single key from bottlenecking the cluster during an aggregation?"*
