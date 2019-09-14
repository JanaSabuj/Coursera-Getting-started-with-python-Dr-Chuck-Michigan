fname = input('Enter a file name')
fhandle = open(fname)
for line in fhandle:
    print(line.rstrip().upper())
