"""
Find the number of times the words 'bull' and 'bear' occur in the contents. We're counting the number of times the words occur so words like 'bullish' should not be included in our count.
Output the word 'bull' and 'bear' along with the corresponding number of occurrences.
"""

# Import your libraries
import pandas as pd
import re

# Start writing code

gfs = google_file_store

#bull = gfs[gfs['contents'].str.contains(r'\bbull\b', flags=re.I)]
#bear = gfs[gfs['contents'].str.contains(r'\bbear\b', flags=re.I)]

gfs['bull'] = gfs['contents'].apply(lambda text: len(re.findall(r'\bbull\b', text)))
gfs['bear'] = gfs['contents'].apply(lambda text: len(re.findall(r'\bbear\b', text)))
gfs[['bull', 'bear']].sum().reset_index()
