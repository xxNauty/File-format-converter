import json
import logging
import xmltodict

from common import datatype_fixer

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    ordered = xmltodict.parse(data)
    logging.info("XML read")
    result = json.loads(json.dumps(ordered))
    print(result)
    for key, value in result.items():
        result[key] = datatype_fixer.fix_datatype(value)

    return result