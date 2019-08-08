import os
import csv

csvpath = os.path.join("..", "Pybank", "budget_data.csv")
print(csvpath)



with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvreader = next(csvreader)
    months = []

    for rows in csvreader:
        months.append(rows[0])
        print(months)