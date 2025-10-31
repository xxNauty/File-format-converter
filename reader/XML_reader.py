import xmltodict
import logging

from common import datatype_fixer

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    result = xmltodict.parse(data)

    for key, value in result.items():
        result[key] = datatype_fixer.fix_datatype(value)

    logging.info("XML read")
    return result