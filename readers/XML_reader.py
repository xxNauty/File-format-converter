import json
import logging
import xmltodict
import xml.parsers.expat

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    try:
        ordered = xmltodict.parse(data)
        logging.info("XML read")
        return json.loads(json.dumps(ordered))
    except xml.parsers.expat.ExpatError as e:
        logging.error("XML parse error: %s", e)
        return None
    except TypeError as e:
        logging.error("Type error during conversion: %s", e)
        return None