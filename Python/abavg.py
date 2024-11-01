cases = int(input())

for i in range(cases):
    acc = 0
    avgs = input().split()
    for i in avgs[1:]:
        acc += int(i)
    avg = acc / (len(avgs) - 1)
    occ = 0
    for i in avgs[1:]:
        if int(i) > avg:
            occ += 1
        aa = (occ/(len(avgs)-1)*100)
    aa = '{0:.3f}'.format(aa)
    print(str(aa) + "%")
