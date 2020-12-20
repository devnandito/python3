# coding=utf-8

import pandas as pd, sqlite3, os, sys, csv
from datetime import datetime, timedelta

if __name__ == '__main__':
    
    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours=ihour, minutes=iminute, seconds=isecond)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    while True:
        fopen = input('Enter file:')
        if fopen == 'quit': break
        ifile = input('Enter file name csv:')
        last = input('Include last value:(-1/0):')

        filename0 = os.path.join(BASE_DIR, 'set/vclog1.txt')
        f = open(filename0, "r")
        f1 = f.readlines()
        list_log = []
        for x in f1:
            list_log.append(x)
        count = int(list_log[0])
        fname = list_log[1]
        f.close()

        df0 = pd.read_excel(fopen)
        cols = df0.columns.ravel()
        list1 = pd.read_excel(fopen, usecols=cols).to_dict(orient='records')
        l1 = 0
        list2 = []
        counts = dict()
        activities = dict()
        if last == '-1':
            lst = list1[:-1]
        else:
            lst = list1
        for line in lst:
            l1 += 1
            ruc = str(line[cols[1]])
            tmp = ruc.split('-')
            ci = tmp[0]
            name = str(line[cols[0]])
            activity = str(line[cols[2]])
            status = str(line[cols[3]])
            salary = str(line[cols[4]])
            if ci not in counts:
                counts[ci] = 1
                activities[activity] = activity
                list2.append({
                    'ci': ci,
                    'ruc': ruc,
                    'name': name,
                    'activity': activities[activity],
                    'status': status,
                    'salary': salary,
                    'count': counts[ci]
                })
                print('New: {}, Line: {}'.format(ci,l1))
            else:
                counts[ci] = counts[ci] + 1
                activities[activity] = activities[activity] + '/' + activity + '-' + str(counts[ci])
                list2.append({
                    'ci': ci,
                    'ruc': ruc,
                    'name': name,
                    'activity': activities[activity],
                    'status': status,
                    'salary': salary,
                    'count': counts[ci]
                })
                print('Duplicated: {}, Line: {}'.format(ci,l1))

        print('Total records: {}'.format(l1))
        val = ''
        ofile = os.path.join(BASE_DIR, 'set/results/'+ifile)
        with open(ofile, 'w+') as f2:
            writer = csv.writer(f2)
            writer.writerow(('ci:ruc:name:activity:status:salary:count',))
            for item in list2:
                val = '%s:%s:%s:%s:%s:%s:%s'%(item['ci'].strip(), item['ruc'].strip(), item['name'].strip(), item['activity'].strip(),item['status'].strip(), item['salary'].strip(), item['count'])
                writer.writerow((val,))

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
        filelog = os.path.join(BASE_DIR, 'set/logs/'+logFile)
        f = open(filelog, 'w')
        f.write(str(message))
        f.close