import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# TODO function for exponential smoothing

# TODO function for SSE retrieval

# TODO function for retieving the best alpha based on notes

df = pd.read_csv('algerian.txt' ,header=None)

cols = ['year', 'value']

# insert a column with values starting from 1960
df.insert(0, 'year', range(1960, 1960 + len(df)))
df.columns = cols
# plot the data nased on the year and the value
# plt.plot(df['year'], df['value'])
df[f'time'] = pd.to_datetime(df['year'],  format='%Y')
df.drop('year', axis=1, inplace=True)
df.set_index('time', inplace=True)

print(df.head())
print(df)
df.plot()

