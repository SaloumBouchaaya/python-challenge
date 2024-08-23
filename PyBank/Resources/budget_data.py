# Import module & csv
import os
import csv

# Create a path to file
csvpath = "C:\\Users\\bouch\\OneDrive\\Desktop\\Starter_Code\\Starter_Code\\PyBank\\Resources\\budget_data.csv"

# Open, read,loop file and identify header

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)


# THIS WILL OPEN THE PATH TO OUR DATA FILE
        




