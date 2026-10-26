# Capstone Client Project Briefs (Sample Public Sector Challenges)

---

### Challenge 1: Statistics Canada Economic Pulse Lakehouse
* **Sponsor:** Statistics Canada - Modernization and Data Architecture Division
* **Problem:** Ingest high-frequency alternate data (credit card aggregates, port shipping volumes, electricity grid loads) to provide real-time economic health indices preceding monthly GDP announcements.
* **Tech Stack:** PySpark, Delta Lake, dbt-core, Apache Airflow, Power BI Service.
* **Key Mandates:** Sub-second analytical queries on 100M+ rows, fully bilingual EN/FR executive dashboard.

---

### Challenge 2: Transport Canada National Autonomous Telematics Stream
* **Sponsor:** Transport Canada - Multimodal Innovation Directorate
* **Problem:** Ingest high-volume simulated connected vehicle telemetry across the Trans-Canada Highway network to detect collision clusters, icy road anomalies, and transit bottlenecks.
* **Tech Stack:** Apache Kafka, Spark Structured Streaming, PostgreSQL (PostGIS), MinIO/S3.
* **Key Mandates:** Real-time sliding window aggregations (5-min intervals) with watermarking for late-arriving packets.

---

### Challenge 3: Health Canada Adverse Drug Reaction Pharmacovigilance Hub
* **Sponsor:** Health Canada - Health Products and Food Branch
* **Problem:** Build a decentralized Data Mesh platform unifying adverse clinical drug reaction logs with social sentiment and hospital admissions while strictly protecting patient PII.
* **Tech Stack:** Data Vault 2.0, Microsoft Purview, Snowflake, Scikit-Learn (Anomaly Detection).
* **Key Mandates:** $k$-anonymity verification, RBAC multi-tenant isolation, automated PII redaction.

---

### Challenge 4: City of Ottawa Bilingual 311 Citizen Service Analytics
* **Sponsor:** City of Ottawa - Service Innovation & Performance Department
* **Problem:** Modernize the municipal 311 service request ecosystem to identify service delivery inequities across urban, suburban, and rural wards.
* **Tech Stack:** AWS Canada Central, Terraform, Power BI, Python/Statsmodels.
* **Key Mandates:** Strict WCAG 2.1 AA screen-reader compliance, open-data publishing pipeline.
