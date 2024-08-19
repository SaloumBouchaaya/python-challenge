import os
import csv

csvpath= "C:\\Users\\bouch\\OneDrive\\Desktop\\Starter_Code\\Starter_Code\\PyPoll\\Resources\\election_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    print(csvreader)
    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)

row_count=0
with open(csvpath, newline='') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        row_count += 1
print(f"Total Votes: {row_count - 1}")







