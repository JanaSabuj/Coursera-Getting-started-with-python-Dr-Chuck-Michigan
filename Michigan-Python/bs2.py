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
tags = soup('a')
t = 7

ans = list()
for i in range(t):
    url1 = tags[17].attrs['href']
    # print(tags[2].contents)
    ans.append(tags[17].contents[0])
    fhandle1 = urllib.request.urlopen(url1, context = gcontext).read()
    soup1 = BeautifulSoup(fhandle1,"html.parser")
    tags = soup1('a')

print(ans[-1])
# for tag in tags:
#     url1 = tag.attrs['href']
#     print(tag.attrs['href'])
