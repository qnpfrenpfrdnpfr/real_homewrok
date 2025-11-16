# app/utils/file_handler.py
import json
from typing import List, Dict

def read_json(path: str) -> List[Dict]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def write_json(path: str, data: List[Dict]):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
