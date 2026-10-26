# Bring Your Own Device (BYOD) Hardware & Software Specifications

To successfully complete the laboratory exercises, distributed container stacks, and big data pipeline tasks, all enrolled students must have access to a personal laptop meeting or exceeding the technical specifications below.

---

## 1. Workstation Hardware Benchmarks

| Hardware Component | Minimum Requirement | Recommended Specification |
| :--- | :--- | :--- |
| **Processor (CPU)** | Intel Core i7 / AMD Ryzen 7 (8 cores, 16 threads) | Apple Silicon (M2/M3 Pro or Max) OR Intel Core i9 / AMD Ryzen 9 |
| **Memory (RAM)** | 16 GB Unified / DDR4 | **32 GB or 64 GB RAM** (Required for concurrent local Spark, Kafka, Airflow, and Postgres containers) |
| **Storage (SSD)** | 512 GB PCIe NVMe SSD | **1 TB or 2 TB NVMe SSD** (Minimum 150 GB free disk space dedicated to Docker images and data files) |
| **Operating System** | Windows 11 Pro / Enterprise (with WSL2) OR macOS 14+ (Sonoma/Sequoia) | macOS with Apple Silicon or Ubuntu Linux 22.04 LTS native |
| **Display** | 1080p FHD (1920x1080) minimum | External 4K or Dual Monitors recommended for data pipeline development |

---

## 2. Software Prerequisites & Tooling Installation Guide

Students should install the following base software prior to Week 1:

### 2.1 Containerization & Virtualization
* **Docker Desktop** (or Rancher Desktop / OrbStack on macOS):
  * Allocate at least **8 CPU cores** and **12 GB RAM** in Docker Desktop settings.
  * Enable Docker Compose v2.

### 2.2 Python & Big Data Environment
* **Python 3.10 or 3.11** installed via `pyenv` or `conda`.
* **Java Development Kit (JDK):** OpenJDK 17 LTS (Required for local Apache Spark execution):
  ```bash
  # macOS (Homebrew)
  brew install openjdk@17
  
  # Ubuntu / WSL2
  sudo apt install openjdk-17-jdk
  ```
* Set `JAVA_HOME` in your shell configuration (`~/.bashrc` or `~/.zshrc`).

### 2.3 Cloud CLIs & Infrastructure as Code
* **AWS CLI v2** and **Azure CLI (`az`)**.
* **Terraform CLI (v1.8+)**:
  ```bash
  terraform -version
  ```

### 2.4 Business Intelligence & Storytelling
* **Microsoft Power BI Desktop** (Windows native or via Windows VM / Parallels on macOS).
* **Tabular Editor 2.x** (Open source) for localized translation and tabular model management.
* **DAX Studio** (Free) for DAX query optimization and performance tracing.
