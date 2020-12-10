import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location:')
data = urllib.request.urlopen(url).read()
info = json.loads(data)
print('Count:', len(info['comments']))

add = 0

for item in info['comments']:
    add = add + int(item['count'])
    # print(item['name'])

print ('Sum: ', add)