import os, sys, json, re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    file_open = os.path.join(BASE_DIR, 'set/results/lines.json')
    # file_open = os.path.join(BASE_DIR, 'set/results/test0.json')
    handle = open(file_open)
    count = 0
    for line in handle:
        count += 1
        xline = line.rstrip()
        # link = r'(\'[A-Z]*\'),\s\'[A-Z]*\',\s\'[0-9]*\',\s\'[A-Z]*[\s,]?[A-Z]*[\s,][A-Z]*[\s,][A-Z]*[\'\s,][A-Z]*[,\s][A-Z]*[\s\',.]*[A-Z]*[\s,\']*'
        # link = r'((\'[A-Z]*\',\s\'[A-Z]*\',\s\'[0-9]*\',\s\'[A-Z]*[\s,]?[A-Z]*[\s,][A-Z]*[\s,][A-Z]*[\'\s,][A-Z]*[,\s][A-Z]*[\s\',.]*[A-Z]*[\s,\']*[A-Z]*[\'\s,]*[A-Z]*[\'\s,]*[0-9]{4}-[0-9]{2}-[0-9]{2}\',\s\'[A-Z]*\'))'
        link = r'((\'[A-Z]*\',\s\'[A-Z]*\',\s\'[0-9]*\',\s\'[A-Z]*[\s,]?[A-Z]*[\s,][A-Z]*[\s,][A-Z]*[\'\s,][A-Z]*[,\s][A-Z]*[\s\',.]*[A-Z]*[\s,\']*[A-Z]*[\'\s,]*[A-Z]*[\'\s,]*[0-9]{4}-[0-9]{2}-[0-9]{2}\',\s\'[A-Z]*\'))'
        stuff = re.findall(link, xline)
        for x in stuff:
            print(x)
