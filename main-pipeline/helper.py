import pandas as pd

raw_data = pd.read_csv('../data/raw_data.csv')
print(raw_data.shape)

fifty_rows = raw_data.iloc[0:50, ]
print(fifty_rows.info())