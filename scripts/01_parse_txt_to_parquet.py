"""
Parse WhatsApp _chat.txt files into Parquet files using Polars.
One Parquet file is created per group.
"""

import re
from os import path
from pathlib import Path
import polars as pl

BASE_DIR = path.dirname(path.realpath(__file__))
RAW_DIR = path.join(BASE_DIR, "../data/raw")
OUTPUT_DIR = path.join(BASE_DIR, "../data/bronze")

LINE_REGEX = re.compile(r"^\[(.*)\] (.*): (.*)$")

def remove_200E(s: str) -> str:
    return s.replace("\u200E", "").strip()

def parse_chat_file(file_path: Path, group_name: str) -> pl.DataFrame | None:
    records = []
    group_name = remove_200E(group_name)

    with file_path.open(encoding="utf-8") as f:
        for line in f:
            match = LINE_REGEX.match(remove_200E(line))
            if match:
                timestamp, sender, message = match.groups()
                records.append((timestamp, sender, message, group_name))

    if not records:
        return None

    return pl.DataFrame(records, schema=["timestamp", "sender", "message", "group_name"])

def parse_and_save_each_chat():
    for chat_file in Path(RAW_DIR).rglob("_chat.txt"):
        group_name = chat_file.parent.name
        print(f"Parsing {chat_file} (group: {group_name})")

        df = parse_chat_file(chat_file, group_name)
        if df is None or df.is_empty():
            print(f"No valid messages in {chat_file}, skipping.")
            continue

        output_path = path.join(OUTPUT_DIR,f"{group_name}.parquet")
        df.write_parquet(output_path)
        print(f"Saved {len(df)} rows to {output_path}")

if __name__ == "__main__":
    parse_and_save_each_chat()
