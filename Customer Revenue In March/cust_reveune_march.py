"""
Calculate the total revenue from each customer in March 2019. Include only customers who were active in March 2019.

Output the revenue along with the customer id and sort the results based on the revenue in descending order.
"""

# Import your libraries
import pandas as pd
from datetime import datetime
# Start writing code
#orders.head()

orders['Month'] = pd.to_datetime(orders['order_date']).dt.month
orders['Year'] = pd.to_datetime(orders['order_date']).dt.year

filt = (orders['Year'] == 2019) & (orders['Month'] == 3)
march_orders = orders[filt]

cust_group = march_orders.groupby(['cust_id']).sum().reset_index()
id_and_rev = cust_group[['cust_id', 'total_order_cost']]

id_and_rev.sort_values(by='total_order_cost', ascending=False)