# coding=utf-8

import sqlite3, os, sys, csv
from datetime import datetime, timedelta

if __name__ == '__main__':
    
    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours=ihour, minutes=iminute, seconds=isecond)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    while True:
        conn = sqlite3.connect('testcsv.sqlite')
        cur = conn.cursor()

        fopen = input('Enter file:')
        if fopen == 'quit': break
        table_name = input('Enter table name:')

        filename0 = os.path.join(BASE_DIR, 'set/vclog1.txt')
        f = open(filename0, "r")
        f1 = f.readlines()
        list_log = []
        for x in f1:
            list_log.append(x)
        count = int(list_log[0])
        fname = list_log[1]
        f.close()

        with open(fopen) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=':')
            next(readCSV, None) 
            for row in readCSV:
                cur.execute('''
                    INSERT INTO {} (ci, name, count)
                    VALUES (?, ?, ?)
                    '''.format(table_name), 
                    (row[0], row[1], row[2],))
                conn.commit()
        cur.close()

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
        f.write(str(fname))
        f.close()

        ext1 = '.txt'
        logFile = '%s%s%s'%(list_log[1].rstrip('\n'),list_log[0].rstrip('\n'),ext1)
        filelog = os.path.join(BASE_DIR, 'set/logs/'+logFile)
        f = open(filelog, 'w')
        f.write(str(message))
        f.close