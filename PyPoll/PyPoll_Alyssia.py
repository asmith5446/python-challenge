import csv
import os

PyPoll_csv = os.path.join("election_data.csv")

with open(PyPoll_csv, newline='') as PyPoll_csv:
    csvreader = csv.reader(PyPoll_csv, delimiter=',')
    csv_header = next(csvreader)

    votes_cast = []
    candidates_list = []
    unique_candidate = []
    vote_percent = []

    count = 0
   

    for row in csvreader:
        count = count + 1
        votes_cast.append(row[0])

    for row in csvreader:
        count = count + 1
        candidate_list.append(row[2])

    for a in set(candidates_list):
        unique_candidate.append(a)

        b = candidates_list.count(a)
        votes_cast.append(b)

        c = (b/count)*100
        vote_percent.append(c)


    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

print("------------------------------")
print("Election Results")
print("------------------------------")
print("Total Votes: " + str(count))
print("------------------------------")

for i in range(len(unique_candidate)):
    print(unique_candidate[i] + ":" + str(vote_percent[i]) + "% (" + str(votes_cast [i]) + ")")

print("------------------------------")
print("Winner: " + str(winner)
