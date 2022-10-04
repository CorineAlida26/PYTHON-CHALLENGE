#Dependencies 

import os
import csv

#variables
v_candidates = []
v_per_candidate = []
T_votes = 0
c_votes = {}
#create path 

election_data = os.path.join("Resources", "election_data.csv")

#open & read csv

with open(election_data, newline="") as csvfile:


    csvreader = csv.reader(csvfile, delimiter=",")

#Read first row

    csv_header = (next(csvreader))

#print 
    print(f"Header: {csv_header}") # print Ballot ID,County,Candidate

    csvreader_2 = list(csvreader)
    print(csvreader_2)

#Read data fater header
for row in csvreader_2:

    # number of votes
    T_votes += 1
    
    v_per_candidate = row[2]


    if v_per_candidate in c_votes:

       c_votes [v_per_candidate] ["votes"] += 1
    else:
        c_votes [v_per_candidate] = {"votes": 1, 'percent': 0 }

#winner calculation in percentage

w_votes = 0
w_percent = 0      

for v_per_candidate in c_votes:
    votes = c_votes[v_per_candidate] ["votes"]
    v_percent = round (votes / T_votes *100, 2)
    c_votes [v_per_candidate]["percent"] = v_percent

    if votes > w_votes:
        w_votes = votes
        w = winner = v_per_candidate
        w_percent = v_percent

#Print Analysis

print("-----------------------")
print("Election Results")
print("------------------------")
print(f"Total Votes : "+ str (T_votes))
print("------------------------")

for v_per_candidate in c_votes:

    print(f'{v_per_candidate}: {c_votes[v_per_candidate]["percent"]}% ({c_votes[v_per_candidate]["votes"]})')
print("-----------------------")

print(f"Winner:{winner}")

#export file
f = open("election_data.txt", "w")
f.write ("Election Results")
f.write('\n')
f.write("-----------------------")
f.write('\n')
f.write(f"Total Votes : "+ str (T_votes))
f.write('\n')
f.write("-----------------------")
f.write('\n')

for v_per_candidate in c_votes:

    print(f'{v_per_candidate}: {c_votes[v_per_candidate]["percent"]}% ({c_votes[v_per_candidate]["votes"]})')
    f.write('\n')

f.write("-----------------------")
f.write('\n')
print(f"Winner:{winner}")
f.write('\n')