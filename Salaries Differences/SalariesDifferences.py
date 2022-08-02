"""
Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. Output just the absolute difference in salaries.
"""

# Import your libraries
import pandas as pd

# Start writing code
#db_employee.head()

# Dept 1 is Engineering. Dept 4 is marketing

mark = db_employee[db_employee['department_id'] == 4]['salary'].max()

eng = db_employee[db_employee['department_id'] == 1]['salary'].max()

diff = mark - eng

diff