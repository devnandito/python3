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
        fopen = input('Enter options [start/quit]:')
        if fopen == 'quit': 
            break
        elif fopen == 'start':
            xlsxname = input('Enter file name to excel:')
            jsonfile = input('Enter json file:')
            filename0 = os.path.join(BASE_DIR, 'set/vlog.txt')
            f = open(filename0, "r")
            f1 = f.readlines()
            list1 = []
            for x in f1:
                list1.append(x)
            count = int(list1[0])
            fname = list1[1]
            f.close()

            df = pd.read_json(jsonfile)

            xfile = os.path.join(BASE_DIR, 'set/results/')
            xlsx = '.xlsx'
            xname = xfile+xlsxname+xlsx
            writer = pd.ExcelWriter(xname, engine='xlsxwriter')

            df.to_excel(writer, sheet_name='Sheet1', startrow=2, index=False, header=False)
            # df.to_excel(writer, sheet_name='Sheet1', startrow=2, index=False, header=False, columns=['CEDULA', 'NOMBRES', 'APELLIDOS'])
            workbook  = writer.book
            worksheet = writer.sheets['Sheet1']

            cell_format = workbook.add_format()
            worksheet.set_column('A:E', 50, cell_format)

            cell_format_title1 = workbook.add_format({
                'bold': True,
                'border': 1,
                'align': 'center',
                'fg_color': 'green',
                'size': 14
            })

            cell_format_title2 = workbook.add_format({
                'bold': True,
                'border': 1,
                'align': 'center',
                'fg_color': 'yellow',
                'size': 14
            })
            worksheet.merge_range('A1:E1', 'FUNCIONARIOS PUBLICOS MES DE JULIO', cell_format_title1)

            header_format = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'valign': 'top',
                'fg_color': '#D7E4BC',
                'border': 1,
                'size': 16
            })

            for col_num, value in enumerate(df.columns.values):
                worksheet.write(1, col_num, value, header_format)

            writer.save()

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