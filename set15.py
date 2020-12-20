# coding=utf-8

import sqlite3, os, sys, json
from datetime import datetime, timedelta

if __name__ == '__main__':

    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours=ihour, minutes=iminute, seconds=isecond)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    while True:
        conn = sqlite3.connect('setjson.sqlite')
        cur = conn.cursor()

        fopen = input('Enter file:')
        if fopen == 'quit': break
        table_name = input('Enter table name:')

        filename0 = os.path.join(BASE_DIR, 'set/jsonlog.txt')
        f = open(filename0, "r")
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

        with open(fopen) as json_file:
            data = json.load(json_file)
            for row in data:
                cur.execute('''INSERT INTO {} (ruc, document, fullname, activity, status, count, salary)
                        VALUES (?, ?, ?, ?, ?, 1, ?)
                '''.format(table_name), (row['ruc'], row['ci'], row['name'], row['activity'], row['status'], row['salary'],))
                conn.commit()
        now = datetime.now()
        ohour = now.hour
        ominute = now.minute
        osecond = now.second
        end = timedelta(hours=ohour, minutes=ominute, seconds=osecond)
        timerun = end - start
        message = '''
                Time start: {} \n
                Runtime: {} \n
                Time finish: {}
                '''.format(start, timerun, end)
        print(message)
        count += 1
        f = open(filename0, 'w')
        f.write(str(count)+'\n')
        f.write(str(list_log[1]))
        f.close()

        ext1 = '.txt'
        logFile = '%s%s%s'%(list_log[1].rstrip('\n'),list_log[0].rstrip('\n'),ext1)
        filename1 = os.path.join(BASE_DIR, 'set/logs/'+logFile)
        f = open(filename1, 'w')
        f.write(str(message))
        f.close