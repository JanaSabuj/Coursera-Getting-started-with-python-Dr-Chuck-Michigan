import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET


gcontext = ssl.SSLContext()
url = input('Enter the url to parse from')
fhandle = urllib.request.urlopen(url, context = gcontext).read()

tree = ET.fromstring(fhandle)
lst = tree.findall('comments/comment')

sum = 0
for item in lst:
    # print(item.find('Name').text)
    # print(item.find('count').text)
    # print(item.find('count').text)
    sum += int(item.find('count').text)

print(sum)
