import pandas as pd

df = pd.read_csv('Data.csv',sep='|')
print(df[df.columns.to_list()[1]].values[5])