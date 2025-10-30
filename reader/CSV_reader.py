import csv
import logging

from common import datatype_fixer
from io import StringIO

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict:
    rows = csv.DictReader(StringIO(data))
    result = {}
    for i, row in enumerate(rows):
        for key, value in row.items():
            row[key] = datatype_fixer.fix_datatype(value)
        result[i] = row
    logging.info("CSV read")
    return result