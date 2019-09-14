fname = input('Enter a file name')
fhandle = open(fname)

hash = dict()

for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    # print(email)
    hash[email] = hash.get(email,0) + 1


nax = None
key = None
for x,y in hash.items():
    if nax is None or y>nax:
        nax = y
        key = x

print(key,nax)
