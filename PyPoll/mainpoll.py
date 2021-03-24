# dependencies
import csv
import os

csv_filepath = os.path.join('Resources', 'election_data.csv')

vote_total = 0
candidates_names = []
candidates_votes = {}
most_votes = 0

with open(csv_filepath, newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader)
    # print(len(spamreader))
    for row in spamreader:
        vote_total += 1

        candidates = row [2]
        if candidates not in candidates_names:
            candidates_names.append(candidates)
            candidates_votes[candidates] = 0
        candidates_votes[candidates] +=1

for key, value in candidates_votes.items():
    vote_total_percentage=value/vote_total
    print (f"{key}, {vote_total_percentage:.2%}")
    if value > most_votes:
        most_votes=value
        print(f"{key}:{most_votes}")
print(most_votes)
