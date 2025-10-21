import csv
import io
import logging

logging.basicConfig(level=logging.INFO)

def process(data: str, key_column: str, delimiter: str = ",") -> dict|None:
    try:
        if delimiter not in data:
            raise ValueError("There is no such character in data")
        reader = csv.DictReader(io.StringIO(data), delimiter=delimiter)
        result = {}
        for row in reader:
            if key_column not in row:
                raise KeyError(f"Key column {key_column!r} not found in CSV headers")
            key = row[key_column]
            value = {k: v for k, v in row.items() if k != key_column}
            result[key] = value
        logging.info("CSV read")
        return result
    except KeyError as e:
        logging.error("An error occurred while conversion: %s", e)
        return None
    except ValueError as e:
        logging.error("An error occurred while conversion: %s", e)