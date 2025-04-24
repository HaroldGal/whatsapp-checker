"""
Unzip the whatsapp exports
"""

import zipfile
from os import path, listdir
from pathlib import Path


DATA_DIR = path.dirname(path.realpath(__file__))
WHATSAPP_ZIP_DIR = path.join(DATA_DIR, "../data/whatsapp_exports")
WHATSAPP_TXT_DIR = path.join(DATA_DIR, "../data/raw")

def extract_whatsapp_zip(zip_file_path):
    file_name = Path(zip_file_path).stem
    with zipfile.ZipFile(zip_file_path, "r") as zip_file:
        zip_file.extractall(path=path.join(WHATSAPP_TXT_DIR, file_name) )
    print(f"Extracted {zip_file_path} to {file_name}/")

def get_whatsapp_zip_files():
    return [f for f in listdir(WHATSAPP_ZIP_DIR) if f.endswith(".zip")]

if __name__ == "__main__":
    for zip_file in get_whatsapp_zip_files():
        extract_whatsapp_zip(path.join(WHATSAPP_ZIP_DIR, zip_file))