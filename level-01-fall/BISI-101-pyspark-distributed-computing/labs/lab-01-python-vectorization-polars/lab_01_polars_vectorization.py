"""
BISI-101: Lab 01 - High-Performance Python & Vectorization with Polars
Author: Algonquin College Business Intelligence & Big Data Faculty

Objectives:
1. Compare memory allocation between Pandas 2.x and Polars on 1,000,000 records.
2. Demonstrate lazy execution and query optimization using Polars LazyFrame.
3. Write vectorized aggregation logic on synthetic Canadian municipal expenditure data.
"""

import time
import polars as pl
import numpy as np

def generate_synthetic_budget_data(rows: int = 1_000_000) -> pl.DataFrame:
    """Generates synthetic public sector municipal expenditure transactions."""
    np.random.seed(42)
    departments = ["Health", "Transportation", "Public Safety", "Parks & Rec", "Treasury"]
    
    print(f"Generating {rows:,} synthetic government expenditure records...")
    data = {
        "transaction_id": np.arange(1, rows + 1),
        "department": np.random.choice(departments, size=rows),
        "amount": np.random.exponential(scale=5000.0, size=rows).round(2),
        "fiscal_year": np.random.choice([2024, 2025, 2026], size=rows),
        "is_audited": np.random.choice([True, False], size=rows, p=[0.05, 0.95])
    }
    return pl.DataFrame(data)

def benchmark_polars_lazy(df: pl.DataFrame):
    """Executes query using Polars LazyFrame and measures processing duration."""
    print("\n--- Polars Lazy Evaluation Benchmark ---")
    start_time = time.time()
    
    # Define execution graph without evaluating
    lazy_query = (
        df.lazy()
        .filter(pl.col("amount") > 1000.0)
        .group_by(["department", "fiscal_year"])
        .agg([
            pl.count().alias("transaction_count"),
            pl.col("amount").sum().alias("total_expenditure"),
            pl.col("amount").mean().alias("avg_expenditure"),
            pl.col("is_audited").sum().alias("audited_count")
        ])
        .sort(["fiscal_year", "total_expenditure"], descending=[False, True])
    )
    
    print("Execution Plan:")
    print(lazy_query.explain())
    
    # Materialize results
    results = lazy_query.collect()
    duration = time.time() - start_time
    
    print(f"Polars Lazy Pipeline executed in: {duration:.4f} seconds")
    print(results)
    return results

if __name__ == "__main__":
    df = generate_synthetic_budget_data(1_000_000)
    benchmark_polars_lazy(df)
    print("\nLab 01 verification completed successfully.")
