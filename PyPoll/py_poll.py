import os
import csv

count = 0
candidatelist = []
vote_count = []
unique_candidate = []
vote_percentage = []
winning_count = []

electiondata_csv = "/Users/mackenzie/python-challenge/PyPoll/Resources/election_data.csv"

with open(electiondata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    print(header)

    for row in csvreader:
        # Count the votes
        count = count + 1
        # Set candidate names
        candidatelist.append(row[2])

    # Create a set from the candidatelist to get unique names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the variable to represent total votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)

        # z is percent totals
        z = (y / count) * 100
        vote_percentage.append(z)

    winning_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_count)]

    print("----------------")
    print("Election Results")
    print("----------------")
    print("Total Votes: " + str(count))
    print("----------------")

    # Verify lengths
    if len(unique_candidate) == len(vote_percentage) == len(vote_count):
        for i in range(len(unique_candidate)):
            print(f"{unique_candidate[i]}: {vote_percentage[i]:.3f}% ({vote_count[i]})")
    else:
        print("Error: Lists have different lengths.")

    print("----------------")
    print("The winner is: " + winner)
    print("----------------")

    #run in txt file
    with open('election_data.txt', 'w') as text:
        text.write("Election Results\n")
        text.write("---------------------------------------\n")
        text.write("Total Vote: " + str(count) + "\n")
        text.write("---------------------------------------\n")
        for i in range(len(set(unique_candidate))):
            text.write(unique_candidate[i] + ": " + str(vote_percentage[i]) + "% (" + str(vote_count[i]) + ")\n")
            text.write("---------------------------------------\n")
            text.write("The winner is: " + winner + "\n")
            text.write("---------------------------------------\n")