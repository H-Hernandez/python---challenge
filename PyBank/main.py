import os
import csv

csvpath = os.path.join("..", "Pybank", "budget_data.csv")
print(csvpath)



with open(csvpath, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")
    budget_header = next(budget_reader)
    #created the list below for the dates, in order to generate the amount of months
    budget_date=[]
    for rows in budget_reader:
        budget_date.append(rows[0])
    
    print("Total months:", len(budget_date))

with open(csvpath, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")
    budget_header = next(budget_reader)
    #created the list below for the profit/loss calculations.
    net_total = []
    for i in budget_reader:
        net_total.append(i[1])
        print("Total sum:", sum(net_total))
        
    