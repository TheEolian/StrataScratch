"""
Find the titles of workers that earn the highest salary. Output the highest-paid title or multiple titles that share the highest salary.
"""

# Import your libraries
import pandas as pd

# Start writing code
worker.head()
df = worker.sort_values('salary', ascending=False)
max_salary = df.loc[df['salary'] == df['salary'].max()]

max_merged = max_salary.merge(title, left_on='worker_id', right_on='worker_ref_id')
result = max_merged.worker_title