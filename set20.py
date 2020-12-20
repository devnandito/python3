# coding=utf-8

import pandas as pd, sqlite3, os, sys, csv, json
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
        ifile = input('Enter file name json:')
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

        df0 = pd.read_excel(fopen, header=None)
        list1 = df0.to_dict(orient='records')
        cols = df0.columns.ravel()
        l1 = 0
        list2 = []
        counts = dict()
        activities = dict()
        sources = dict()
        if last == '-1':
            lst = list1[:-1]
        else:
            lst = list1
        for line in lst:
            l1 += 1
            ruc = str(line[cols[1]])
            if ruc == '': continue
            tmp = ruc.split('-')
            ci = tmp[0]
            name = str(line[cols[0]])
            activity = str(line[cols[2]])
            status = str(line[cols[3]])
            salary = str(line[cols[4]])
            if ci not in counts:
                counts[ci] = 1
                activities[activity] = activity
                sources[fopen] = fopen
                list2.append({
                    'ci': ci,
                    'ruc': ruc,
                    'name': name,
                    'activity': activities[activity],
                    'status': status,
                    'salary': salary,
                    'source': sources[fopen],
                    'count': counts[ci]
                })
                print('New: {}, Line: {}'.format(ci,l1))
            else:
                counts[ci] = counts[ci] + 1
                activities[activity] = activities[activity] + '/' + activity + '-' + str(counts[ci])
                sources[fopen] = sources[fopen] + '/' + fopen
                for i in range(len(list2)):
                    if list2[i]['ci'] == ci:
                        list2[i]['activity'] = activities[activity]
                        list2[i]['source'] = sources[fopen]
                        list2[i]['count'] = counts[ci]
                    else:
                        continue
                print('Duplicated: {}, Line: {}'.format(ci,l1))

        print('Total records: {}'.format(l1))
        ofile = os.path.join(BASE_DIR, 'set/results/'+ifile)
        with open(ofile, 'w+') as outfile:
            json.dump(list2, outfile)

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
        f.close()