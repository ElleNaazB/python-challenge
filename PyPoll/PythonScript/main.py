import os
import pandas as pd

# Define the current directory and the relative path to the CSV
CURRENT_DIR = os.path.dirname(__file__)
csvpath = os.path.join(CURRENT_DIR, '../Resources/election_data.csv')

# Load the data from the CSV file
election_data = pd.read_csv(csvpath)

# Calculating the total number of votes cast
total_votes = election_data.shape[0]

# Getting a list of unique candidates and calculating votes
candidates_votes = election_data['Candidate'].value_counts()
candidates_percentage = (candidates_votes / total_votes) * 100

# Identifying the winner of the election based on popular vote
winner = candidates_votes.idxmax()

# Preparing the results for display and export
results = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"
]

for candidate, votes in candidates_votes.items():
    results.append(f"{candidate}: {candidates_percentage[candidate]:.3f}% ({votes})")

results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Writing the results to the terminal
for line in results:
    print(line)

# Defining the output file path in PythonScript file
output_file_path = os.path.join(CURRENT_DIR, 'election_results.txt')

# Writing a code that copies the results into a text file 
with open(output_file_path, 'w') as file:
    file.write("\n".join(results))