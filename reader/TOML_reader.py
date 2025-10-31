import tomllib
import logging

logging.basicConfig(level=logging.INFO)

def process(data: str) -> dict|None:
    formatted_data = tomllib.loads(data)

    logging.info("TOML read")
    return formatted_data
