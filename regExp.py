import re

sum = 0
file = input("Enter file name")
lines = open(file, 'r')
for line in lines:
  list = re.findall('[0-9]+', line)
  for element in list:
    sum = sum + int(element)

print(sum)
