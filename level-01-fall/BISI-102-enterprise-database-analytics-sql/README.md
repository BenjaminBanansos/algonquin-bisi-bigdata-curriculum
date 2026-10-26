# BISI-102: Advanced Enterprise Database Analytics & SQL for Big Data

* **Course Code:** BISI-102
* **Contact Hours:** 70.0 Hours (5.0 hrs/week × 14 weeks)
* **Delivery Mode:** Lab-Intensive / Database Studio
* **Prerequisites:** Admission to Program

---

## 1. Course Description
Focuses on advanced relational database design, query optimization, and enterprise data security. Students implement 3NF transactional schemas and star/snowflake analytical warehouses in PostgreSQL 16. Emphasizes query execution plan analysis (`EXPLAIN ANALYZE`), indexing mechanisms (B-tree, Hash, GIN, BRIN for timeseries), window functions, recursive CTEs, and row-level security (RLS) policies mandated in public sector multi-tenant architectures.

---

## 2. Weekly Syllabus

| Week | Lecture Topics | Laboratory Work |
| :---: | :--- | :--- |
| **01** | Relational calculus, Relational engine internals, Buffer pool, WAL | Lab 01: 3NF Relational Schema Design & DDL Constraints |
| **02** | Advanced DDL: check constraints, generated columns, table inheritance | Multi-tenant schema setup with partitioning |
| **03** | Advanced SQL Aggregations: `GROUPING SETS`, `ROLLUP`, `CUBE` | Multidimensional expenditure reporting |
| **04** | SQL Window Functions 1: Over clause, Partition by, Order by | Lab 02: Analytical Window Functions (Running Totals & Rank) |
| **05** | SQL Window Functions 2: Frame specifications (`ROWS BETWEEN`), Lead, Lag | Period-over-period delta and anomaly detection |
| **06** | Recursive Common Table Expressions (CTEs) & Hierarchical Data | Modeling departmental org charts and budget rollups |
| **07** | Query Execution Engine: Parse, Rewrite, Plan, Execute | Lab 03: Query Plan Analysis & Performance Optimization |
| **08** | Indexes Deep Dive: B-Tree, BRIN, GIN, GiST, Covering indexes | Benchmarking 10M record table before/after index tuning |
| **09** | ACID Isolation Levels: Read Committed, Repeatable Read, Serializable | Simulating lost updates, dirty reads, and deadlock detection |
| **10** | Database Security & Compliance: RBAC, Grants, Principle of Least Privilege | Creating read-only auditor and data engineer roles |
| **11** | Row-Level Security (RLS) & Column-Level Encryption in PostgreSQL | Lab 04: Public Sector RLS & Multi-Department Isolation |
| **12** | Database Maintenance: Vacuuming, Autovacuum tuning, Bloat, Reindexing | Optimizing high-write transaction logs |
| **13** | Database Migration & Version Control with Liquibase / Alembic | Managing declarative schema migrations |
| **14** | Comprehensive Practical SQL Examination | 3-Hour timed database performance & security audit |

---

## 3. Directory Contents
* [`labs/`](labs/) - 4 Runnable SQL lab scripts with seed data.
* [`assignments/`](assignments/) - 2 Major database audit assignments.
