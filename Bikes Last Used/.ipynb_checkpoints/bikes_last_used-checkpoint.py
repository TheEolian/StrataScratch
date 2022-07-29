"""
Find the last time each bike was in use. Output both the bike number and the date-timestamp of the bike's last use (i.e., the date-time the bike was returned). Order the results by bikes that were most recently used.
"""
# Import your libraries
import pandas as pd

# Start writing code
dc_bikeshare_q1_2012.head()
q1_2012_subset = dc_bikeshare_q1_2012[['bike_number', 'end_time']]
q1_2012_subset_ordered = q1_2012_subset.sort_values(['end_time'], ascending=False)
no_duplicates = q1_2012_subset_ordered.drop_duplicates(['bike_number'])
no_duplicates