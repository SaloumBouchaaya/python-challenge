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

# Calculate amount of months/rows
row_count = 0
with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        row_count += 1
print(f"Total Months: {row_count-1}")

# Add total of Profit/Loss
total_sum = 0
with open(csvpath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        total_sum += float(row['Profit/Losses'])
print(f"Total:","$", {total_sum})

# Calculate average change in Profit/Loss
profit_losses_change = []
with open(csvpath, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        profit_losses_change.append(float(row['Profit/Losses']))
changes=[]
for i in range(1,len(profit_losses_change)):
    change = profit_losses_change[i] - profit_losses_change[i-1]
    changes.append(change)
average_change = sum(changes)/len(changes)
print("Average Change:", "$" , average_change)


# Find Greatest Increase in Profits
pl=[]
month=[]
with open(csvpath, newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        pl.append(float(row['Profit/Losses']))
        month.append(row['Date'])
    
change=[pl[i]-pl[i-1] for i in range(1,len(pl))]
greatest_inc=max(change)
greatest_inc_index=change.index(greatest_inc)+1
greatest_increase_date=month[greatest_inc_index]

print(f"Greatest Increase in Profits:", {greatest_increase_date}, "$",{greatest_inc})


# Find Greatest Decrease in profits
pl=[]
month=[]
with open(csvpath, newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        pl.append(float(row['Profit/Losses']))
        month.append(row['Date'])
    
change=[pl[i]-pl[i-1] for i in range(1,len(pl))]
greatest_dec=min(change)
greatest_dec_index=change.index(greatest_dec)+1
greatest_decrease_date=month[greatest_dec_index]

print(f"Greatest Decrease in Profits:", {greatest_decrease_date}, "$",{greatest_dec})
