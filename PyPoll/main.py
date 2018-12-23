# Importing Modules to use
import os
import csv

# Input and output files
inp = "election_data.csv"
out = "Election_Analysis.txt"

# declaring date and revneue lists as placeholders
Voter_ID = list()
County = list()
Candidate = list()
# UC - Unique Candiates, COU = count of uniqe candidates, POUC - % of unique candidates
UC = list()
COUC = list()
POUC = list()

# Initiating file path
csvpath = os.path.join('', 'Resources', inp)
output_path = os.path.join('', "Resources", out)

# Initiating csv reading
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Identify firs row as header
    headerline = next(csvreader)

    # identify the list for unique counts
    for line in csvreader:
        Voter_ID.append(line[0])
        County.append(line[1])
        Candidate.append(line[2])
        if line[2]not in UC:
            UC.append(line[2])
    Total_Votes = len(Voter_ID)

    # Analyzing the Count of unique candidates, percent of vode sfor unique candidates and winner. 
    for c in UC:
        COUC.append(Candidate.count(c))
        POUC.append(round(Candidate.count(c)/Total_Votes*100,2))
        Winner = UC[COUC.index(max(COUC))]

    # Printing the results on the console
    print("```text")
    print("Election Results")
    print("-----------------------------------")
    print("Total Votes: " + str(Total_Votes))
    print("-----------------------------------")
    for x in range(len(UC)):
        print(str(UC[x]) + ": " + str(POUC[x]) +"%" +" " + "(" + str(COUC[x]) + ")")
    print("")
    print("-----------------------------------")
    print("Winner: "+ str(Winner))
    print("-----------------------------------")

    # Writting data to a file using text.write
    with open(out,"w") as text_file:
        text_file.write("Election Results" + "\n")
        text_file.write("-----------------------------------" + "\n")
        text_file.write("Total Votes: " + str(Total_Votes) + "\n")
        text_file.write("-----------------------------------" + "\n")
        for x in range(len(UC)):
            text_file.write("" + str(UC[x]) + ": " + str(POUC[x]) +"%" +" " + "(" + str(COUC[x]) + ")" + "\n")
        text_file.write("-----------------------------------" + "\n")
        text_file.write("Winner: " + str(Winner) + "\n")
        text_file.write("-----------------------------------" + "\n")
