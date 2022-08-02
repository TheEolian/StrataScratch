"""
Find all Lyft drivers who earn either equal to or less than 30k USD or equal to or more than 70k USD.
Output all details related to retrieved records.
"""
# Import your libraries
import pandas as pd

# Start writing code
df = lyft_drivers.loc[(lyft_drivers['yearly_salary'] <= 30000) | (lyft_drivers['yearly_salary'] >= 70000)]
df