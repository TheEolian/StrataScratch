"""
Find the top business categories based on the total number of reviews. Output the category along with the total number of reviews. Order by total reviews in descending order.
"""
# Import your libraries
import pandas as pd

yelp_business.head()

### Split and Explode

#reassign categories to be a split string
yelp_business['categories'] = yelp_business['categories'].str.split(";")

# grab only the colums we need 
yelp_business = yelp_business[['categories', 'review_count']]

### Use explode to separate the categorys list components to new rows 
### preserving review counts for each item mentioned in the review
yelp_business = yelp_business.explode('categories')

# group by categories and sum review counts
yelp_business = yelp_business.groupby(by='categories').sum().reset_index()

# Sort the values to descending order
yelp_business.sort_values('review_count', ascending=False)