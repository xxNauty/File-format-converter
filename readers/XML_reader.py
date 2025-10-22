import json
import logging
import xmltodict

from xml.parsers.expat import ExpatError

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    try:
        ordered = xmltodict.parse(data)
        logging.info("XML read")
        return json.loads(json.dumps(ordered))
    except ExpatError as e:
        logging.error(f"XML parse error: {e}")
        return None
    except TypeError as e:
        logging.error(f"Type error during conversion: {e}")
        return None