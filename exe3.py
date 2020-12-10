import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
counts = dict()

tags = soup('a')
for tag in tags:
    if tag not in counts:
        counts[tag.get('href', None)] = 1
    else:
        counts[tag.get('href', None)] = counts[tag.get('href', None)] + 1

print(counts)
