import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter url:")
html_doc = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html_doc, 'html.parser')
tags = soup('span')
counts = 0
sums = 0
for tag in tags:
    counts = counts + 1
    sums = sums + int(tag.contents[0])
    #print(tag.contents[0])
print('Counts:', counts, 'Sum:', sums)