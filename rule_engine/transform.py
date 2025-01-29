import logging

logger = logging.getLogger(__name__)

class RuleEngine:
    def average_salary(self, applicants):
        try:
            total_salary = sum(int(applicants['AnnualSalary']) for applicants in applicants)
            avg_salary = total_salary / len(applicants)
            logger.info("Calculated average salary successfully.")
            return avg_salary
        except Exception as e:
            logger.error("Error calculating average salary", exc_info=True)
            raise

    def max_salary(self, applicants):
        try:
            max_salary = max(int(applicants['AnnualSalary']) for applicants in applicants)
            logger.info("Calculated maximum salary successfully.")
            return max_salary
        except Exception as e:
            logger.error("Error calculating maximum salary", exc_info=True)
            raise

    def min_salary(self, applicants):
        try:
            min_salary = min(int(applicants['AnnualSalary']) for applicants in applicants)
            logger.info("Calculated minimum salary successfully.")
            return min_salary
        except Exception as e:
            logger.error("Error calculating minimum salary", exc_info=True)
            raise