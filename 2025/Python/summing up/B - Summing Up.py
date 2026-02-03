ab = [int(x) for x in input().strip().split()]
ab.sort()
acc = 0
case = 1
while ab[0] != 0 or ab[1] !=0:
    #code
    sum = 0
    acc = ab[0]+1
    for x in range(ab[0]+1,ab[1]):
        sum += acc
        acc += 1
    print("Case " + str(case) + ": " + str(sum))
    case += 1
    ab = [int(x) for x in input().strip().split()]
    ab.sort()

