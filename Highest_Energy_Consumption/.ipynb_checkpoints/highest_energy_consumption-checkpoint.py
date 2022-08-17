"""
Find the date with the highest total energy consumption from the Meta/Facebook data centers. Output the date along with the total energy consumption across all data centers.
"""

# Import your libraries
import pandas as pd

# Start writing code

# Concat the three dataframes 
df = pd.concat([fb_eu_energy, fb_asia_energy, fb_na_energy])

# group on date and sum the consumption column
df = df.groupby('date', as_index = False)['consumption'].sum()

# Get max row for consumption
df[df['consumption'] == df['consumption'].max()].sort_values('date')