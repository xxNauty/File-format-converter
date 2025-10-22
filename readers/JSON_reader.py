import json
import logging

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    try:
        formatted_data = json.loads(data)
        logging.info("JSON read")
        return formatted_data
    except json.JSONDecodeError as e:
        logging.error(f"An error occurred with JSON structure: {e}")
        return None
    except TypeError as e:
        logging.error(f"Type error during conversion: {e}")
        return None