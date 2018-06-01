# Import Files
import os
import pandas as pd
import csv
budget_csv = os.path.join("budget_data_1.csv")
budget_pd = pd.read_csv(budget_csv)
budget_pd.head()

print('-----------------------------')

print('Financial Analysis')

print('-----------------------------')
# Total Months
TotalCounts = budget_pd['Date'].count()
print('Total Months: '+str(TotalCounts))

# Total Revenue
TotalRevenue = budget_pd['Revenue'].sum()
print('Total Revenue: $'+str(TotalRevenue))

AvgRevenueDelta = budget_pd['Revenue'].diff()
AvgRevenueDelta.head()

# Average Revenue Change
Average = AvgRevenueDelta.mean()
print('Average Revenue Change: $'+str(Average))

# Greatest Increase/Decrease in Revenue
budget_pd['Diff']= budget_pd['Revenue']-budget_pd['Revenue'].shift(1)
diff_budget = budget_pd.head(10)
new_diff = diff_budget.drop(columns=['Revenue'])
new_diff.head()

# Greatest Increase in Revenue
max = new_diff.loc[new_diff['Diff'].idxmax()]
print(max)

# Greatest Decrease in Revenue
min = new_diff.loc[new_diff['Diff'].idxmin()]
print(min)

print('-----------------------------')

# Output to Text File
f= open("main.txt","w")
f.write("-----------------------------\n")
f.write("Financial Analysis\n")
f.write("-----------------------------\n")
f.write('Total Months: '+str(TotalCounts))
f.write('Total Revenue: $'+str(TotalRevenue))
f.write('Average Revenue Change: $'+str(Average))
f.write(str(max))
f.write(str(min))
f.write("-----------------------------\n")
f.close()