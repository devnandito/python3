import pandas as pd, sqlite3

conn = sqlite3.connect('/mnt/d/pytyvo2/set1.sqlite')
cur = conn.cursor()

while True:
    fopen = input('Enter file:')
    if fopen == 'quit': break
    table_name = input('Enter table name:')

    cur.execute('''DROP TABLE IF EXISTS {}'''.format(table_name))
    cur.execute('''
        CREATE TABLE {} (ruc TEXT, fullname TEXT,
        activity TEXT, status TEXT, count INTEGER)
    '''.format(table_name))

    df0 = pd.read_excel(fopen)
    cols = df0.columns.ravel()
    list1 = pd.read_excel(fopen, usecols=cols).to_dict(orient='records')

    for line in list1:
        ruc = line[cols[1]]
        name = line[cols[0]]
        activity = line[cols[2]]
        cur.execute('SELECT count FROM {} WHERE ruc = ? '.format(table_name), (ruc,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO {} (ruc, fullname, activity, count)
                    VALUES (?, ?, ?, 1)
            '''.format(table_name), (ruc, name, activity,))
        else:
            cur.execute('''UPDATE {} 
                SET count = count + 1,
                avtivity = CONCAT(activity, ' ', ? )
                WHERE ruc = ?
            '''.format(table_name), (activity,ruc,))
        conn.commit()
    # sqlstr = '''
    #     SELECT ruc, fullname, count
    #     FROM {} ORDER BY count DESC LIMIT 10
    #     '''.format(table_name)
    # for row in cur.execute(sqlstr):
    #     print(str(row[0]), str(row[1]), row[2])
    cur.close()
    print('Total records: {}'.format(len(list1)))