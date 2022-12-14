"""
Find the customer with the highest daily total order cost between 2019-02-01 to 2019-05-01. If customer had more than one order on a certain day, sum the order costs on daily basis. Output customer's first name, total cost of their items, and the date.

For simplicity, you can assume that every first name in the dataset is unique.
"""

# Import your libraries
import pandas as pd

# merge customers and orders on id/cust_id and sort values
df = customers.merge(orders, how = 'right', left_on = 'id', right_on = 'cust_id').sort_values (by = ['first_name','order_date'])

# Group by first name and order date and sum the total order cost
df = df.groupby(['first_name','order_date'], as_index = False)['total_order_cost'].sum()

# Remove hours/minutes/seconds
df['order_date'] = df['order_date'].dt.strftime('%Y-%m-%d')

# Get only values between Feb 1, 2019 and May 1, 2019
df[df['order_date'].between('2019-02-01', '2019-05-01')]

# Return only the largest daily total order
df.nlargest(1,'total_order_cost', keep= 'all')