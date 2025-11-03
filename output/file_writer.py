import logging
import os

logging.basicConfig(level=logging.INFO)

def write_to_file(filepath: str, data:str) -> None:
    try:
        with open(filepath, 'w') as file:
            file.write(data)
            file.close()
            logging.info("Data writen to file")
    except Exception as error:
        logging.error("Something went wrong when writing to file: %s", error)
        os.remove(filepath)