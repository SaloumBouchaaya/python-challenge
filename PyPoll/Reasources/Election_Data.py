# Import Module & CSV Files
import os
import csv

# Create a path to data file
csvpath= "C:\\Users\\bouch\\OneDrive\\Desktop\\Starter_Code\\Starter_Code\\PyPoll\\Resources\\election_data.csv"

# Open path as a CSV file, identify header & loop
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    print(csvreader)
    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)







