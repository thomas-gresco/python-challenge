import csv 
from pathlib import Path
import os

input_file = Path("election_data.csv")
out_file = Path("result_PyPoll.txt")

# Define variables
total_votes = 0
candidates = {}
winner_votes = 0
winner_name = ""

with open(input_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # Loop through candidates
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        # If the candidate is in dictionary then add to vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# Loop through the candidates dictionary and calculate their percentage of the total vote and total votes received
for candidate in candidates:
    vote_count = candidates[candidate]
    vote_percentage = vote_count / total_votes * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({vote_count})")
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner_name = candidate
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")


with open(out_file, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate in candidates:
        vote_count = candidates[candidate]
        vote_percentage = vote_count / total_votes * 100
        output_file.write(f"{candidate}: {vote_percentage:.3f}% ({vote_count})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner_name}\n")
    output_file.write("-------------------------")