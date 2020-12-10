# coding=utf-8

import pandas as pd, sqlite3

if __name__ == '__main__':

    while True:
        conn = sqlite3.connect('setall.sqlite')
        cur = conn.cursor()

        fopen = input('Enter file:')
        if fopen == 'quit': break
        table_name = input('Enter table name:')
        last = input('Include last value:(-1/0):')

        cur.execute('''DROP TABLE IF EXISTS {}'''.format(table_name))
        cur.execute('''
            CREATE TABLE {} (ruc TEXT, document TEXT, fullname TEXT,
            activity TEXT, status TEXT, count INTEGER, source TEXT, salary TEXT)
        '''.format(table_name))

        df0 = pd.read_excel(fopen)
        cols = df0.columns.ravel()
        list1 = pd.read_excel(fopen, usecols=cols).to_dict(orient='records')
        l1 = 0
        if last == '-1':
            lst = list1[:-1]
        else:
            lst = list1
        # for line in list1[:5]:
        for line in lst:
            l1 += 1
            ruc = line[cols[1]]
            tmp = ruc.split('-')
            ci = tmp[0]
            name = line[cols[0]]
            activity = line[cols[2]]
            status = line[cols[3]]
            salary = line[cols[4]]
            cur.execute('SELECT count FROM {} WHERE ruc = ? '.format(table_name), (ruc,))
            row = cur.fetchone()
            if row is None:
                cur.execute('''INSERT INTO {} (ruc, document, fullname, activity, status, count, source, salary)
                        VALUES (?, ?, ?, ?, ?, 1, ?, ?)
                '''.format(table_name), (ruc, ci, name, activity, status, fopen, salary,))
                print('New: {}, Line: {}'.format(ci,l1))
            else:
                cur.execute('''UPDATE {} 
                    SET count = count + 1,
                    activity = activity || '/' ||  ? ,
                    source = source || '/' || ? || '-' || count
                    WHERE ruc = ?
                '''.format(table_name), (activity,fopen,ruc,))
                print('Duplicated: {}, Line: {}'.format(ci,l1))
            conn.commit()
        sqlstr = '''
            SELECT ruc, fullname, count
            FROM {} ORDER BY count DESC LIMIT 10
            '''.format(table_name)
        for row in cur.execute(sqlstr):
            print(str(row[0]), str(row[1]), row[2])
        cur.close()
        print('Total records: {}'.format(l1))
