#PyPoll: Smalltown, USA voting analysis
#Import dependent modules
import os
import csv

#set path for input and output csv file
csvpath = os.path.join("python-challenge/PyPoll/Resources/election_data.csv")

#Create file for the text output to be saved in the Analysis folder
f = open("python-challenge/PyPoll/Analysis/PyPoll_Analysis.txt", 'w')

#open the csv file for analysis
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Set variables
    vote_counter = 0
    khan_vote = 0
    correy_vote = 0
    li_vote = 0
    otool_vote = 0
    
    #Create an empty dictionary

    for row in csvreader:
        #Count total number of votes
        vote_counter += 1
        
        #Count total number of votes for each candidate
        if row[2] == "Khan":
            khan_vote += 1
        elif row[2] == "Correy":
            correy_vote += 1
        elif row[2] == "Li":
            li_vote += 1
        else:
            otool_vote += 1


    #Calculate percentages
    per_khan = round((khan_vote/vote_counter) * 100,2)
    per_cor = round((correy_vote/vote_counter) * 100,2)
    per_li = round((li_vote/vote_counter) * 100,2)
    per_otool = round((otool_vote/vote_counter) * 100,2)

    #Create final results dictionary to find winner and number of votes
    d = {"Kahn":khan_vote, "Correy":correy_vote, "Li":li_vote, "O'Toole":otool_vote}
    max_key = max(d.keys(), key=lambda x: d[x])
    max_value = d[max_key]

    #Print report to terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {vote_counter}")
    print(f"----------------------------")
    print(f"Khan: {per_khan}% ({khan_vote})")
    print(f"Correy: {per_cor}% ({correy_vote})")
    print(f"Li: {per_li}% ({li_vote})")
    print(f"O'Toole: {per_otool}% ({otool_vote})")
    print(f"----------------------------")
    print(f"Winner: {max_key} ({max_value})")
    print(f"----------------------------")
    
    #Print report to new file
    print("Election Results", file=f)
    print("----------------------------", file=f)
    print(f"Total Votes: {vote_counter}", file=f)
    print(f"----------------------------", file=f)
    print(f"Khan: {per_khan}% ({khan_vote})", file=f)
    print(f"Correy: {per_cor}% ({correy_vote})", file=f)
    print(f"Li: {per_li}% ({li_vote})", file=f)
    print(f"O'Toole: {per_otool}% ({otool_vote})", file=f)
    print(f"----------------------------", file=f)
    print(f"Winner: {max_key} ({max_value}))", file=f)
    print(f"----------------------------", file=f)
