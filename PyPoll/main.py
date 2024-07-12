#Create a Python Script that analyzes the records to calculate the following:
import os
import csv
import statistics
import sys

#Select where the data lives
data_folder = "Resources"
poll_data_csv = os.path.join(os.getcwd(), data_folder, "election_data.csv")

#Set variables
total_votes = []
candidate_votes = []
percentage_votes = []
winner = ""


#Store the text output/set output variable
output_text = ""

with open(poll_data_csv) as csvfile:

    #Specify the delimiter and variable
    csvreader = csv.reader(csvfile, delimiter= ',')

    #Read the Header Row
    csv_header = next(csvreader)

    for row in csvreader:

        #Total Number of Votes cast
        total_votes.append(row[0])

#Print the total votes
print(f"Total Votes: {len(total_votes)}")
output_text += f"Total Votes: {len(total_votes)}\n"

# Complete list of candidates who received votes & The percentage of votes each candidate won
#Calculate for total votes
total_votes = 0
candidate_votes = {}
with open(poll_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_reader = next(csvreader)

    for row in csvreader:
    #Count votes for each candidate
        #Total Number of Votes Cast
        total_votes += 1
        #Notate where the candidates names are located
        candidate_name = row[2]
        #See how many votes each candidate has; check to see if the candidate name 
        # is a key in the votes dictionary, if it is then candidate has had a vote before.
        if candidate_name in candidate_votes:
            #If the candidate is in the dictionary, it will add 1 vote to the count
            candidate_votes[candidate_name] += 1
        #Otherwise it sets the vote count to just 1
        else:
            candidate_votes[candidate_name] = 1

#Calculate the percentage of votes for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes/total_votes) * 100
    candidate_name = ""
    if candidate == "Charles Casper Stockham":
        candidate_name = "Charles Casper Stockham"
    elif candidate == "Diana Degette":
        candidate_name = "Diana Degette"
    elif candidate == "Raymon Anthony Doane":
        candidate_name = "Raymon Anthony Doane"


    #Print the percentage of votes for each candidate
    print(f"{candidate}: {percentage: .3f}% ({votes})")
    output_text += f"{candidate}: {percentage: .3f}% ({votes})\n"

# The winner of the election based on popular vote
#select the winner by collecting the candidate with the most votes, or max number of votes
#Assign the key (candidate name) corresponding to the max value (most votes)
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winnder: {winner}")
output_text += f"Winner: {winner}\n"


#Be sure that the analysis prints to the terminal and exports a text file with the results
analysis_folder = "Analysis"
output_file = os.path.join(analysis_folder, "election_results.txt")
print(output_text)
with open(output_file, "w") as file:
    file.write(output_text)