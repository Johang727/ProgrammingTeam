import sys

inp:list[int] = [int(x) for x in sys.stdin.readlines()]

if inp[0] > inp[1]:
    print("MAGA!")
elif inp[1] > inp[0]:
    print("FAKE NEWS!")
else:
    print("WORLD WAR 3!")