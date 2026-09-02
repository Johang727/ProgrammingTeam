import sys

inp:list[str] = sys.stdin.read().split()
it = iter(inp)

ints:int = int(next(it))
int_list:list[int] = []

for _ in range(ints):
    int_list.append( int(next(it)) )

for _ in range(ints):
    print( int_list.pop(len(int_list)-1) )