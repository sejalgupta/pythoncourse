from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0

fhand = urlopen('http://py4e-data.dr-chuck.net/comments_391039.html', context=ctx).read()
soup = BeautifulSoup(fhand, "html.parser")

tags = soup('span')
for tag in tags:
    t = tag.contents[0]
    sum = sum + int(t)

print(sum)
