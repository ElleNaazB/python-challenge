import csv
import os

# Defining the current directory where the script is located
CURRENT_DIR = os.path.dirname(__file__)

# Defining the path to the CSV file
csvpath = os.path.join(CURRENT_DIR, '../Resources/budget_data.csv')

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_month_profit_losses = None
monthly_change = []
dates = []

# Try to open and read the CSV file
try:
    with open(csvpath, mode='r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)  # Skip the header row
        
        for row in csvreader:
            # Counting the total number of months
            total_months += 1

            # Calculating the total profit/losses
            current_month_profit_losses = int(row[1])
            total_profit_losses += current_month_profit_losses

            # Calculating the monthly change in profit/losses
            if previous_month_profit_losses is not None:
                change = current_month_profit_losses - previous_month_profit_losses
                monthly_change.append(change)
                dates.append(row[0])

            previous_month_profit_losses = current_month_profit_losses

    # Calculating average change, greatest increase, and decrease
    if len(monthly_change) > 0:
        average_change = sum(monthly_change) / len(monthly_change)
        greatest_increase = max(monthly_change)
        greatest_decrease = min(monthly_change)
        increase_date = dates[monthly_change.index(greatest_increase)]
        decrease_date = dates[monthly_change.index(greatest_decrease)]
    else:
        average_change = 0
        greatest_increase = 0
        greatest_decrease = 0
        increase_date = ''
        decrease_date = ''

    # Analyzing the data
    analysis = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit_losses}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})"
    )

    print(analysis)

    # Saving the output in the same directory as the script
    output_path = os.path.join(CURRENT_DIR, 'financial_analysis.txt')
    with open(output_path, 'w') as file:
        file.write(analysis)

except FileNotFoundError:
    print(f"Error: The file at '{csvpath}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

    
        
avarage_change=sum(monthly_change)/len(monthly_change)
if len(monthly_change) > 0:
             average_change = sum(monthly_change) / len(monthly_change)
else:
    average_change = 0
    greatest_increase =max(monthly_change)
    greatest_deacrease=min(monthly_change)

    increase_date = dates[monthly_change.index(greatest_increase)]
    decrease_date = dates[monthly_change.index(greatest_deacrease)]

#Printing the calculations
analysis = (
    "financial Analysis\n"
    "----------------------------\n"
    f"Total Months : {total_months}\n"
    f"Total : ${total_profit_losses}\n"
    f"Avarage Change: ${avarage_change:.2f}\n"
    f"Greatest Increase in Profits: {increase_date} (${greatest_increase}\n)"
    f"Greatest Decrease in Proits: {decrease_date} (${greatest_decrease})"
)

#printing the analysis on a seperate txt file 

with open('financial_analysis.txt', 'w') as file:
    file.write(analysis)
