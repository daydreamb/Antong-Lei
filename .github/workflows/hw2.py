import pandas as pd
import numpy as np

#1
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered_df = df[['Manufacturer', 'Model', 'Type']].iloc[::20]

#2
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)

#3
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rows_sum_gt_100 = df[df.sum(axis=1) > 100]

#4
arr = np.random.randint(1, 100, (4, 4))
rows_array = arr.reshape(2, 2, 4).sum(axis=1)
columns_array = arr.reshape(2, 2, 4).sum(axis=0)

sum_row_col = lambda arr: (np.sum(arr, axis=1), np.sum(arr, axis=0))
row_sum, col_sum = sum_row_col(arr)
