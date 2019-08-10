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
    # below code prints out the total months
    print("Total months:", len(budget_date))

with open(csvpath, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")
    budget_header = next(budget_reader)
#created the list variable below for the profit/loss row.
    budget_num = []
    diff = 0
#created the for loop to append row 1 to budget_num
    for rows in budget_reader:
        budget_num.append(int(rows[1]))
# print(budget_num) successful
# sum up the budget_num list
    sum (budget_num) 
# I'm setting a variable (net_total) to equal sum (budget_num)
    net_total = sum (budget_num)
#print successfull
    print(f'Total: ${net_total}')

#duplicating the csv reader to calculate the amounts required in the HW.
with open(csvpath, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")
    budget_header = next(budget_reader)
    profit_loss = []
    diff_list = []
    for rows in budget_reader:
        profit_loss.append(int(rows[1]))
    diff = [profit_loss[i+1] - profit_loss[i] for i in range(len(profit_loss)-1)]
    

diff_list = diff
sum (diff_list)
max (diff_list)
min(diff_list)
diff_sum = sum (diff_list)   
diff_avg = round(diff_sum / len(diff_list),2)
diff_max = max(diff_list)
diff_min = min(diff_list)

print(f'Average Change: ${diff_avg}')
print(f'Max Amount: ${diff_max}')
print(f'Min Amount: ${diff_min}')
      

