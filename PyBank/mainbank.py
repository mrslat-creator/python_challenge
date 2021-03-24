# dependencies
import csv
import os

csv_filepath = os.path.join('Resource', 'budget_data.csv')

month_total = 0
net_total = 0
date = []
profit_losses ={}

with open(csv_filepath, newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader)
    # print(len(spamreader))
    for row in spamreader:
        month_total += 1
        
        date = row [2]
        if date not in date:
            date.append(date)
            date[date] = 0
        date[date] +=1
