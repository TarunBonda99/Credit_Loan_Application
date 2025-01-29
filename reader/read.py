import json
import csv
import logging

logger = logging.getLogger(__name__)

class Reader:
    def read_json(self, filepath):
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                logger.info(f"Successfully read JSON file: {filepath}")
                return data
        except Exception as e:
            logger.error(f"Error reading JSON file: {filepath} - {e}", exc_info=True)
            raise

    def read_csv(self, filepath):
        try:
            with open(filepath, 'r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                logger.info(f"Successfully read CSV file: {filepath}")
                return data
        except Exception as e:
            logger.error(f"Error reading CSV file: {filepath} - {e}", exc_info=True)
            raise