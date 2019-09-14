import urllib.request, urllib.parse, urllib.error
import ssl
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
address = input('Enter location: ')
print('Retrieving http://..')
serviceurl2 = urllib.parse.urlencode({'address': address})

url = serviceurl + serviceurl2
gcontext = ssl.SSLContext()
fhandle = urllib.request.urlopen(url,context = gcontext).read().decode()
data = json.loads(fhandle)
# print(url)
print('Retrieved {} characters'.format(len(data)))
print('Place id', data['results'][0]['place_id'])
# print(json.dumps(data, indent=4))
