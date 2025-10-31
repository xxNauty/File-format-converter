import json
import logging

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    formatted_data = json.loads(data)

    logging.info("JSON read")
    return formatted_data
