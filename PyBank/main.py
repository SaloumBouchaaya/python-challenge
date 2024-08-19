import os
import csv

csvpath = "C:\\Users\\bouch\\OneDrive\\Desktop\\Starter_Code\\Starter_Code\\PyBank\\Resources\\budget_data.csv"


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)


row_count = 0
with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        row_count += 1
print(f"Total Months: {row_count-1}")


total_sum = 0
with open(csvpath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        total_sum += float(row['Profit/Losses'])
print(f"Total:","$", {total_sum})


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



with open(csvpath, 'r') as csvfile:
    reader = csv.reader(csvfile)
























#date = []
#profit_loss = []
#with open(csvpath, newline='') as csvfile:
 #   reader = csv.DictReader(csvfile)
  #  for row in reader:
   #     date.append(row['Date'])
    #    profit_loss.append(float(row['Profit/Losses']))
     #   for i in range(1,len(values)):
      #      changes = [profit_loss[i] - profit_loss[i-1] for i in range(1,len(values))]
       #     greatest_increase = max(changes)
        #    greatest_increase_index = changes.index(grastest_increase) + 1

#date_greatest_increase = dates[greatest_increase_index]

#print(f"Greatest Increase in profits:", {date_greatest_increase}, "$", {greatest_increase})



    
                                     






                                                                                                    



