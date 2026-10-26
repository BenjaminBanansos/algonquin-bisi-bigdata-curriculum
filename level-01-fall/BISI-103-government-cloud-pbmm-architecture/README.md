# BISI-103: Government Cloud Infrastructure & PBMM Secure Architecture

* **Course Code:** BISI-103
* **Contact Hours:** 56.0 Hours (4.0 hrs/week × 14 weeks)
* **Delivery Mode:** Cloud Sandbox / Architectural Lab
* **Prerequisites:** Admission to Program

---

## 1. Course Description
Explores enterprise cloud computing within the Government of Canada governance framework. Covers Shared Services Canada (SSC) cloud brokerage guidelines, the Canadian Centre for Cyber Security (CCCS) ITSG-33 baseline security controls, and **Protected B, Medium Integrity, Medium Availability (PBMM)** architecture. Students deploy automated, secure infrastructure using **Terraform (IaC)** in AWS and Azure Canada Central sovereign cloud regions.

---

## 2. Weekly Syllabus

| Week | Lecture Topics | Laboratory Work |
| :---: | :--- | :--- |
| **01** | GC Cloud Adoption Strategy, Sovereign data residency, CCCS ITSG-33 | Setup AWS & Azure Canada Central CLI environments |
| **02** | Security Categorization: Unclassified, Protected A, Protected B, Protected C | Mapping data classifications to technical security controls |
| **03** | Cloud Networking 1: VPCs/VNets in `ca-central-1`, Private vs Public subnets | Lab 01: Sovereign VPC Architecture & Zero-Ingress Subnets |
| **04** | Cloud Networking 2: VPC Peering, Transit Gateways, PrivateLink endpoints | Routing analytics traffic through private network backbones |
| **05** | Identity & Access Management (IAM): Least Privilege, Role federation | Configuring IAM Roles, Instance Profiles, and SCIM Sync |
| **06** | Cryptography in the Cloud: KMS, Envelope Encryption, Customer-Managed Keys (CMK) | Lab 02: KMS Envelope Encryption on Protected B Data |
| **07** | Storage Security: S3 Bucket Policies, TLS 1.3 enforcement, Object Lock | Hardening object stores against unauthorized exfiltration |
| **08** | Infrastructure as Code (IaC) Fundamentals: Terraform architecture | Writing modular Terraform templates for cloud foundations |
| **09** | Automating PBMM Baselines with Terraform | Deploying end-to-end PBMM compliant cloud landing zones |
| **10** | Continuous Compliance Monitoring: AWS Config, Azure Policy, GuardDuty | Lab 03: Azure Policy & Automated Compliance Auditing |
| **11** | Container Security: Hardening Docker images, AWS ECR image scanning | Deploying containerized workloads on secure ECS/AKS clusters |
| **12** | Centralized Logging & Audit Trails: CloudTrail, Log Analytics, SIEM | Ingesting administrative access logs into audit dashboards |
| **13** | Disaster Recovery & High Availability: Multi-AZ failover, RTO/RPO metrics | Executing automated failover drills in Canada East/Central |
| **14** | Architecture Defense & Blueprint Evaluation | Technical defense of Assignment 01 Cloud Blueprint |

---

## 3. Directory Contents
* [`terraform/`](terraform/) - Production-ready Terraform modules for Canada Central PBMM deployment.
* [`labs/`](labs/) - 3 Hands-on security and cloud engineering labs.
* [`assignments/`](assignments/) - Major enterprise cloud migration blueprint.
