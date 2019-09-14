import re
fhandle = open('regex_sum_277976.txt')

sum = 0
for line in fhandle:
    temp = re.findall('[0-9]+',line)
    for num in temp:
        sum += int(num)

print(sum)
