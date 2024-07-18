import os
import csv

#set file path
budgetdatacsv = "/Users/mackenzie/python-challenge/PyBank/Resources/budget_data.csv"
text_path = "budget_data.txt"

#set variables
total_months = 0
total_profits = 0
profit_change_ls = []
monthly_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

#open/read csv file
with open(budgetdatacsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csvreader)

    for row in csvreader:
        #grab months and profits/losses
        total_months += 1
        profit = int(row[1])
        total_profits += profit

        #calculate profit change
        if total_months > 1:
            profit_change = profit - previous_profits
            profit_change_ls.append(profit_change)
            monthly_changes.append(row[0])

            #greatest increase and decrease
            if profit_change > greatest_increase[1]:
                greatest_increase = [row[0], profit_change]
            if profit_change < greatest_decrease[1]:
                greatest_decrease = [row[0], profit_change]

        previous_profits = profit

#calculate average change
revenue_average = sum(profit_change_ls) / len(profit_change_ls)

#print to terminal
print("Financial Analysis\n")
print("---------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total Revenue: ${total_profits}\n")
print(f"Average Revenue Change: ${revenue_average:.2f}\n")
print(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n")
print(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
#write to text file
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total Revenue: ${total_profits}\n")
    file.write(f"Average Revenue Change: ${revenue_average:.2f}\n")
    file.write(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")