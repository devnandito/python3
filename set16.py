# coding=utf-8

import pandas as pd, sqlite3, os, sys, json
from datetime import datetime, timedelta

if __name__ == '__main__':

    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours=ihour, minutes=iminute, seconds=isecond)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    while True:
        fopen = input('Enter options [start/quit]:')
        if fopen == 'quit': 
            break
        elif fopen == 'start':
            ifile = input('Enter file name json:')
            sqlfile = input('Enter query file sql:')
            filename0 = os.path.join(BASE_DIR, 'set/vlog.txt')
            f = open(filename0, "r")
            f1 = f.readlines()
            list1 = []
            for x in f1:
                list1.append(x)
            count = int(list1[0])
            fname = list1[1]
            f.close()

            filesql = os.path.join(BASE_DIR, 'set/'+sqlfile)
            fsql = open(filesql, "r")
            query1 = ''
            for x in fsql:
                query1 = query1 + x

            conn = sqlite3.connect('/mnt/c/sqlite/db/pyt2.db')

            cur = conn.cursor()

            # list1 = pd.read_excel(fopen, usecols=cols).to_dict(orient='records')
            df = pd.read_sql_query(query1, conn).to_dict(orient='records')
            documents = dict()
            salaries = dict()
            list2 = []
            line_count = 0
            for row in df:
                line_count += 1
                ci = row['CEDULA']
                salary = row['SALARIO']
                name = row['NOMBRES']
                lastname = row['APELLIDOS']
                if ci not in documents:
                    documents[ci] = 1
                    salaries[ci] = int(salary)
                    list2.append({
                        'CEDULA': ci,
                        'NOMBRES': name,
                        'APELLIDOS': lastname,
                        'SUMA-SALARIO': salaries[ci],
                        'count-cedula': documents[ci]
                    })
                    print('New: {}, Line: {}'.format(ci,line_count))
                else:
                    documents[ci] = documents[ci] + 1
                    salaries[ci] =  salaries[ci] + int(salary)
                    list2.append({
                        'CEDULA': ci,
                        'NOMBRES': name,
                        'APELLIDOS': lastname,
                        'SUMA-SALARIO': salaries[ci],
                        'count-cedula': documents[ci]
                    })
                    print('Duplicated: {}, Line: {}'.format(ci,line_count))
            ofile = os.path.join(BASE_DIR, 'set/results/'+ifile)
            with open(ofile, 'w+') as outfile:
                json.dump(list2, outfile)

            print(list2)
            print(len(list2))                
            conn.close()

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
            f.write(str(list1[1]))
            f.close()

            ext1 = '.txt'
            logFile = '%s%s%s'%(list1[1].rstrip('\n'),list1[0].rstrip('\n'),ext1)
            filename1 = os.path.join(BASE_DIR, 'set/logs/'+logFile)
            f = open(filename1, 'w')
            f.write(str(message))
            f.close