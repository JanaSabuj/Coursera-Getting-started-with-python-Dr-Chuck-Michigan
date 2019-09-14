import urllib.request, urllib.parse, urllib.error
import ssl
import json

gcontext = ssl.SSLContext()
url = input('Enter the url to parse from')
fhandle = urllib.request.urlopen(url, context = gcontext).read().decode()

info = json.loads(fhandle)
# test = json.dumps(fhandle, indent=4)
# print(info['comments'])
sum = 0
for comment in info['comments']:
    sum += comment['count']

print(sum)
