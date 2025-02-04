# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# source to read data
budget_data = os.path.join("Resources", "budget_data.csv")  # Input file path

#create file to hold the output
outputfile = os.path.join("budget_data.txt") # Output file path

# Define variables to track the financial data
total_months = 0 
total_net = 0

#create empty lists to hold data
months = []
net_change_list = []


# Open and read the csv
with open(budget_data) as financial_data:
    #create csv reader
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1 #count first month
    total_net += int(first_row[1]) #add P&L for first month
    prev_net = int(first_row[1]) #Create net for first change
    months.append(first_row[0]) # Add the first month to list

    #start to loop through data
    for row in reader:

        # Track the total months and total P&L
        total_months += 1
        total_net += int(row[1])
        months.append(row[0])

        # Track the net change
        net_change = int(row[1]) - prev_net
        net_change_list.append(net_change) # Include change in the list
        prev_net = int(row[1]) #update the net for next iteration of the loop

# Calculate the greatest increase in profits (month and amount)
greatest_increase = max(net_change_list) #find greatest increase amount
greatest_increase_month = months[net_change_list.index(greatest_increase) + 1] #find greatest increase month

# Calculate the greatest decrease in losses (month and amount)
greatest_decrease = min(net_change_list) #find greatest decrease amount
greatest_decrease_month = months[net_change_list.index(greatest_decrease) + 1] #find greatest decrease month

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    f"Financial Data Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"  # Print total months
    f"Total: ${total_net}\n"  # Print total profit/loss
    f"Average Change: ${average_change:.2f}\n"  # Print average change in P&L
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"  # Print greatest profit increase
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"  # Print greatest profit decrease
)

# Print the output
print(output)

# Write the results to a text file
with open("budget_data.txt", "w") as txt_file:
    txt_file.write(output)
