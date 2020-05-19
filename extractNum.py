text = "X-DSPAM-Confidence:    0.8475";
zero = text.find('0')
num = text[zero:zero+6]
print(float(num))
