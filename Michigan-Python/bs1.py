import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ctx = ssl.create_deafult_context()
# ctx.check_hostname = False
# ctx.verify_mode = SSL.CERT_NONE
gcontext = ssl.SSLContext()
url = input('Enter the url to parse from')
fhandle = urllib.request.urlopen(url, context = gcontext).read()
soup = BeautifulSoup(fhandle,"html.parser")

#parse
tags = soup('span')
sum = 0
for tag in tags:
    # print('TAG:',tag.attrs)
    # print('TAG:',tag.contents)
    list = tag.contents
    for x in list:
        sum += int(x)


print(sum)
