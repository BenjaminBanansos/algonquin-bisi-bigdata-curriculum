# BISI-104: Machine Learning 1: Predictive Modeling & Policy Analytics

* **Course Code:** BISI-104
* **Contact Hours:** 56.0 Hours (4.0 hrs/week × 14 weeks)
* **Delivery Mode:** Lab-Intensive / Modeling Studio
* **Prerequisites:** Admission to Program

---

## 1. Course Description
Applies predictive modeling techniques to public administration, social program delivery, economic indicators, and fraud detection. Emphasizes the entire machine learning lifecycle: data imputation, feature engineering, cross-validation on administrative datasets, and model explainability using **SHAP (Shapley Additive exPlanations)** and **LIME**. Students evaluate models not only on standard metrics (ROC-AUC, F1-Score) but also on algorithmic fairness, disparate impact, and demographic parity across vulnerable demographic sub-cohorts.

---

## 2. Weekly Syllabus

| Week | Lecture Topics | Laboratory Work |
| :---: | :--- | :--- |
| **01** | The ML lifecycle in government: Administrative records vs. survey data | Setting up Scikit-Learn & MLflow tracking servers |
| **02** | Data Preprocessing: Imputation strategies, outlier capping, robust scaling | Lab 01: Administrative Data Cleaning & Feature Engineering |
| **03** | Categorical Encoding: One-Hot, Target encoding, Weight of Evidence (WoE) | Processing high-cardinality postal codes & industry codes |
| **04** | Linear & Logistic Regression: Assumptions, Regularization (Lasso/Ridge) | Modeling determinants of municipal transit ridership |
| **05** | Time Series Analysis in Public Policy: ARIMA, SARIMAX, Prophet | Lab 02: Macroeconomic Indicator Forecasting |
| **06** | Tree-based models: Decision Trees, Random Forests, pruning, entropy | Predicting social benefit uptake across regional offices |
| **07** | Gradient Boosted Decision Trees: XGBoost, LightGBM, CatBoost | Tuning hyperparameters via Bayesian Optimization |
| **08** | Class Imbalance in Government: Procurement fraud, tax evasion, auditing | Lab 03: Fraud Detection with Imbalanced Classification |
| **09** | Resampling strategies: SMOTE, ADASYN, Cost-sensitive loss functions | Precision-Recall curve optimization for audit selection |
| **10** | Model Explainability 1: Global vs. Local explanations, Permutation importance | Interpreting tree splits and feature correlation matrices |
| **11** | Model Explainability 2: SHAP values, Beeswarm plots, Force plots, LIME | Lab 04: Explainable AI with SHAP & Partial Dependence |
| **12** | Algorithmic Fairness: Demographic Parity, Equalized Odds, Disparate Impact | Auditing model predictions for demographic bias |
| **13** | Model Deployment: Serializing models (ONNX, joblib), REST APIs (FastAPI) | Containerizing an explainable inference microservice |
| **14** | Final Project Defense & Ethical Audit Presentations | Submission of Assignment 01 Policy Audit Model |

---

## 3. Directory Contents
* [`labs/`](labs/) - 4 Runnable Python ML labs.
* [`assignments/`](assignments/) - 1 End-to-end policy modeling project.
