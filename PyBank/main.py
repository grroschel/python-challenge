##########
# PyBank #
##########

# ------------------------
# Calculate the following:
# ------------------------
# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# --------------------
# Initialize variables
# --------------------
month_count = 0
total_pl = 0
greatest_increase_in_profits = 0
greatest_decrease_in_profits = 0

# -------------------------------------
# Get set up to Read in budget_data.csv
# -------------------------------------
# C:\# Gregs Temp\Rice U DABC\#5 - Rice U DABC - Homework\Rice U DABC Homework #03 - Python\budget_data.csv
import os
import csv
csvpath = os.path.join('C:', '/', '# Gregs Temp', 'Rice U DABC', '#5 - Rice U DABC - Homework', 'Rice U DABC Homework #03 - Python',
                       'budget_data.csv')

# --------------------------
# Read in & Process the file
# --------------------------
with open(csvpath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first to position ourselves for processing the data
    # This file does have a header row
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # Increment the month counter; each row is a new month
        month_count = (month_count + 1)
        # Collect the profit & loss from the 2nd column in the row
        total_pl = (total_pl + int(row[1]))
        # Collect the greatest-increase-in-profits
        if int(row[1]) > int(greatest_increase_in_profits):
            # Save that amount from the 2nd column
            greatest_increase_in_profits = row[1]
            greatest_increase_in_profits = int(greatest_increase_in_profits)
            # Save the date of the greatest-increase-in-profits from the 1st column
            giip_date = row[0]
        # Collect the greatest-decrease-in-profits
        if int(row[1]) < int(greatest_decrease_in_profits):
            # Save that amount from the 2nd column
            greatest_decrease_in_profits = row[1]
            greatest_decrease_in_profits = int(greatest_decrease_in_profits)
            # Save the date of the greatest-decrease-in-profits from the 1st column
            gdip_date = row[0]

# ------------------------------------------------------------
# We're all done processing rows from the csv file
# Calculate the average profit and loss over the entire period
# ------------------------------------------------------------
average_pl = (total_pl / month_count)
average_pl = '{:,.2f}'.format(average_pl)

# --------------------------------------------------------------------------------
# Since we're writing the Financial Analysis to a text file as well as printing it
# to the terminal, prepare the Financial Analysis report lines first
# --------------------------------------------------------------------------------
line1 = "Financial Analysis"
line2 = "------------------"
line3 = ("Total Months: " + str(month_count))
line4 = ("Total: $" + str(format(total_pl, ',d')))
line5 = ("Average Change: $" + str(average_pl))
line6 = ("Greatest Increase in Profits: " + str(giip_date) + " $" + str(format(greatest_increase_in_profits, ',d')))
line7 = ("Greatest Decrease in Profits: " + str(gdip_date) + " $" + str(format(greatest_decrease_in_profits, ',d')))

# --------------------------------------------------
# Write the Financial Analysis report to a text file
# --------------------------------------------------
filepath = os.path.join('C:', '/', '# Gregs Temp', 'Rice U DABC', '#5 - Rice U DABC - Homework',
                        'Rice U DABC Homework #03 - Python', 'financial_analysis.txt')
txtfile = open(filepath, "w")
txtfile.write(line1)
txtfile.write("\n" + line2)
txtfile.write("\n" + line3)
txtfile.write("\n" + line4)
txtfile.write("\n" + line5)
txtfile.write("\n" + line6)
txtfile.write("\n" + line7)
txtfile.close()

# ---------------------------------------------------
# Print the Financial Analysis report to the terminal
# ---------------------------------------------------
print("")
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)

# End of PyBank program
