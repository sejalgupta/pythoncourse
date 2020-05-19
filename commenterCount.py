name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
names = dict()
biggestName = None
biggestCount = 0
for line in handle:
    if line.startswith('From '):
        word = line.split()
        names[word[1]] = names.get(word[1], 0) + 1
for n, count in names.items():
    if biggestCount < count:
        biggestCount = count
        biggestName = n
print(biggestName, biggestCount)
