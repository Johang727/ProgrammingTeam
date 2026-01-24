inp:list[int] = [int(x) for x in input().split()]


n = inp[0]; h = inp[1]; v = inp[2]


bigWidth = max((n-h), h)

bigHeight = max((n-v), v)

print(bigWidth * bigHeight * 4)
