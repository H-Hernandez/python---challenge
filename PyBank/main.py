import os
import csv

csvpath = os.path.join("..", "Pybank", "budget_data.csv")
print(csvpath)



with open(csvpath, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")
    budget_header = next(budget_reader)
    budget_date=[]

    for rows in budget_reader:
        budget_date.append(rows[0])
    
    print("Total months ", len(budget_date))