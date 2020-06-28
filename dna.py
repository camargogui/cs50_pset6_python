#data: https://cdn.cs50.net/2019/fall/psets/6/dna/dna.zip

import math
import pandas as pd
from sys import argv, exit


if len(argv) != 3:
    print('Missing a valid command-line argument.')
    exit(1)

dataframe = pd.read_csv(f'{argv[1]}')
with open (f'{argv[2]}', 'r') as file:
    content = file.read()

count = 0
result = {}
list_name = []

for i in range(1,dataframe.shape[1]):
    for j in range(math.ceil(len(content)/4)):
        if (dataframe.columns[i]*j) in content:
            temp = {dataframe.columns[i]: j}
        result.update(temp)
for i in range(dataframe.shape[0]):
    for j in range(1,dataframe.shape[1]):
        if dataframe.loc[i][dataframe.columns[j]] != result[dataframe.columns[j]]:
            break
        else:
            count += 1
    if count == (dataframe.shape[1]-1):
        list_name = dataframe.name[i]
        break
    count = 0
if not list_name:
    print(f'No match')
else:
    print(f'{list_name}.')