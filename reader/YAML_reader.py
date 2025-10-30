import yaml
import logging

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    data = yaml.safe_load(data)
    logging.info("YAML read")
    return data

