"""
We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order.
"""
# Import your libraries
import pandas as pd

# Start writing code
ms_employee_salary.head()

# Sort the salaries from highest to lowest
sorted = ms_employee_salary.sort_values(by=['salary'], ascending=False)

# Drop duplicate rows based on employee ID which are records of an their old salary, keep the first (highest) record
dropped = sorted.drop_duplicates(subset='id', keep="first")

# Sort the rows by employee id
dropped.sort_values(by='id')