# Master Academic Bibliography & Regulatory Authoritative Sources

This curriculum is rigorously anchored in peer-reviewed computer science literature, industry-defining reference texts, and official regulatory frameworks of the Government of Canada.

---

## 1. Foundational Computer Science & Distributed Systems Literature

1. **Zaharia, M., Chowdhury, M., Franklin, M. J., Shenker, S., & Stoica, I. (2010).**  
   *Spark: Cluster Computing with Working Sets.* In Proceedings of the 2nd USENIX Conference on Hot Topics in Cloud Computing (HotCloud'10), pp. 10–17.  
   *Curricular Application:* Forms the theoretical foundation for `BISI-101` and `BISI-202`. Establishes Resilient Distributed Datasets (RDDs), lineage graphs, and memory-centric computing compared to MapReduce disk-bound models.

2. **Armbrust, M., Xin, R. S., Lian, C., Huai, Y., Liu, D., Bradley, J. K., Meng, X., Kaftan, T., Franklin, M. J., Ghodsi, A., & Zaharia, M. (2015).**  
   *Spark SQL: Relational Data Processing in Spark.* In Proceedings of the 2015 ACM SIGMOD International Conference on Management of Data, pp. 1383–1394.  
   *Curricular Application:* Direct study in `BISI-101` Module 2 and `BISI-106`. Explores Catalyst optimizer rules (analysis, logical optimization, physical planning, code generation) and Tungsten execution memory layouts.

3. **Armbrust, M., Ghodsi, A., Xin, R., & Zaharia, M. (2020).**  
   *Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics.* In Proceedings of CIDR 2021 (Conference on Innovative Data Systems Research).  
   *Curricular Application:* Core reading for `BISI-106` and `BISI-203`. Establishes the Medallion Architecture (Bronze, Silver, Gold), ACID transactions over cloud object storage, and decoupled compute/storage economics.

4. **Armbrust, M., Das, T., Sun, S., Yavuz, B., Zhu, S., Murthy, M., Torres, J., van Hovell, H., Ionescu, V., Luszczak, A., & Zaharia, M. (2020).**  
   *Delta Lake: High-Performance ACID Table Storage over Cloud Object Stores.* Proceedings of the VLDB Endowment, 13(12), pp. 3411–3424.  
   *Curricular Application:* Core text for `BISI-101` Lab 5 and `BISI-203`. Details write-ahead transaction logs (`_delta_log`), optimistic concurrency control, and parquet compaction.

5. **Kleppmann, M. (2017).**  
   *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems.* Sebastopol, CA: O'Reilly Media. ISBN: 978-1449373320.  
   *Curricular Application:* Required textbook across `BISI-101`, `BISI-102`, `BISI-202`, and `BISI-204`. Chapters 1–3 (Reliability, Scalability, Storage Engines), Chapter 7 (Transactions & ACID Isolation Levels), Chapter 10 (Batch Processing), Chapter 11 (Stream Processing & Event Sourcing).

6. **Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020).**  
   *Database System Concepts* (7th Edition). New York: McGraw-Hill. ISBN: 978-0078022159.  
   *Curricular Application:* Theoretical reference for `BISI-102`. Chapters 14–16 on Query Processing, Query Optimization, and B+Tree / Hashing index access paths.

7. **Kimball, R., & Ross, M. (2013).**  
   *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling* (3rd Edition). Indianapolis, IN: John Wiley & Sons. ISBN: 978-1118530801.  
   *Curricular Application:* Applied in `BISI-105` and `BISI-106`. Star schemas, snowflake schemas, conformed dimensions, surrogate keys, and slowly changing dimensions (SCD Types 1, 2, and 3).

8. **Linstedt, D., & Olschimke, M. (2015).**  
   *Building a Scalable Data Warehouse with Data Vault 2.0.* Waltham, MA: Morgan Kaufmann. ISBN: 978-0128025109.  
   *Curricular Application:* Required for `BISI-204`. Hubs, Links, Satellites, hash-key generation, and continuous auditable schema evolution for public administration registries.

9. **Dehghani, Z. (2022).**  
   *Data Mesh: Delivering Data-Driven Value at Scale.* Sebastopol, CA: O'Reilly Media. ISBN: 978-1492092391.  
   *Curricular Application:* Required for `BISI-204`. Four principles: Domain ownership, Data as a Product, Self-serve data platform, Federated computational governance.

10. **DAMA International (2017).**  
    *DAMA-DMBOK: Data Management Body of Knowledge* (2nd Edition). Basking Ridge, NJ: Technics Publications.  
    *Curricular Application:* Standard for `BISI-204` Master Data Management, metadata management, and enterprise data quality dimensions.

11. **Tufte, E. R. (2001).**  
    *The Visual Display of Quantitative Information* (2nd Edition). Cheshire, CT: Graphics Press.  
    *Curricular Application:* Required reading for `BISI-105`. Data-ink ratio, graphical integrity, elimination of chartjunk, and visual narrative structure for policy makers.

12. **Lundberg, S. M., & Lee, S. I. (2017).**  
    *A Unified Approach to Interpreting Model Predictions.* In Advances in Neural Information Processing Systems (NeurIPS 2017), 30, pp. 4765–4774.  
    *Curricular Application:* Required for `BISI-104` and `BISI-205`. Game-theoretic Shapley values (SHAP) for transparent algorithmic decision-making in public administration.

---

## 2. Government of Canada & Canadian Regulatory Standards

1. **Treasury Board of Canada Secretariat (TBS) (2023).**  
   *Policy on Service and Digital.* Ottawa: Her Majesty the Queen in Right of Canada.  
   *Focus:* Mandatory requirements for chief data officers, open data by default, client-centric design, and digital service standards.

2. **Treasury Board of Canada Secretariat (TBS) (2023).**  
   *Directive on Automated Decision-Making* (Version 4.0). Ottawa: Government of Canada.  
   *Focus:* Mandatory Algorithmic Impact Assessments (AIA Levels I–IV), human-in-the-loop requirements, explainability, and bias auditing for automated public policy systems.

3. **Privy Council Office & Treasury Board Secretariat (2023).**  
   *Canada's 2023–2026 Data Strategy for the Federal Public Service.* Government of Canada.  
   *Focus:* Four pillars: Data for public good, Data governance, Data literacy and talent, and Modern data infrastructure.

4. **Canadian Centre for Cyber Security (CCCS) (2017).**  
   *ITSG-33: IT Security Risk Management: A Lifecycle Approach.* Ottawa: Communications Security Establishment.  
   *Focus:* Baseline security controls catalog, security categorization (Protected A, B, C), and operational risk mitigation for analytics infrastructure.

5. **Shared Services Canada (SSC) (2022).**  
   *Government of Canada Cloud Security Assessment and Authorization (CSAA) - Protected B, Medium Integrity, Medium Availability (PBMM) Profile.*  
   *Focus:* Mandatory cloud broker guardrails, tenant isolation, KMS customer-managed key encryption, and Canadian sovereign data residency in `ca-central-1`.

6. **Treasury Board of Canada Secretariat (2013, amended 2021).**  
   *Standard on Web Accessibility.* Ottawa: Government of Canada. Incorporating:  
   *World Wide Web Consortium (W3C) (2018).* *Web Content Accessibility Guidelines (WCAG) 2.1.* W3C Recommendation.  
   *Focus:* Strict adherence to Level AA compliance across executive dashboards, keyboard tab navigation, high-contrast color schemes, and non-visual screen-reader narratives.

7. **Parliament of Canada (1985, updated 2023).**  
   *Official Languages Act (R.S.C., 1985, c. 31 (4th Supp.)). Act current to 2024.*  
   *Focus:* Section IV and VII mandates on equal status of English and French in federal communications, digital portals, and data disclosures.

8. **Office of the Privacy Commissioner of Canada (OPC) & Statistics Canada (2022).**  
   *Joint Guidelines on Methods for De-identification of Personal Information in Administrative Data.*  
   *Focus:* Practical protocols for $k$-anonymity, $l$-diversity, differential privacy, and re-identification risk management for open data releases.
