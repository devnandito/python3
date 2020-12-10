import re
read = input("Enter the file name:")
handle = open(read)
sumTotal = 0
for line in handle:
    xline = line.rstrip()
    stuff = re.findall('[0-9]+', xline)
    if len(stuff) < 1: continue
    for num in stuff:
        sumTotal = sumTotal + int(num)
print(sumTotal)