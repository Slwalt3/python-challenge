import os
import csv
csvpath = os.path.join('python-challenge','PyPoll','Resources','election_data.csv')
candidates = []
all_candidates = []
percent_list = []
data = {}
total = 0
with open(csvpath) as csvfile:
    csvreader =csv.reader(csvfile)
    for row in csvreader:
        total+=1
        all_candidates.append(row[2])
        if row[2] in candidates:
            continue
        else:
            candidates.append(row[2])
    total-=1
for i in range(1,len(candidates)):
    count = 0
    for j in range(len(all_candidates)):
        if candidates[i]==all_candidates[j]:
            count+=1
    data[candidates[i]]= count
candidates.remove(candidates[0])
