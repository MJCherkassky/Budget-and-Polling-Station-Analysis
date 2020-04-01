# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The percentage of votes each candidate won
#The winner of the election based on popular vote.
import os
import csv
votes = {} #Set up a dictionary for candidates as key and vote count as value
csvpath = os.path.join("..", "..", "..", "Classwork", "vu-nsh-data-pt-02-2020-u-c", "03-Python", "Homework", "Instructions", "PyPoll", "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        candidate = row[2]
        if candidate in votes.keys(): #for each row in the data, compile a list of unique values from all rows #A complete list of candidates who received votes
            votes[candidate] += 1
        else:
            votes[candidate] = 1
    total_votes=sum(votes.values()) #Total number of votes cast
    winner = max(votes, key=votes.get)
    statement1 = f"""
Election Results \n~~~~~~~~~~~~~~~
Total Votes: {total_votes}\n~~~~~~~~~~~~~~~
    """
    statement2 = f"""
~~~~~~~~~~~~~~~\nWinner: {winner} \n~~~~~~~~~~~~~~~
    """
    print(statement1)    
    if not os.path.isdir("Output"):
        os.mkdir("Output")
    else:
        pass  
    output_path = os.path.join("Output", "ElectionResults.txt")
    with open(output_path, "w+") as writedata:
        writedata.writelines(statement1)
        for i in votes:
            popularvote = (votes[i]/total_votes)
            print(f"{i} : {popularvote:.3%} ({votes[i]})")
            writedata.writelines(f"""
{i}: {popularvote:.3%} ({votes[i]})""") #The total number of votes for each candidate 
        winner = max(votes, key=votes.get)
        writedata.writelines(statement2)
print(statement2)