fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    lineR = line.rstrip()
    print(lineR.upper())
