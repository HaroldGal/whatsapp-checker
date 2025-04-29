"""
Upload local parquet files to GCS bronze layer
"""

from pathlib import Path
from google.cloud import storage
from os import path

BASE_DIR = path.dirname(path.realpath(__file__))
BRONZE_DIR = Path(path.join(BASE_DIR, "../data/bronze"))
GCS_BUCKET = "whatsapp-database"
GCS_FOLDER = "bronze/"

def upload_file(client, local_path, bucket_name, gcs_path):
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(gcs_path)
    blob.upload_from_filename(local_path)
    print(f"Uploaded {local_path} to gs://{bucket_name}/{gcs_path}")

def upload_parquets_to_gcs():
    storage_client = storage.Client()

    for parquet_file in BRONZE_DIR.glob("*.parquet"):
        gcs_target_path = f"{GCS_FOLDER}{parquet_file.name}"
        upload_file(storage_client, str(parquet_file), GCS_BUCKET, gcs_target_path)

if __name__ == "__main__":
    upload_parquets_to_gcs()
