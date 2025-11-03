import logging

logging.basicConfig(level=logging.INFO)

def read_file(filepath: str) -> str|None:
    try:
        with open(filepath, 'r') as file:
            logging.info("File read")
            return file.read()
    except FileNotFoundError:
        logging.error("There is no such file")
        return None