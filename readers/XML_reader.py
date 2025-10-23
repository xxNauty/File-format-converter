import json
import logging
import xmltodict

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    ordered = xmltodict.parse(data)
    logging.info("XML read")
    return json.loads(json.dumps(ordered))