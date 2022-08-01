"""
Find the top business categories based on the total number of reviews. Output the category along with the total number of reviews. Order by total reviews in descending order.
"""
# Import your libraries
import pandas as pd

# Start writing code
#yelp_business.head()

#make a column list of the categories
yelp_business['cats'] = yelp_business['categories'].str.split(";")

#get only the colums we need 
yelp_business = yelp_business[['cats', 'review_count']]

# Use explode to separate the cats list components to new rows (preserving review counts)
yelp_business = yelp_business.explode('cats')

# group by category and sum reviews
yelp_business = yelp_business.groupby(by='cats').sum().reset_index().sort_values('review_count', ascending=False)