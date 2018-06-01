# Import Files
import os
import csv
import pandas as pd
ED1_csv = os.path.join("election_data_1.csv")
ED1_pd = pd.read_csv(ED1_csv)
ED1_pd.head(10)
TotalCounts = ED1_pd['Voter ID'].count()
print('-----------------------------')

# The total number of votes cast
print('Total Votes: '+ str(TotalCounts))
print('-----------------------------')

# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
CandidateCounts = ED1_pd['Candidate'].value_counts()
CandidateCounts
PercentageVotes = round((CandidateCounts/TotalCounts)*100,0)
(PercentageVotes)
Summary = pd.concat([PercentageVotes, CandidateCounts], axis=1)
Summary
Summary.columns=['Percentage', 'Total Votes']
Summary.columns
NewSummary = Summary[['Percentage', 'Total Votes']]
print(NewSummary)
winner = NewSummary['Percentage'].sort_values(ascending=False)
WinnerName = winner.index[0]
print('-----------------------------')

# The winner of the election based on popular vote.
print('Winner: '+WinnerName)

# Output to Text File
f= open('main.txt', 'w')
f.write('-----------------------------\n')
f.write('Total Votes: '+ str(TotalCounts))
f.write('-----------------------------\n')
f.write(str(NewSummary))
f.write('-----------------------------\n')
f.write('Winner: '+WinnerName)
f.close()

