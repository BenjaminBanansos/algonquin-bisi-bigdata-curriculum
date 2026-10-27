# Module 01: Protected B Sovereign Cloud Architecture & CCCS ITSG-33

* **Course:** BISI-103: Government Cloud Infrastructure & PBMM Secure Architecture
* **Estimated Workload:** 6 Hours Lecture & Independent Study | 4 Hours Hands-on Laboratory
* **Prerequisites:** Basic Cloud Concepts (AWS/Azure fundamentals), Networking basics (CIDR, DNS)
* **Instructional Design Standard:** University Postgraduate / Coursera MasterTrack Rigor

---

## 1. Module Learning Objectives (Bloom's Revised Taxonomy)

Upon successful completion of this module, students will be able to:
1. **[Bloom: Understand]** Categorize public sector data assets according to the Canadian Policy on Government Security (Unclassified, Protected A, Protected B, Protected C).
2. **[Bloom: Analyze]** Map CCCS ITSG-33 baseline security controls to automated cloud architectural implementations.
3. **[Bloom: Evaluate]** Audit cloud storage and networking boundaries to verify the absence of public ingress and compliance with Canadian sovereign data residency in `ca-central-1`.
4. **[Bloom: Create]** Author production-ready Terraform modules provisioning KMS customer-managed envelope encryption and isolated private link networks.

---

## 2. In-Depth Theoretical Lecture

### 2.1 The Protected B, Medium Integrity, Medium Availability (PBMM) Profile
Under the Government of Canada's Policy on Government Security:
* **Protected A:** Compromise causes injury to an individual, organization, or government (e.g., personal email address, date of birth).
* **Protected B:** Compromise causes **serious injury** (e.g., Social Insurance Numbers, medical records, financial tax filings, law enforcement investigative notes).
* **Protected C:** Compromise causes **extremely grave injury** (e.g., national security informant identities).

For public sector cloud deployments, Shared Services Canada (SSC) mandates the **PBMM Profile**:
1. **Data Residency:** All data at rest, data in transit, backups, and transaction logs must reside exclusively within the physical geographic boundaries of Canada (e.g., AWS `ca-central-1` or Azure `Canada Central`).
2. **Customer-Managed Cryptography:** Data must be encrypted with Customer-Managed Keys (CMK) where the government retains sole cryptographic custody of the key material via Hardware Security Modules (FIPS 140-2 Level 3).
3. **Zero Public Ingress:** Analytical clusters and databases must have **no public IP addresses** and no direct internet gateway routing. All administrative and pipeline access must occur via private endpoints (AWS PrivateLink / Azure Private Endpoints) and authenticated jump hosts.

---

## 3. Required Academic & Regulatory Literature

1. **Canadian Centre for Cyber Security (CCCS) (2017).** *ITSG-33: IT Security Risk Management: A Lifecycle Approach.* Ottawa: Government of Canada.  
   *Reading Focus:* Annex 4: "Security Control Baselines" (AC, AU, SC control families).
2. **Shared Services Canada (SSC) (2022).** *Government of Canada Cloud Security Assessment Criteria for Protected B, Medium Integrity, Medium Availability.*

---

## 4. Formative Self-Assessment Quiz

### Question 1
Why does CCCS Guardrail #1 strictly prohibit using default cloud-provider managed encryption keys (e.g., `aws/s3`) for Protected B administrative data?
* A) Cloud-provider keys do not support AES-256 encryption.
* B) The cloud service provider retains access to the root key material, violating the sovereign requirement that the Government of Canada retain exclusive cryptographic control and key revocation authority.
* C) Cloud-provider keys expire every 24 hours.
* D) Protected B data does not require encryption.

> **Answer:** **B**  
> **Pedagogical Rationale:** Under Canadian sovereign cloud mandates, the cloud service provider must have zero technical capability to decrypt government records in response to foreign subpoenas or insider threats. Customer-Managed Keys (CMK) housed in dedicated HSMs guarantee this sovereign isolation.

---

## 5. Direct Capstone & Federal Competency Traceability

* **Connection to BISI-201 Public Sector Capstone:**  
  Mandatory for **Sprint 0 and 1**. Any capstone team that provisions a public S3 bucket or unencrypted database automatically fails the security audit checkpoint.
* **Federal Classification Competency:**  
  * **Classification:** IT-02 / IT-03 (Cloud Infrastructure & Security).
  * **Interview Drill Question:** *"Describe the architectural differences between deploying an analytics cluster under Commercial Standard vs. Protected B (PBMM) in the Government of Canada."*
