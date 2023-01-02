"""
Required Tasks
These are the required tasks for this project. You should aim to complete these tasks before
adding your own ideas to the project.
1. Read the data from the spreadsheet
2. Collect all of the sales from each month into a single list
3. Output the total sales across all months

Ideas for Extending the Project
Here are a few ideas for extending the project beyond the required tasks. These ideas are just
suggestions, feel free to come up with your own ideas and extend the program however you want.
● Calculate the following:
○ Monthly changes as a percentage 4.
○ The average 5.
○ Months with the highest and lowest sales 6.

"""

import pandas as pd

data = pd.read_csv('sales.csv')  # 1.
sales = data['sales'].to_list()  # 2.
print('sales', sales)
sales_sum = sum(sales)  # 3.
print('sales sum', sales_sum)

average = sales_sum / len(sales)  # 5.
print('average', average)
minimum = min(sales)  # 6.
print('min', minimum)
maximum = max(sales)  # 6.
print('max', maximum)

data['change'] = 'no info'

for index, row in data.iterrows():  # 4.
    if index > 0:
        change = data['sales'].iloc[index] / data['sales'].iloc[index-1] * 100
        data['change'].iloc[index] = f"{round(change - 100, 2)}%"

print(data.to_string())

