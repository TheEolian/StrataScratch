"""
Find order details made by Jill and Eva.
Consider the Jill and Eva as first names of customers.
Output the order date, details and cost along with the first name.
Order records based on the customer id in ascending order.
"""

# Import your libraries
import pandas as pd

# Filter to only records with Jill or Eva as the first name
jill_and_eva = customers.loc[(customers['first_name'] == 'Eva') | (customers['first_name'] == 'Jill')]
jill_and_eva.head()

#rename id column to merge on
jill_and_eva.rename(columns = {'id':'cust_id'}, inplace = True)
jill_and_eva.head()

# merge orders df on customers df
merged = jill_and_eva.merge(orders, on='cust_id')
merged.head()

# Output the order date, details and cost along with the first name.
reduced_df = merged[['order_date','order_details','total_order_cost','first_name','cust_id']]
reduced_df.head()

# Order records based on the customer id in ascending order
reduced_df.sort_values(by='cust_id')