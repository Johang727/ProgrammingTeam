n = int(input())
a = 0

for i in range(n):
    qn = input()
    i = qn.find(' ')

    q = float(qn[:i])
    n = float(qn[i:])

    qol = q*n
    a += qol

print(a)

