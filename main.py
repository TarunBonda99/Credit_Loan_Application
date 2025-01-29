import os
import logging
from reader.read import Reader
from rule_engine.transform import RuleEngine
from writing.write import Writer

# Configure logging
logging.basicConfig(
    filename=os.path.join('output', 'app.log'),
    filemode='a',  # Append to the log file
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # Capture all levels of logs (DEBUG, INFO, WARNING, ERROR, CRITICAL)
)

logger = logging.getLogger(__name__)

def main():
    # Input and output directories
    input_path = './input/applicants.json'  # Path to your input file
    output_path = './output'                # Path to your output directory
    file_type = 'csv'                       # 'json' or 'csv'

    reader = Reader()
    rule_engine = RuleEngine()
    writer = Writer()

    try:
        # Read the input data
        if file_type == 'json':
            data = reader.read_json(input_path)
            applicants = data['applicants']
        elif file_type == 'csv':
            applicants = reader.read_csv(input_path)
        else:
            logger.error("Unsupported file type")
            return

        # Calculate salary statistics
        avg_salary = rule_engine.average_salary(applicants)
        max_salary = rule_engine.max_salary(applicants)
        min_salary = rule_engine.min_salary(applicants)

        # Prepare the output data
        output_data = {
            "average_salary": avg_salary,
            "max_salary": max_salary,
            "min_salary": min_salary
        }

        # Write the output data
        if file_type == 'json':
            writer.write_json(os.path.join(output_path, 'salary_report.json'), output_data)
        elif file_type == 'csv':
            writer.write_csv(os.path.join(output_path, 'salary_report.csv'), [output_data])

        logger.info("Processing completed successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
        print("An error occurred. Check the log file for more details.")

if __name__ == "__main__":
    main()