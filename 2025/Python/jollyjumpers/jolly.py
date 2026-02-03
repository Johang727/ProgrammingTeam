import sys
import time

all_inp = sys.stdin.readlines()

for i in all_inp:
    i = i.strip('\n')
    list = i.split()
    list.pop(0)
    for j in range(len(list)):
        list[j] = int(list[j])
    poss_diff = [x for x in range(1, len(list))]
    for j in range(1, len(list)):
        diff = abs(list[j-1] - list[j])
        if diff in poss_diff:
            try:
                poss_diff.remove(diff)
            except:
                time.sleep(0) # i need something in the except
    if len(poss_diff) == 0:
        print("Jolly")
    else:
        print("Not jolly")
