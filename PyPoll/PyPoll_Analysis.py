# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
election_data = os.path.join("Resources", "election_data.csv")  # Input file path
election_analysis = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast


# Define lists and dictionaries to track candidate names and vote counts
candidates = []  # List for candidate names
candidate_votes = {}  # Dictionary for votes for each candidate

# Winning Candidate and Winning Count Tracker
winning_candidate = ""  # Canidate with the most votes
winning_count = 0  # Highest vote count
winning_percentage = 0  # Highest vote percentage

# Open the CSV file and process it
with open(election_data) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)  # Add new candidate to the list
            candidate_votes[candidate_name] = 0  # Initialize new canidate vote count

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1  # Increment vote count for the candidate

# Create output for loop
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"  # Display the total number of votes cast
    f"-------------------------\n"
)

# Open a text file to save the output
with open(election_analysis, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(output)

    # Write the total vote count to the text file
    txt_file.write(output)

 # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]  # Get the vote count for the candidate
        vote_percentage = (votes / total_votes) * 100  # Calculate the vote percentage

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes  # Update the highest vote count
            winning_candidate = candidate  # Update the winning candidate name
            winning_percentage = vote_percentage  # Update the winning percentage

        # Print and save each candidate's vote count and percentage
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results)  # Display candidate's results
        txt_file.write(candidate_results)  # Save candidate's results to the text file

    # Generate and print the winning candidate summary
    winning_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"  # Display the name of the winning candidate
        f"Winning Vote Count: {winning_count}\n"  # Display the vote count of the winner
        f"Winning Percentage: {winning_percentage:.3f}%\n"  # Display the vote percentage of the winner
        f"-------------------------\n"
    )

    # Print the winner summary
    print(winning_summary)

    # Save the winning candidate summary to the text file
    txt_file.write(winning_summary)  # Ensure this is inside the 'with' block