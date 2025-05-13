#!/bin/bash

spark-submit \
  --packages org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.4.2 \
  --jars jars/gcs-connector.jar \
  scripts/03_create_iceberg_table.py
