import pandas as pd, json, csv

fopen = input('Enter file: ')
df1 = pd.read_excel(fopen, header=None)
cols = df1.columns.ravel()
list1 = df1.to_dict(orient='records')
print(df1)
# df1 = pd.read_csv(fopen)
# print(cols_to_use)
# print(len(list1))
# print(df1)

# with open(fopen) as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=':')
#     next(readCSV, None) 
#     for row in readCSV:
#         row[0] = row[0].replace('"','')
#         print(row[0])
        # print(row[0], row[1], row[2])

# cols1 = [1,2,3,4,5]
# df1 = pd.read_excel(fopen, usecols=cols1)
# list1 = df1.to_dict(orient='records')
# print(list1)


# df1 = pd.read_excel(fopen)
# json1 = df1.to_json(orient='records', date_format=None)
# print(json1)

# print('Total records:', len(list1))
# df2 = pd.read_excel(fopen, header=0, usecols='A:C')
# df2 = pd.read_excel(fopen,
#                    header=1,
#                    usecols=lambda x: x.lower() in cols)
# print(df2)
# df0 = pd.read_excel(fopen, usecols=['RUC', 'NOMBRE '])
# print(df0)
# print(df0['RUC'].tolist())
# print('Excel Sheet to Dict:', df0.to_dict(orient='record'))
# list1 = df0.to_dict(orient='record')

# cols_to_use = ['item_type', 'order id', 'order date', 'state', 'priority']
# df = pd.read_excel(src_file,
#                    header=1,
#                    usecols=lambda x: x.lower() in cols_to_use)