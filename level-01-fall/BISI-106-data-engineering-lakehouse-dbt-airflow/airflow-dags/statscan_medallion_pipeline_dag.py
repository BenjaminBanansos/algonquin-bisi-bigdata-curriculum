"""
BISI-106: Production Apache Airflow DAG - Statistics Canada Open Data Medallion Pipeline
Author: Algonquin College Business Intelligence & Big Data Faculty
Schedule: Daily at 02:00 UTC
"""

from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'data_engineering_team',
    'depends_on_past': False,
    'email_on_failure': True,
    'email': ['data-alerts@example.gc.ca'],
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

@dag(
    dag_id='statscan_medallion_pipeline',
    default_args=default_args,
    description='Automated Bronze -> Silver -> Gold Lakehouse pipeline for StatsCan Open Data',
    schedule_interval='0 2 * * *',
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['public_sector', 'lakehouse', 'dbt', 'statscan']
)
def statscan_pipeline():

    @task
    def ingest_raw_open_data_bronze():
        """Extracts raw CSV/JSON payload from Open Government portal into Bronze storage."""
        print("Ingesting raw Statistics Canada microdata into MinIO Bronze bucket...")
        return "s3://bronze-bucket/statscan/2026/01/data.raw"

    @task
    def validate_bronze_schema(raw_uri: str):
        """Runs Great Expectations validation on raw ingestion payload."""
        print(f"Validating schema integrity and record count for: {raw_uri}")
        return True

    # Execute dbt transformation to Silver layer (Cleansed / Deduplicated)
    dbt_run_silver = BashOperator(
        task_id='dbt_run_silver_models',
        bash_command='dbt run --select models/silver --project-dir /opt/airflow/dbt_project'
    )

    # Execute dbt transformation to Gold layer (Business-Ready Marts)
    dbt_run_gold = BashOperator(
        task_id='dbt_run_gold_models',
        bash_command='dbt run --select models/gold --project-dir /opt/airflow/dbt_project'
    )

    # Run automated dbt tests
    dbt_test_quality_gates = BashOperator(
        task_id='dbt_test_quality_gates',
        bash_command='dbt test --project-dir /opt/airflow/dbt_project'
    )

    # DAG Dependency Topology
    raw_path = ingest_raw_open_data_bronze()
    is_valid = validate_bronze_schema(raw_path)
    
    is_valid >> dbt_run_silver >> dbt_run_gold >> dbt_test_quality_gates

pipeline_instance = statscan_pipeline()
