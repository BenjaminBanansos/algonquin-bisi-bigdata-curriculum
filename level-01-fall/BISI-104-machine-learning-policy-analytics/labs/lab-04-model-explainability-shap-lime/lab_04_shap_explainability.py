"""
BISI-104: Lab 04 - Explainable AI (XAI) using SHAP on Public Service Grant Approvals
Author: Algonquin College Business Intelligence & Big Data Faculty

Objectives:
1. Train a Gradient Boosted Classifier (XGBoost) on synthetic public grant approval data.
2. Compute exact TreeSHAP values to quantify feature contribution per applicant.
3. Generate global feature importance beeswarm plots and local decision force plots.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import shap

def generate_grant_data(n: int = 5000):
    np.random.seed(42)
    data = {
        "annual_revenue": np.random.lognormal(mean=12.0, sigma=1.0, size=n),
        "years_in_operation": np.random.randint(1, 25, size=n),
        "employee_count": np.random.randint(1, 200, size=n),
        "prior_grants_received": np.random.poisson(lam=1.5, size=n),
        "debt_to_equity_ratio": np.random.uniform(0.1, 4.0, size=n),
        "has_community_partnership": np.random.choice([0, 1], size=n, p=[0.4, 0.6])
    }
    df = pd.DataFrame(data)
    
    # Latent approval probability logic
    logit = (
        0.000005 * df["annual_revenue"]
        + 0.12 * df["years_in_operation"]
        + 0.02 * df["employee_count"]
        + 0.45 * df["prior_grants_received"]
        - 0.8 * df["debt_to_equity_ratio"]
        + 0.7 * df["has_community_partnership"]
        - 2.5
    )
    prob = 1 / (1 + np.exp(-logit))
    df["grant_approved"] = (prob > 0.5).astype(int)
    return df

def train_and_explain():
    df = generate_grant_data(5000)
    X = df.drop(columns=["grant_approved"])
    y = df["grant_approved"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train XGBoost Model
    print("Training XGBoost Classifier on public grant applicants...")
    model = XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.05, random_state=42)
    model.fit(X_train, y_train)

    # Compute SHAP Values
    print("Computing TreeSHAP values for algorithmic explainability...")
    explainer = shap.TreeExplainer(model)
    shap_values = explainer(X_test)

    # Print mean absolute SHAP contribution (Global feature importance)
    mean_abs_shap = np.abs(shap_values.values).mean(axis=0)
    importance_df = pd.DataFrame({
        "feature": X.columns,
        "mean_abs_shap": mean_abs_shap
    }).sort_values(by="mean_abs_shap", ascending=False)

    print("\n--- Global Algorithmic Feature Importance (SHAP) ---")
    print(importance_df.to_string(index=False))

    # Explain single applicant (Applicant #0)
    print(f"\nExplaining Decision for Test Applicant #0 (Actual: {y_test.iloc[0]}):")
    for feat, val, s_val in zip(X.columns, X_test.iloc[0], shap_values.values[0]):
        impact = "Increased Approval" if s_val > 0 else "Decreased Approval"
        print(f"  - {feat} = {val:.2f} -> SHAP value: {s_val:+.4f} ({impact})")

if __name__ == "__main__":
    train_and_explain()
    print("\nLab 04 explainability audit completed.")
