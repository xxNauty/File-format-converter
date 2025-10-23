import csv
import logging

from io import StringIO

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    rows = csv.DictReader(StringIO(data))
    result = {}
    for i, row in enumerate(rows):
        result[i] = row
    logging.info("CSV read")
    return result

