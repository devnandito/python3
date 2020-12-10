import pandas as pd

fopen = input('Enter file: ')
df1 = pd.read_excel(fopen)
list1 = df1.to_dict(orient='records')
print(df1.columns.ravel())
print('Total records:', len(list1))
df0 = pd.read_excel(fopen, usecols=['RUC', 'NOMBRE '])
print(df0)
# print(df0)
# print(df0['RUC'].tolist())
# print('Excel Sheet to Dict:', df0.to_dict(orient='records'))
# list1 = df0.to_dict(orient='records')
