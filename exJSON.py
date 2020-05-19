import json
import urllib.request

address = input('Enter location: ')

print('Retrieving', address)
data = urllib.request.urlopen(address).read()

info = json.loads(data)

print('Count:', len(info))

sum = 0

for item in info['comments']:
    sum = sum + int(item['count'])

print('Sum:', sum)
