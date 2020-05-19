fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    length = len("X-DSPAM-Confidence:")
    lineCut = line[length:]
    lineCutStrip = lineCut.strip()
    floatLine = float(lineCutStrip)
    total = total + floatLine
avg = total/count
print("Average spam confidence:", avg)
