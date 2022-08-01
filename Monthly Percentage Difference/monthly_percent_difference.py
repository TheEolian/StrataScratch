"""
Given a table of purchases by date, calculate the month-over-month percentage change in revenue. The output should include the year-month date (YYYY-MM) and percentage change, rounded to the 2nd decimal point, and sorted from the beginning of the year to the end of the year.
The percentage change column will be populated from the 2nd month forward and can be calculated as ((this month's revenue - last month's revenue) / last month's revenue)*100.
"""
# Import your libraries
import pandas as pd

# Start writing code
#sf_transactions.head()

# Add YYYY-MM column
sf_transactions['Date'] = pd.to_datetime(sf_transactions['created_at'], format='%Y%m.0').dt.strftime('%Y-%m')

# Group by Date YYYYMM col
grouped = sf_transactions.groupby(['Date']).sum().reset_index()
# Create % Change Column
grouped['percent_change'] = 0
# remove unneeded cols
grouped = grouped[['Date', 'value','percent_change']]

# Add previous value for calc
grouped['prev_value'] = grouped['value'].shift(1)

# Calculate percent change
grouped['percent_change'] = ((grouped['value'] - grouped['prev_value']) / grouped['prev_value'])*100
#grouped.fillna(0, inplace=True)

#round percent change to two decimals
grouped['percent_change'] = grouped['percent_change'].round(decimals = 2)
final = grouped[['Date','percent_change']]