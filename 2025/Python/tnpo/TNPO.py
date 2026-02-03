"""
if n is even, n/2
if n is odd, 3n + 1
repeat until n=1
"""

def prob(i):
    acc = 0
    while(i != 1):
        if (i % 2 == 0):
            i /= 2
        else:
            i = (i*3) + 1
        acc += 1
    acc += 1
    return acc

line = input()
k = line.find(" ")
first = int(line[:k])
last = int(line[k:])
best = 0

if last < first:
    hold = first
    last = first
    first = hold

for i in range(first, last + 1):
    acc = prob(i)
    if acc > best:
        best = acc
print(line + " " + str(best))

