import json
import csv
import logging

logger = logging.getLogger(__name__)

class Writer:
    def write_json(self, filepath, data):
        try:
            with open(filepath, 'w') as file:
                json.dump(data, file, indent=4)
            logger.info(f"Successfully wrote JSON to file: {filepath}")
        except Exception as e:
            logger.error(f"Error writing JSON to file: {filepath} - {e}", exc_info=True)
            raise

    def write_csv(self, filepath, data):
        try:
            keys = data[0].keys()  # Assuming all dictionaries have the same keys
            with open(filepath, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
            logger.info(f"Successfully wrote CSV to file: {filepath}")
        except Exception as e:
            logger.error(f"Error writing CSV to file: {filepath} - {e}", exc_info=True)
            raise