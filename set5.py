# coding=utf-8

import pandas as pd, sqlite3, os, sys
from datetime import datetime, timedelta

if __name__ == '__main__':
    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours=ihour, minutes=iminute, seconds=isecond)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    while True:
        conn = sqlite3.connect('setall.sqlite')
        cur = conn.cursor()

        file_excel = input('Enter file:')
        if file_excel == 'quit': break
        table_name = input('Enter table name:')
        last = input('Include last value:(-2/-1/0):')

        tmp_source = file_excel.split('/')
        source_name = tmp_source[1]

        file_log = os.path.join(BASE_DIR, 'python/set/dblog.txt')
        f = open(file_log, "r")
        f1 = f.readlines()
        list_log = []
        for x in f1:
            list_log.append(x)
        count = int(list_log[0])
        fname = list_log[1]
        f.close()

        cur.execute('''DROP TABLE IF EXISTS {}'''.format(table_name))
        cur.execute('''
            CREATE TABLE {} (ruc TEXT, document TEXT, fullname TEXT,
            activity TEXT, status TEXT, count INTEGER, source TEXT, salary TEXT)
        '''.format(table_name))

        df0 = pd.read_excel(file_excel)
        cols = df0.columns.ravel()
        list1 = df0.to_dict(orient='records')
        l1 = 0
        if last == '-1':
            lst = list1[:-1]
        elif last == '-2':
            lst = list1[:-2]
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
                '''.format(table_name), (ruc, ci, name, activity, status, source_name, salary,))
                print('New: {}, Line: {}'.format(ci,l1))
            else:
                cur.execute('''UPDATE {} 
                    SET count = count + 1,
                    activity = activity || '/' ||  ? ,
                    source = source || '/' || ? || '-' || count
                    WHERE ruc = ?
                '''.format(table_name), (activity,source_name,ruc,))
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

        now = datetime.now()
        ohour = now.hour
        ominute = now.minute
        osecond = now.second
        end = timedelta(hours=ohour, minutes=ominute, seconds=osecond)
        timerun = end - start

        message = '''
                Time start: {} \n
                Runtime: {} \n
                Time finish: {} \n
                File: {}
                '''.format(start, timerun, end, source_name)
        print(message)

        count += 1
        f = open(file_log, 'w')
        f.write(str(count)+'\n')
        f.write(str(list_log[1]))
        f.close()

        ext1 = '.txt'
        logFile = '%s%s%s'%(list_log[1].rstrip('\n'),list_log[0].rstrip('\n'),ext1)
        filelog = os.path.join(BASE_DIR, 'python/set/logs/'+logFile)
        f = open(filelog, 'w')
        f.write(str(message))
        f.close()
