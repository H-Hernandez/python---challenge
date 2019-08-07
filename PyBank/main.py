import os
import csv

csvpath = os.path.join("..", "Pybank", "budget_data.csv")
print(csvpath)

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    for row in csvreader:
        print(row)
