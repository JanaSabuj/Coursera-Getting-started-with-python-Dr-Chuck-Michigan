fname = input('Enter a file name ')
fhandle = open(fname)

hash = dict()
for line in fhandle:
    if not line.startswith('From '): continue
    line = line.rstrip()
    pos = line.find(':')
    val = line[pos-2:pos]
    hash[val] = hash.get(val,0) + 1

hash = sorted(hash.items())

for x,y in hash:
    print(x,y)
