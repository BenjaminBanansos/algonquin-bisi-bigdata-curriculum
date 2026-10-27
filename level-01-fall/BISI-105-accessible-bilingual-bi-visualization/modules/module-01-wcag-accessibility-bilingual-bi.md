# Module 01: Accessible & Bilingual BI Visualization (WCAG 2.1 AA & Official Languages)

* **Course:** BISI-105: Accessible & Bilingual BI Visualization (Power BI / WCAG 2.1 AA)
* **Estimated Workload:** 6 Hours Lecture & Independent Study | 4 Hours Hands-on Laboratory
* **Prerequisites:** Foundational Data Visualization concepts
* **Instructional Design Standard:** University Postgraduate / Coursera MasterTrack Rigor

---

## 1. Module Learning Objectives (Bloom's Revised Taxonomy)

Upon successful completion of this module, students will be able to:
1. **[Bloom: Understand]** Apply the Treasury Board Standard on Web Accessibility and W3C WCAG 2.1 Level AA mandates to executive BI dashboards.
2. **[Bloom: Analyze]** Audit visual interfaces for screen-reader readability, keyboard focus order, and contrast compliance (>4.5:1 ratio).
3. **[Bloom: Apply]** Implement dynamic localized DAX measure switching enabling single-click English and French language parity.
4. **[Bloom: Create]** Author automated narrative alt-text DAX expressions summarizing visual statistical anomalies for non-sighted users.

---

## 2. In-Depth Theoretical Lecture

### 2.1 Legal & Human Rights Mandate in Public Sector Analytics
In Canadian public administration, business intelligence dashboards are not merely internal tools—they are instruments of public accountability. Under the **Canadian Human Rights Act**, the **Accessible Canada Act**, and the **Official Languages Act**:
* Dashboards must be accessible to individuals with visual, motor, or cognitive disabilities.
* Dashboards published by federal institutions must provide simultaneous, functionally equivalent availability in both official languages (English and French).

### 2.2 Technical Implementation of WCAG 2.1 Level AA in Power BI
1. **Keyboard Focus Tab Order:** Sighted users navigate with a mouse, but motor-impaired or blind users navigate via keyboard `Tab` strokes. Analysts must manually set the visual tab order in the Power BI Selection Pane:
   $$	ext{Filter Slicers} \longrightarrow 	ext{KPI Cards} \longrightarrow 	ext{Primary Trend Charts} \longrightarrow 	ext{Detailed Data Table}$$
2. **Color Contrast:** Foreground text and interactive graphic elements must maintain a contrast ratio of at least **4.5:1** against the background canvas (3:1 for large graphical components).
3. **Screen Reader Narrative Alt-Text:** Sighted users perceive visual trends at a glance. Screen-reader users require dynamic verbal alt-text. Analysts construct DAX measures that evaluate live metrics and synthesize contextual sentences:
   ```dax
   Dynamic_Alt_Text = 
   "Bar chart showing expenditures across 5 departments. Highest spending is in Public Works at " & 
   FORMAT([Max_Spending], "$#,##0") & ", reflecting a 12 percent increase over prior period."
   ```

---

## 3. Required Academic & Regulatory Literature

1. **Treasury Board of Canada Secretariat (2013, amended 2021).** *Standard on Web Accessibility.* Ottawa: Government of Canada.
2. **W3C (2018).** *Web Content Accessibility Guidelines (WCAG) 2.1.* World Wide Web Consortium Recommendation.
3. **Tufte, E. R. (2001).** *The Visual Display of Quantitative Information.* Graphics Press.

---

## 4. Formative Self-Assessment Quiz

### Question 1
Why is it insufficient to rely on automatic browser translation (e.g., Google Translate) for public sector reporting dashboards instead of engineering tabular model translations?
* A) Automatic translations change the underlying numerical data values.
* B) Machine translations often misinterpret specialized Canadian legislative and fiscal terminology (e.g., translating "Estimates" or "Vote 1 Operating Expenditures" incorrectly) and violate the Official Languages Act standard of equal institutional quality.
* C) Power BI blocks external translation tools.
* D) French text requires more disk storage than English text.

> **Answer:** **B**  
> **Pedagogical Rationale:** Federal guidelines require certified official bilingual terminology. Tabular model localization (via Tabular Editor and bilingual DAX measures) ensures that vetted, official government translations are displayed accurately.

---

## 5. Direct Capstone & Federal Competency Traceability

* **Connection to BISI-201 Public Sector Capstone:**  
  In **Sprint 3**, all capstone projects undergo an official accessibility review using NVDA screen-reading tools and colorblind filters.
* **Federal Classification Competency:**  
  * **Classification:** IT-01 / EC-02 (BI Developer / Visual Analytics Specialist).
  * **Interview Drill Question:** *"Walk me through the technical steps you take to ensure a Power BI report satisfies WCAG 2.1 Level AA and bilingual language requirements."*
