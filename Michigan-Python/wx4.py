fname = input('Enter a file name')
fhandle = open(fname)

ans = list()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in ans: continue
        ans.append(word)

ans.sort()
print(ans)
