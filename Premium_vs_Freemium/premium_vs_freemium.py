"""
Find the total number of downloads for paying and non-paying users by date. Include only records where non-paying customers have more downloads than paying customers. The output should be sorted by earliest date first and contain 3 columns date, non-paying downloads, paying downloads.
"""

# Import your libraries
import pandas as pd

# First Merge
merge1 = ms_user_dimension.merge(ms_acc_dimension, on='acc_id')

# Second Merge
merge2 = merge1.merge(ms_download_facts, on='user_id')

# Create pivot table
pivoted = merge2.pivot_table(index='date', columns='paying_customer', values='downloads', aggfunc='sum')
pivoted
final = pivoted[pivoted['no'] > pivoted['yes']].reset_index()

final