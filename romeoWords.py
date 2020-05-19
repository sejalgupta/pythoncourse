fname = input("Enter file name: ")
fh = open(fname)
list = list()
for line in fh:
    current = line.split()
    for word in current:
        if word not in list:
           list.append(word)
list.sort()
print(list)
