import os
import csv
from collections import Counter

# Define the current directory and the relative path to the CSV
CURRENT_DIR = os.path.dirname(__file__)
csvpath = os.path.join(CURRENT_DIR, '../Resources/election_data.csv')

# Initialize a dictionary to count votes for each candidate
candidate_votes = Counter()

# Reading the CSV file
with open(csvpath, mode='r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        candidate_votes[row['Candidate']] += 1

# Calculating the total number of votes casted
total_votes = sum(candidate_votes.values())

# Calculating percentages
candidates_percentage = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Identifying the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Preparing the results for display and export
results = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"
]

for candidate, votes in candidate_votes.items():
    results.append(f"{candidate}: {candidates_percentage[candidate]:.3f}% ({votes})")

results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Writing the results into the terminal
for line in results:
    print(line)

# Defining the output file path
output_file_path = os.path.join(CURRENT_DIR, 'election_results.txt')

# Writing the results to the text file 
with open(output_file_path, 'w') as file:
    file.write("\n".join(results))
