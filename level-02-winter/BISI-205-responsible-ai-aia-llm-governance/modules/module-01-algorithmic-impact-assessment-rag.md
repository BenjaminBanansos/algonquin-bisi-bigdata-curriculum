# Module 01: Treasury Board Algorithmic Impact Assessment (AIA) & Private RAG

* **Course:** BISI-205: ML 2: TBS Algorithmic Impact Assessment, Responsible AI & LLMs
* **Estimated Workload:** 6 Hours Lecture & Independent Study | 4 Hours Hands-on Laboratory
* **Prerequisites:** BISI-104 (Machine Learning 1)
* **Instructional Design Standard:** University Postgraduate / Coursera MasterTrack Rigor

---

## 1. Module Learning Objectives (Bloom's Revised Taxonomy)

Upon successful completion of this module, students will be able to:
1. **[Bloom: Understand]** Deconstruct the Treasury Board Secretariat Directive on Automated Decision-Making and its 4 Impact Levels.
2. **[Bloom: Evaluate]** Calculate system risk scores based on raw decision reversibility, client vulnerability, and demographic impact.
3. **[Bloom: Apply]** Integrate Microsoft Presidio PII sanitization pipelines to scrub sensitive personal identifiers prior to vector embedding.
4. **[Bloom: Create]** Build a private, sovereign Retrieval-Augmented Generation (RAG) assistant querying federal policy repositories with deterministic citations.

---

## 2. In-Depth Theoretical Lecture

### 2.1 The Treasury Board Directive on Automated Decision-Making
Effective since 2019 and revised regularly, this directive governs any artificial intelligence system used by the Government of Canada to support or make administrative decisions impacting the rights, liberties, or benefits of individuals.

The directive establishes four **Impact Levels**:
* **Level I (Reversible / Low Impact):** e.g., Automated internal document routing. Requires basic testing.
* **Level II (Moderate Impact):** e.g., Grant eligibility pre-screening. Requires human-in-the-loop oversight and peer-reviewed testing.
* **Level III (High Impact):** e.g., Tax audit selection, immigration application triage. Requires published explanations and external third-party audits.
* **Level IV (Critical / Irreversible Impact):** e.g., Public safety or border security decisions. Requires full transparent algorithm disclosure and Deputy Minister sign-off.

### 2.2 Sovereign Private RAG with PII Guardrails
Deploying Large Language Models in government requires preventing **data leakage** and **hallucinations**:
```
User Query (e.g. "Can I claim child care benefits?")
           |
           v
[PII Scrubbing Pipeline (Presidio)] -> Redacts SIN, Names, Addresses
           |
           v
[Vector Database (Chroma / pgvector)] -> Similarity Search on Hardened Policy Embeddings
           |
           v
[Prompt Guardrail + LLM] -> "Answer strictly using provided excerpts. Cite Section #."
           |
           v
Audited Response with Direct Legislative Footnotes
```

---

## 3. Required Academic & Regulatory Literature

1. **Treasury Board of Canada Secretariat (2023).** *Directive on Automated Decision-Making.* Version 4.0. Ottawa: Government of Canada.
2. **Lundberg, S. M., & Lee, S. I. (2017).** *A Unified Approach to Interpreting Model Predictions.* NeurIPS 2017.
3. **Office of the Privacy Commissioner of Canada (2022).** *Principles for Responsible and Trustworthy AI.*

---

## 4. Formative Self-Assessment Quiz

### Question 1
Under the TBS Directive on Automated Decision-Making, what happens if an AI system is classified at Impact Level III?
* A) The system cannot be deployed under any circumstances.
* B) The department must ensure a human decision-maker makes the final decision, publish a plain-language explanation of how the system works on Canada.ca, and conduct regular bias testing on vulnerable populations.
* C) The department can use the model without logging user interactions.
* D) Only private contractors may operate the system.

> **Answer:** **B**  
> **Pedagogical Rationale:** Level III mandates meaningful human-in-the-loop oversight, mandatory public disclosure, detailed documentation of data sources, and recurring bias/fairness reviews.

---

## 5. Direct Capstone & Federal Competency Traceability

* **Connection to BISI-201 Public Sector Capstone:**  
  In **Sprint 4**, every student team must submit a signed, complete Algorithmic Impact Assessment (AIA) accompanying their analytical models.
* **Federal Classification Competency:**  
  * **Classification:** IT-02 / EC-04 (Data Scientist / Policy Modeler).
  * **Interview Drill Question:** *"Under the TBS Directive on Automated Decision-Making, how do you determine if a model requires human-in-the-loop intervention versus fully autonomous decisioning?"*
