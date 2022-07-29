"""
Find the top 5 states with the most 5 star businesses. Output the state name along with the number of 5-star businesses and order records by the number of 5-star businesses in descending order. In case there are ties in the number of businesses, return all the unique states. If two states have the same result, sort them in alphabetical order.
"""

# Import your libraries
import pandas as pd

# Start writing code
#yelp_business.head()

five_stars = yelp_business.loc[yelp_business['stars'] == 5]

state_groups = five_stars.groupby(['state']).size().reset_index(name='counts')

final_five_state_counts = state_groups.sort_values(by=['counts'], ascending=False)
final_five_state_counts = final_five_state_counts.head(6)
final_five_state_counts