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

# Calculate Total Votes
row_count=0
with open(csvpath, newline='') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        row_count += 1
print(f"Total Votes: {row_count - 1}")

# Initialize count & Vote
vote_counts={}
total_votes=0

# Loop Candidates & Get vote count
with open (csvpath, 'r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        candidate=row['Candidate']
        current_count=vote_counts.get(candidate,0)
        vote_counts[candidate]=current_count+1

        total_votes += 1

# Intialize, calculate & assigen percentages
percentages = {}
winner = None
max_votes = 0

for candidate, count in vote_counts.items():
    if total_votes>0:
        percentage=(count/total_votes)*100
    else:
        percentage=0

    percentages[candidate]=percentage

# Find max votes & identitfy winner
    if count>max_votes:
        max_votes=count
        winner=candidate

for candidate in vote_counts:
    count=vote_counts[candidate]
    percentage= f"{percentages[candidate]:.3f}%"

# Print out results

    print(f"{candidate}: ,{count},{percentage} ")

print(f"Winner: {winner}")


      












