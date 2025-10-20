import json
import logging
import sys

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    try:
        formatted_data = json.loads(data)
        logging.info("JSON read")
        return formatted_data
    except json.JSONDecodeError:
        logging.error("An error occurred with JSON structure")
        return None

# json_data = '{"name": "Alice, "age": 30, "active": true}'
#
# result = process(json_data)
# if result is None:
#     sys.exit(1)
#
# print(result['name'])