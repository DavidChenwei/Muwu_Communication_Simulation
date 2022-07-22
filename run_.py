import random

import pandas as pd

from simulate import samples_simulate

sourceFile = 'Simulated_T2(old).xlsx'
conmunication_df = pd.read_excel(sourceFile, header=0, usecols=[8], sheet_name=None)
T1_se = conmunication_df['Sheet1'].groupby('communication').size()

# Get total communications in one sheet
total = 0
for item in T1_se:
    total = total + item
print('The total number of communications is ', total)

# Get the probability of each level communication
probabilitis = []
for item in T1_se:
    probabilitis.append(round(item / total, 2))

print('The probability of the sheet is ', probabilitis)

# Check whether the sum of probabilities is 1
sum = 0.0
for item in probabilitis:
    sum = sum + item

print('The total of each probability is ', sum)

# simulate

samples = samples_simulate(probabilitis, 20299, 1000000, 1)

table_df = pd.read_excel(sourceFile, header=0, sheet_name='Sheet1')

for index in table_df.index:
    try:
        table_df.loc[index, 'communication'] = samples[index]
    except Exception as e:
        print(e)

# table_df.to_csv('Simulated_T1.csv')
# table_df.to_excel('Simulated_T2.xlsx')