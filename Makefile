.PHONY: help up down status restart logs spark-shell jupyter test clean

help:
	@echo "=========================================================================="
	@echo "Algonquin BISI - Big Data & Public Sector Infrastructure Management CLI"
	@echo "=========================================================================="
	@echo "make up          - Start all local stack containers (Spark, Kafka, Postgres, Airflow, MinIO)"
	@echo "make down        - Tear down stack and preserve volumes"
	@echo "make status      - Display running container states and exposed ports"
	@echo "make logs        - Tail stack logs across all services"
	@echo "make spark-shell - Enter interactive PySpark shell on Spark Master"
	@echo "make jupyter     - Output JupyterLab URL with access token"
	@echo "make test        - Run test suite across course lab modules"
	@echo "make clean       - Remove cached data files, python bytecode, and temporary logs"
	@echo "=========================================================================="

up:
	docker compose up -d
	@echo "Services launching. Open http://localhost:8888 for JupyterLab, http://localhost:8080 for Airflow."

down:
	docker compose down

status:
	docker compose ps

restart:
	docker compose restart

logs:
	docker compose logs -f

spark-shell:
	docker compose exec spark-master /opt/spark/bin/pyspark

jupyter:
	@echo "JupyterLab available at: http://localhost:8888 (Token: bisi2026)"

test:
	pytest -v level-01-fall/ level-02-winter/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
