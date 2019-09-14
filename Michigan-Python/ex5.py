fname = input('Enter the file name')
fhandle = open(fname)

cnt = 0
for line in fhandle:
    if not line.startswith('From '): continue
    line = line.rstrip()
    words = line.split()
    email = words[1]
    print(email)
    cnt = cnt + 1

print('There were {} lines in the file with From as the first word'.format(cnt)) 
