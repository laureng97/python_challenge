# Create a Python Script that analyzes the records to calculate the following:
import os
import csv
import statistics 
import sys
# Select where the data lives
data_folder = "Resources"
budget_data_csv = os.path.join(os.getcwd(), data_folder, "budget_data.csv")

#Set my Variables
total_months = []
total_profits = []
profit_changes = 0
monthly_changes = []
change = 0
#Store all the text output
output_text = ""

with open(budget_data_csv) as csvfile:

    #Specify the delimiter and variable
    csvreader = csv.reader(csvfile, delimiter= ',')

    #Read the header row 
    csv_header = next(csvreader)

    for row in csvreader:

    #Total Number of Months included in the data set
        total_months.append(row[0])
        total_profits.append(row[1])
    #Print the total months
    print(f"Total Months: {len(total_months)}")
    output_text += f"Total Months: {len(total_months)}"     

    # Net total amount of Profit/Losses over the entire period
    total_profits = [int(x) for x in total_profits]
    total_profits_sum = sum(total_profits)
    #Print the Total Amount of Profit/Losses
    print(f"Total: ${total_profits_sum} ")
    output_text += f"Total: ${total_profits_sum} "

# The changes in Profit/Losses over the entire period, and then the AVERAGE of those changes
for i in range(len(total_profits)-1):
    #Difference amongst two months and append to monthly profit changes
    monthly_changes.append(total_profits[i+1]-total_profits[i])

#Calculate the average of the changes in profit/losses
average_change = statistics.mean(monthly_changes)
#Round the average changes to two decimal places
average_change_rounded = round(average_change, 2)
#Print the average of changes in Profit/Losses
print(f"Average Change: ${average_change_rounded}")
output_text += f"Average Change: ${average_change_rounded}"

# The greatest increase in profits (date and amount) over the entire period
#Set the greatest increase to the biggest amount listed in monthly changes
greatest_increase = max(monthly_changes)
#Index the greatest increase value
greatest_increase_index = monthly_changes.index(greatest_increase)
#Find the date associated with the greatest value in the greatest increase index
date_greatest_increase = total_months[greatest_increase_index + 1]
#Print the statement showing the greatest increase and date associated with the value
print(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})")
output_text += f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})"

# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(monthly_changes)
#Index the greatest decrease value
greatest_decrease_index = monthly_changes.index(greatest_decrease)
#Find the date associated with the greatest value in the greatest decrease index
date_greatest_decrease = total_months[greatest_decrease_index + 1]
#Print the statement showing the greatest decrease and date associated with the value
print(f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})")
output_text += f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})"


# Be sure that the analysis prints to the terminal and exports a text file with the results
analysis_folder = "Analysis"
output_file = os.path.join(analysis_folder, "financial_analysis.txt")
with open(output_file, "w") as file:
    file.write(output_text)