fname = input('Enter a file name')
fhandle = open('mbox-short.txt')

val = 0.0
cnt = 0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    pos = line.find(':')
    line = line[pos+1:].lstrip()
    val += float(line)
    cnt = cnt + 1

print('Average spam confidence:', val/cnt)
