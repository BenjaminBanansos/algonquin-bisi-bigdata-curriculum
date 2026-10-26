# BISI-105: Accessible & Bilingual BI Visualization (Power BI / WCAG 2.1 AA)

* **Course Code:** BISI-105
* **Contact Hours:** 42.0 Hours (3.0 hrs/week × 14 weeks)
* **Delivery Mode:** Visualization Studio / Lab
* **Prerequisites:** Admission to Program

---

## 1. Course Description
Focuses on enterprise visual analytics and executive dashboard storytelling in Microsoft Power BI and Tableau. Tailored to Canadian federal and provincial public administration, this course emphasizes:
1. **WCAG 2.1 Level AA Accessibility Compliance:** Keyboard-only tab order, screen-reader narrative alt-text, contrast ratios (>4.5:1), and color-blind safe palettes.
2. **Dynamic Bilingualism (Official Languages Act):** Creating single-report architectures that switch dynamically between English and French across titles, axes, tooltips, and data dictionaries using Tabular Editor and DAX measures.
3. **Enterprise Data Modeling:** Dimensional star schemas, granular row-level security (RLS), and DAX time-intelligence on Canadian fiscal calendar years (April 1 to March 31).

---

## 2. Weekly Syllabus

| Week | Lecture Topics | Laboratory Work |
| :---: | :--- | :--- |
| **01** | Visual perception theory, Gestalt principles, Edward Tufte guidelines | Designing clean KPI layouts for executive oversight |
| **02** | Power BI Desktop Architecture: Storage modes (Import vs. DirectQuery) | Configuring Power Query (M) transformations |
| **03** | Dimensional Modeling for BI: Fact tables, Conformed dimensions, Star schemas | Lab 01: Star Schema Design & Relationship Validation |
| **04** | Introduction to DAX: Evaluation context (Row vs. Filter context) | Writing scalar measures: `SUM`, `DIVIDE`, `COUNTROWS` |
| **05** | The `CALCULATE` function: Context transition, modifying filter context | Computing multi-departmental baseline shares |
| **06** | DAX Time Intelligence: Canadian Federal Fiscal Calendar (Apr 1 - Mar 31) | Lab 02: Advanced DAX Fiscal Year Metrics (FY-YTD, YoY) |
| **07** | Government Accessibility Mandate: Standard on Web Accessibility | Auditing color contrast against WCAG 2.1 AA benchmarks |
| **08** | Keyboard Navigation & Screen Readers: Focus order, Alt-text, smart narratives | Lab 03: WCAG 2.1 AA Tab-Order & Screen-Reader Hardening |
| **09** | Official Languages Act (OLA) in Digital Products: Equal Status (FR/EN) | Designing localized multilingual data dictionaries |
| **10** | Tabular Model Localization: Tabular Editor translations and cultures | Lab 04: Dynamic Bilingual Dashboard Localization |
| **11** | Dynamic DAX Measure Switching: Parameter tables for language selection | Building language-aware measure titles and axis labels |
| **12** | Enterprise Security: Row-Level Security (RLS) & Object-Level Security (OLS) | Configuring departmental access roles in Power BI Service |
| **13** | Deployment Pipelines: Development, Test, Production workspaces in Power BI | Automating dataset refreshes with On-Premises Data Gateways |
| **14** | Final Bilingual Dashboard Defense & Usability Walkthrough | Presentation of Assignment 01 Public Sector Portal |

---

## 3. Directory Contents
* [`templates-and-dax/`](templates-and-dax/) - Reusable DAX bilingual functions and GC Accessible theme JSON.
* [`labs/`](labs/) - 4 Interactive dashboard engineering labs.
* [`assignments/`](assignments/) - Major bilingual accessible dashboard capstone.
