import yaml
import logging

from yaml.parser import ParserError
from yaml.scanner import ScannerError

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    try:
        data = yaml.safe_load(data)
        if not isinstance(data, dict):
            raise ValueError(f"YAML top-level value is not a mapping, actual type: { type(data)}")
        logging.info("YAML read")
        return data
    except (ValueError, AttributeError) as e:
        logging.error("There was an error with given data: %s", e)
        return None
    except (ScannerError, ParserError) as e:
        logging.error("There was an error with YAML structure: %s", e)

