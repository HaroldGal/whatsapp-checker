# 📱 WhatsApp Analyzer

![Iceberg](https://img.shields.io/badge/Iceberg-Table-blue?logo=apache)
![GCS](https://img.shields.io/badge/GCS-Storage-yellow?logo=googlecloud)
![Terraform](https://img.shields.io/badge/Terraform-Infrastructure-purple?logo=terraform)

Personal project to analyze my WhatsApp history using modern data tools.
Simple, local-first setup that showcases clean data engineering practices.
Useful project to test technologies.

## 🔧 Stack
- **Apache Iceberg** for versioned, queryable tables
- **GCS** (Google Cloud Storage) as the data lake
- **Terraform** to provision the infra
- **Spark + SQL scripts** to explore and analyze the data

## 📌 Objectives (MAYBE WOULD CHANGE)
- [x] Automatize unzip tasks;
- [x] Parse raw WhatsApp .txt export into structured format;
- [ ] Provision GCS bucket via Terraform;
- [ ] Upload parsed data to GCS following Apache Iceberg practices;
- [ ] Create usable layers of data with CLI tools;
- [ ] Have visualisation or toolbox to get some KPIs (TO DEFINE).

## 🚀 Quickstart (coming soon)

### Source system setup

1. Extract aimed conversations on whatsApp application.
2. Copy all files (*.zip) into whats_app_extracts folder.
3. Use terraform to create GCS environment.
4. Use differents scripts to load it into GCS as parquet.
