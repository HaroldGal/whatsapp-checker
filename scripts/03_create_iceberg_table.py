from pyspark.sql import SparkSession

BUCKET = "whatsapp-database"
LANDING_PATH = f"gs://{BUCKET}/landing/"
ICEBERG_WAREHOUSE = f"gs://{BUCKET}/iceberg/"

def main():
    session = (
        SparkSession.builder
        .appName("CreateIcebergTable")
        .config("spark.sql.catalog.my_catalog", "org.apache.iceberg.spark.SparkCatalog")
        .config("spark.sql.catalog.my_catalog.type", "hadoop")
        .config("spark.sql.catalog.my_catalog.warehouse", ICEBERG_WAREHOUSE)
        .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
        .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", "/Users/harold/Projects/whatsapp-checker/key/whatsapp-checker-458308-b666ca5cec9c.json")
        .getOrCreate()
    )

    # Lire les fichiers bruts
    df = session.read.parquet(LANDING_PATH)

    # Créer ou remplacer la table Iceberg (bronze layer)
    (
        df.writeTo("my_catalog.bronze_whatsapp")
        .using("iceberg")
        .tableProperty("format-version", "2")
        .createOrReplace()
    )

    print("Iceberg table 'bronze_whatsapp' created at:", ICEBERG_WAREHOUSE)

if __name__ == "__main__":
    main()
