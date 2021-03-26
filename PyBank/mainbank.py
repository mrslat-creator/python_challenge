# dependencies
import csv
import os
import datetime

csv_filepath = os.path.join('Resource', 'budget_data.csv')

month_total = 0
profit = 0
sum_profit = 0
sum_loss = 0

with open(csv_filepath, newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader)
    # print(len(spamreader))
    for row in spamreader:
        month_total += 1
        
# The total number of months included in the dataset
end_date = datetime.datetime(2017, 2)
start_date = datetime.datetime(2010, 1)

num_months = (end_date.year - start_date.year) * 12 + (end_date.month -

print(num_months)

#  The net total amount of "Profit/Losses" over the entire period
for row in csv_filepath:
    profit = int(row[1])
    if profit > 0:
        sum_profit =sum_profit + profit
    elif profit < 0:
        sum_loss
#  Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#  The greatest increase in profits (date and amount) over the entire period

#  The greatest decrease in losses (date and amount) over the entire period