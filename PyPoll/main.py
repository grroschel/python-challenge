##########
# PyPoll #
##########

# ------------------------
# Calculate the following:
# ------------------------
# You will be given a set of poll data called election_data.csv. The dataset is composed of
# three columns: Voter ID, County, and Candidate. Your task is to create a Python script that
# analyzes the votes and calculates each of the following:
#   The total number of votes cast
#   A complete list of candidates who received votes
#   The percentage of votes each candidate won
#   The total number of votes each candidate won
#   The winner of the election based on popular vote.

# --------------------
# Initialize variables
# --------------------
total_vote_count = 0
candidates_voted_for = []
winners_count = 0
winners_name = ""
unique_candidates = []

# ---------------------------------------
# Get set up to Read in election_data.csv
# ---------------------------------------
# C:\# Gregs Temp\Rice U DABC\#5 - Rice U DABC - Homework\Rice U DABC Homework #03 - Python\
# election_data.csv
import os
import csv
csvpath = os.path.join('C:', '/', '# Gregs Temp', 'Rice U DABC', '#5 - Rice U DABC - Homework',
                        'Rice U DABC Homework #03 - Python', 'election_data.csv')

# ------------------------------
# Read in & Process the csv file
# ------------------------------
with open(csvpath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first to position ourselves for processing the data
    # This file does have a header row
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for csvrow in csvreader:
        
        # Save the name of the candidate voted for from the 3rd column
        candidates_voted_for.append(csvrow[2])
        
# ------------------------------------------------
# We're all done processing rows from the csv file
# Calculate the total votes
# ------------------------------------------------
total_vote_count = len(candidates_voted_for)

# ---------------------------------
# Build the Election Results report
# ---------------------------------

# ------------------------------------------------------------------------------
# Since we're writing the Election Results to a text file as well as printing it
# to the terminal, prepare the Election Results report lines first
# ------------------------------------------------------------------------------
line1 = ("Election Results")
line2 = ("-" * 25)
formatted_total_vote_count = format(len(candidates_voted_for), ',d')
line3 = ("Total Votes: " + str(formatted_total_vote_count))
line4 = ("-" * 25)

# ---------------------------------------------------------------------
# Print the initial part of the Election Results report to the terminal
# ---------------------------------------------------------------------
print("")
print(line1)
print(line2)
print(line3)
print(line4)

# ----------------------------------------------------------------------
# Write the initial part of the Election Results report to the text file
# ----------------------------------------------------------------------
filepath = os.path.join('C:', '/', '# Gregs Temp', 'Rice U DABC', '#5 - Rice U DABC - Homework',
                        'Rice U DABC Homework #03 - Python', 'election_results.txt')
txtfile = open(filepath, "w")
txtfile.write(line1)
txtfile.write("\n" + line2)
txtfile.write("\n" + line3)
txtfile.write("\n" + line4)
# Write individual candidate totals here

# -----------------------------------------------------------------------------------
# Print/Write each candidates vote count & percentage to the terminal & the text file
# -----------------------------------------------------------------------------------
for candidate in candidates_voted_for:

    if candidate not in unique_candidates:

        # Stick him or her in there
        unique_candidates.append(candidate)

        # Calculate the candidates vote count & percentage
        candidate_count = candidates_voted_for.count(candidate)
        candidate_percentage = ((candidate_count / total_vote_count) * 100)

        # Save the potential winner's name
        if candidate_count > winners_count:
            winners_name = candidates_voted_for[0]
            # There's no need to save the winner's count

        # Print & write each candidate's name with their vote "count" & "percent"
        # First, format those numbers nicely
        candidate_percentage = format(candidate_percentage, ',.2f')
        candidate_count = format(candidate_count, ',d')
        linea = (candidate + ": " + str(candidate_percentage) + "% (" + str(candidate_count) + ")")
        print(linea)
        txtfile.write("\n" + linea)
        
# --------------------------------------------------------
# Build the remaining lines of the Election Results report
# --------------------------------------------------------
line5 = ("-" * 25)
line6 = ("Winner: " + winners_name)
line7 = ("-" * 25)

# -----------------------------------------------------------
# Finish printing the Election Results report to the terminal
# -----------------------------------------------------------
print(line5)
print(line6)
print(line7)

# -----------------------------------------------------------
# Finish writing the Election Results report to the text file
# -----------------------------------------------------------
txtfile.write("\n" + line5)
txtfile.write("\n" + line6)
txtfile.write("\n" + line7)
txtfile.close()

# End of PyPoll program
