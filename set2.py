mport pandas as pd, sqlite3

conn = sqlite3.connect('set.sqlite')
cur = conn.cursor()

fopen = input('Enter file: ')
df0 = pd.read_excel(fopen, usecols=['RUC', 'NOMBRE '])
list1 = df0.to_dict(orient='records')
for line in list1:
    ruc = line['RUC']
    name = line['NOMBRE ']
    cur.execute('SELECT count FROM counts WHERE ruc = ? ', (ruc,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO counts (ruc, name, count)
                VALUES(?, ?, 1)''', (ruc, name,))
    else:
        cur.execute('UPDATE counts SET count = count + 1 WHERE ruc = ? ', (ruc,))
    conn.commit()
sqlstr = 'SELECT ruc, name, count FROM counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), str(row[1]), row[2])
print(len(list1))
cur.close()