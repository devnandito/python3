# coding=utf-8

import pandas as pd, json, csv, os, sys
from datetime import datetime, timedelta

def ext(data):
    ext = data.split('.')
    ext = ext[1]
    return ext

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours=ihour, minutes=iminute, seconds=isecond)

    while True:
        options = input('Enter options [start/quit]:')
        options = options.lower()
        if options == 'quit':
            break
        elif options == 'start':
            file_log = os.path.join(BASE_DIR, 'python/set/viewDataLog.txt')
            f = open(file_log, "r")
            f1 = f.readlines()
            list_log = []
            for x in f1:
                list_log.append(x)
            count = int(list_log[0])
            log_name = list_log[1]
            f.close()

            file_input = input('Enter file:')
            res = ext(file_input)
            
            if res == 'json':
                data_frame = pd.read_json(file_input)
                cols = data_frame.columns.ravel()
                data_list = data_frame.to_dict(orient='records')
                print('Total records:',len(data_list))
                print(cols)
            elif res == 'xlsx':
                # data_frame = pd.read_excel(file_input, header=None)
                data_frame = pd.read_excel(file_input)
                cols = data_frame.columns.ravel()
                data_list = data_frame.to_dict(orient='records')
                print('Total records:',len(data_list))
                print(cols)
            elif res == 'csv':
                data_frame = pd.read_csv(file_input)
                cols = data_frame.columns.ravel()
                data_list = data_frame.to_dict(orient='records')
                print('Total records:',len(data_list))
                print(cols)
            else:
                print('Error archivo incorrecto')

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
                    '''.format(start, timerun, end, file_input.lstrip())
            print(message.strip())
            count += 1
            f = open(file_log, 'w')
            f.write(str(count)+'\n')
            f.write(str(log_name))
            f.close()
        else:
            continue

