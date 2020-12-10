import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Input url:')
count = int(input('Input count:'))
pos = int(input('Input position:'))

while count > 0:
    count = count - 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    uri = tags[pos-1].get('href', None)
    print(tags[pos-1].get('href', None))
    url = uri

# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# tags = soup('a')
# print(tags[pos-1].get('href', None))
