# coding=utf-8

import pandas as pd, sqlite3
from datetime import datetime, timedelta

if __name__ == '__main__':

    now = datetime.now()
    ihour = now.hour
    iminute = now.minute
    isecond = now.second
    start = timedelta(hours=ihour, minutes=iminute, seconds=isecond)

    while True:

        fopen = input('Enter file:')
        if fopen == 'quit': break

        elif fopen == 'start':
            conn = sqlite3.connect('tracks/trackdb.sqlite')

            cur = conn.cursor()
            df = pd.read_sql_query('''
                SELECT
                id AS PK,
                artist_id AS FK,
                title as TITLE
                FROM Album ORDER BY id
            ''', conn)

            writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

            df.to_excel(writer, sheet_name='Sheet1', startrow=2, index=False, header=False)
            # df.to_excel(writer, sheet_name='Sheet1', startrow=1, index=False, header=False, columns=['PK', 'FK', 'TITLE'], startcol=0)
            workbook  = writer.book
            worksheet = writer.sheets['Sheet1']

            cell_format = workbook.add_format()
            worksheet.set_column('A:B', 20, cell_format)
            worksheet.set_column('C:C', 100, cell_format)
            # cell_format.set_border()

            cell_format_title1 = workbook.add_format({
                'bold': True,
                'border': 1,
                'align': 'center',
                'fg_color': 'green',
                'size': 16
            })

            cell_format_title2 = workbook.add_format({
                'bold': True,
                'border': 1,
                'align': 'center',
                'fg_color': 'yellow',
                'size': 16
            })
            worksheet.merge_range('A1:B1', 'PRIMER PAGO PYTYVO 2.0', cell_format_title1)
            worksheet.merge_range('C1:D1', 'FUNCIONARIO PUBLICOS', cell_format_title2)

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
                # worksheet.write(0, col_num + 1, value, header_format)

            writer.save()

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