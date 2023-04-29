import csv 
from pathlib import Path

input_file = Path("budget_data.csv")
output_file = Path("result_PyBank.txt")


# Reading the file
with open(input_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Empty Lists
    total_months = []
    total_profit = []
    monthly_profit_change = []

    for row in csvreader: 

        # Add the total months and total profit to their empty lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Get monthly change in profits
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# Get the max and min for profit change
    max_increase_value = max(monthly_profit_change)
    max_decrease_value = min(monthly_profit_change)

# Get greatest increase and decrease over a period of time
    max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
    max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 


#Report Summary
    report = f'''Financial Analaysis
    Financial Analysis
    ----------------------------
    Total Months: {len(total_months)}
    Total: ${sum(total_profit)}
    Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}
    Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})
    Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})'''

    print(report)

# Spit Out to Text File
    with output_file.open("w") as txtfile:
        txtfile.write(report)

