"""
Find the review_text that received the highest number of  'cool' votes.
Output the business name along with the review text with the highest numbef of 'cool' votes.
"""

# Import your libraries
import pandas as pd

# Start writing code
max_vote = yelp_reviews['cool'].max()

# Get the records where cool equals the max
yelp_reviews = yelp_reviews[yelp_reviews['cool'] == max_vote]

#Get only the columns we want
yelp_reviews = yelp_reviews[['business_name', 'review_text']]
yelp_reviews