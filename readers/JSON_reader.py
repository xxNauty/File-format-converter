import json
import logging

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    try:
        formatted_data = json.loads(data)
        logging.info("JSON read")
        return formatted_data
    except json.JSONDecodeError as e:
        logging.error("An error occurred with JSON structure: %s", e)
        return None
    except TypeError as e:
        logging.error("Type error during conversion: %s", e)
        return None
