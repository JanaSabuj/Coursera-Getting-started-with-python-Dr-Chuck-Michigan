text = "X-DSPAM-Confidence:    0.8475";
pos1 = text.find('0')
str = text[pos1:]
print(float(str))
