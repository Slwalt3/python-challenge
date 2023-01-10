import os
import csv
csvpath = os.path.join('..','python-challenge','PyBank','Resources','budget_data.csv')
total_months = []
net_total_profit = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"csv header: {csv_header}")
    for row in csvreader:
        total_months.append(row[0])
        net_total_profit.append(row[1])
    print(len(total_months))
    net_total_profit = [int(x)for x in net_total_profit]
    totalprofit = (sum(net_total_profit))
    print(totalprofit)
avg_change = []
for i in range(len(net_total_profit)-1):
    avg_change.append(net_total_profit[i]-net_total_profit[i+1])
avg = sum(avg_change)/len(avg_change)
print(avg)
greatest_increase = 0
greatest_decrease = 999999
for i in range(len(net_total_profit)-1):
    if net_total_profit[i]-net_total_profit[i+1]>greatest_increase:
        greatest_increase = i+1
    if net_total_profit[i]-net_total_profit[i+1]<greatest_decrease:
        greatest_decrease = i+1
        print(greatest_increase)
