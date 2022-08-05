"""
Meta/Facebook has developed a new programing language called Hack.To measure the popularity of Hack they ran a survey with their employees. The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with Hack. Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location. Luckily the user IDs of employees completing the surveys were stored.
Based on the above, find the average popularity of the Hack per office location.
Output the location along with the average popularity.
"""

# Import your libraries
import pandas as pd

# Rename employee_id column to match other df for quick merge
facebook_hack_survey.rename(columns = {'employee_id':'id'}, inplace=True)

# Merge the two dataframes on the id column
merged = facebook_employees.merge(facebook_hack_survey, on='id')

# Group df by location and return the average of popularity for each location
merged = merged.groupby(['location']).agg({'popularity': 'mean'}).reset_index()
merged