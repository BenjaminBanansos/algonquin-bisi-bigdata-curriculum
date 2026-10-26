"""
BISI-101: Lab 03 - PySpark DataFrame API on Canadian Census Microdata
Author: Algonquin College Business Intelligence & Big Data Faculty

Objectives:
1. Initialize a resilient SparkSession with custom memory configurations.
2. Load and parse semi-structured census records with explicit schemas.
3. Compute distributed aggregations across provincial and demographic strata.
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql import functions as F

def get_spark_session() -> SparkSession:
    return (
        SparkSession.builder
        .appName("BISI-101-Lab03-CensusDataFrames")
        .master("local[4]")
        .config("spark.driver.memory", "2g")
        .config("spark.sql.shuffle.partitions", "8")
        .getOrCreate()
    )

def run_census_analysis(spark: SparkSession):
    # 1. Define explicit schema (prevents expensive schema inference pass)
    schema = StructType([
        StructField("record_id", IntegerType(), False),
        StructField("province", StringType(), False),
        StructField("age_group", StringType(), False),
        StructField("household_income", DoubleType(), True),
        StructField("education_level", StringType(), True),
        StructField("official_language", StringType(), False)
    ])

    # 2. Synthetic Census Microdata
    sample_data = [
        (1, "ON", "25-34", 82000.0, "Bachelor", "English"),
        (2, "QC", "35-44", 76000.0, "Master", "French"),
        (3, "ON", "45-54", 115000.0, "Bachelor", "Bilingual"),
        (4, "BC", "25-34", 91000.0, "Master", "English"),
        (5, "QC", "25-34", 64000.0, "College", "French"),
        (6, "AB", "35-44", 98000.0, "High School", "English"),
        (7, "ON", "35-44", 105000.0, "Doctorate", "English"),
        (8, "NB", "45-54", 58000.0, "College", "Bilingual"),
    ]

    df = spark.createDataFrame(sample_data, schema=schema)
    df.printSchema()

    # 3. Distributed Analytical Aggregation
    summary = (
        df.groupBy("province", "official_language")
        .agg(
            F.count("record_id").alias("sample_weight"),
            F.round(F.avg("household_income"), 2).alias("avg_income"),
            F.max("household_income").alias("max_income")
        )
        .orderBy(F.desc("avg_income"))
    )

    print("\n--- Census Distribution Summary ---")
    summary.show(truncate=False)

if __name__ == "__main__":
    spark = get_spark_session()
    run_census_analysis(spark)
    spark.stop()
