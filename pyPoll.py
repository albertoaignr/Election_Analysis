# Add our dependencies 
import csv

import os

# Assign a variable to load a file from a path

file_to_load = os.path.join("Resources","election_results.csv")

# Assing a variable to save the file to a path

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize the total vote counter

total_votes = 0

candidate_options = []

# Declare an empy dictionary

candidate_votes = {}

#Winning candidate and winning count tracker 

winning_candidate = ""

winning_count = 0

winning_percentage = 0 

# Open the election results and read the file 

with open(file_to_load) as election_data:

# To do: Read and analyze data here 

    file_reader = csv.reader(election_data)

# Read and print header row

    headers = next(file_reader)

    print(headers)

# Print each row in the CSV file

    for row in file_reader:

        # Add to the total vote count

        total_votes += 1

        # Print the candidate name from each row 

        candidate_name = row[2]

        # If candidate do not match any existing candidate

        if candidate_name not in candidate_options:
        
        # Add the candidate name to the candidate list 
            candidate_options.append(candidate_name)

        # Begin tracking of candidate name votes 

            candidate_votes[candidate_name]=0

        # Add a vote for each candidate name

        candidate_votes[candidate_name]+=1

        # Determine tthe percentage of votes for each candidate by looping through the counts 

        # Iterate through the candidate list 

    for candidate_name in candidate_votes:

            # Retrieve vote count of a candidate 

            votes = candidate_votes[candidate_name]

            # Calculate the percentage of votes 

            vote_percentage = float(votes) / float(total_votes) * 100

            #  Print the candidate name and percentage of votes 
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #print(f"{candidate_name}: received {round(vote_percentage,2)}% of the vote")
     
            # Determine winning vote count and cadidate 
    
            # Determine if votes is greater than the winning count 

            if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentag
             winning_count = votes

             winning_percentage = vote_percentage

            # Set winning candidate to candidate name 

             winning_candidate = candidate_name

            # to do: print winning count / percentage and candidate name 

            # To do: print out each candidate's name, vote count, and percentage of
           
            # votes to the terminal.
            
    

    winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
    print(winning_candidate_summary)
        
        




