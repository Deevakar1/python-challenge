import os
import csv

os.chdir(os.path.dirname(__file__))
month=0
total=0
current_mth=0
last_mth =0
change_number =0
total_change =[]
months=[]

bank_data_csv = os.path.join("Resources/budget_data.csv")

with open(bank_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
     
    for row in csvreader:
        month = month+1
        months.append(row[0])
        current_mth = int(row[1])
        total = total+current_mth
        if month>1:
            change_number = current_mth - last_mth
            total_change.append(change_number)
        last_mth = current_mth  

sum_profit = sum(total_change)
average_change = (sum_profit/ (month - 1))
max_change = max(total_change)
min_change = min(total_change)
max_month_index = total_change.index(max_change)
min_month_index = total_change.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

print("Total Months:" + str(month))
print("Total:$" + str(total))
print(f'Average Change:${round(average_change,2)}')
print(f"Greatest Increase in profits: {max_month} (${max_change})")
print(f"Greatest Increase in profits: {min_month} (${min_change})")
