import sys

inp:list[str] = sys.stdin.readlines()



len1:int = int(inp[0].split()[0])
len2:int = int(inp[1+len1].split()[0])+len1

#print(len1); print(len2)

case1 = [x.removesuffix("\n") for x in inp[1:len1+1]]


case2 = [x.removesuffix("\n") for x in inp[len2-1:]]


[print(x) for x in case1]; print("\n"); [print(x) for x in case2]

