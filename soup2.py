from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0

url = input("Enter URL: ")
count = input("Enter count: ")
position = input("Enter position: ")

number = 1
name = ''

while (number <= int(count)):
    fhand = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(fhand, "html.parser")
    tags = soup('a')
    tagCount = 1
    for tag in tags:
        if (tagCount == int(position)):
            url = tags[tagCount - 1].get('href', None)
            print(url)
            if (number == int(count)):
                name = name + str(tags[tagCount - 1].contents[0])
        tagCount = tagCount + 1
    number = number + 1

print(name)
