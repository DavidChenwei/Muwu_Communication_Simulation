import pandas as pd

from simulate import samples_simulate

sourceFile = 'H:/T2.xlsx'
# use read_excel API to read data from XlSX file
communication_dict = pd.read_excel(sourceFile, header=0, usecols=[2, 8], sheet_name=None)

# the form of data is dict，it needs to get the DataFrame in the dict according to the label name of the table
communication_df = communication_dict['Sheet1']

# The unique function directly obtains the unique value of the specified column in DataFrame
store_array = communication_df['Store ID'].unique()
store_numbers = len(store_array)

all_samples = []

# Start to calculate the distribution of communication separately according to the store ID
for store in store_array:
    df = communication_df.loc[communication_df['Store ID'] == store]
    T1_se = df.groupby('communication').size()
    # Get total communications in one sheet
    total = 0
    for item in T1_se:
        total = total + item
    print('The total number of communication in store ', store, ' is ', total)

    # Get the probability of each level communication
    probabilities = []
    standard_set = {1, 2, 3, 4, 5}  # Standard score
    real_set = set()  # store the actual score
    for index, item in T1_se.iteritems():
        probabilities.append(round(item / total, 2))
        real_set.add(index)
    loss_set = standard_set - real_set

    # for item in loss_set:
    #     probabilities.insert(item - 1, 0)
    print('The probability of store ', store, ' is ', probabilities)
    print('The loss communication is : ', loss_set)

    sum = 0.0
    for item in probabilities:
        sum = sum + item
    print('The total of each probability is ', sum)

    # begin to simulate data
    Offset = len(loss_set) + 1
    samples = samples_simulate(probabilities, total, 10000, Offset)
    print('-------------------------------------------------------')
    all_samples.extend(samples)

print(all_samples)
print(all_samples.__len__())

table_df = pd.read_excel(sourceFile, header=0, sheet_name='Sheet1')
for index in table_df.index:
    try:
        table_df.loc[index, 'communication'] = all_samples[index]
    except Exception as e:
        print(e)

table_df.to_excel('Simulated_T2_Base_each_store.xlsx')
# table_df.to_excel('Simulated_T1_Base_each_store.xlsx')