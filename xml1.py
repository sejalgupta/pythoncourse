import urllib.request
import xml.etree.ElementTree as ET
import ssl

address = input('Enter location: ')

print('Retrieving', address)
data = urllib.request.urlopen(address).read()

print('Retrieved', len(data), 'characters')
print(data.decode())

tree = ET.fromstring(data)

counts = tree.findall('comments/comment/count')
print('Count: ' + str(len(counts)))

sum = 0

for x in counts:
  sum = int(x.text) + sum

print("Sum: " + str(sum))
