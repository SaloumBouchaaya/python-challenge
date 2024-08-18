import os
import csv

csvpath =os.path.join("..", 'Class_Folder','Starter_Code (1)', 'Starter_Code','PyBank', 'Resources', 'budget_data')

with open(csvpath) as csvfile:
    print(csvreader)
    csv_header=next(csvreader)
    print(f"CSV Header:{csvreader}")

    for row in csvreader:
        print(row)


