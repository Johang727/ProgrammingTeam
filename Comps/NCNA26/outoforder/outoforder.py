import sys

n = int(input())
num_list = [int(x) for x in sys.stdin.readlines()]

def order(num_list):
    sorted_num = sorted(num_list)
    reverse_num = sorted(num_list, reverse=True)
    sorted_pairs = []
    reverse_pairs = []

    for i in range(n-1):
        sorted_pairs.append((sorted_num[i], sorted_num[i+1]))
        reverse_pairs.append((reverse_num[i], reverse_num[i+1]))   

    for i in range(n-1):
        pair = (num_list[i], num_list[i+1])
        if pair in sorted_pairs:
            return print("In at least partial order")
        elif pair in reverse_pairs:
            return print("In at least partial order")
    return print("Totally out of order")

order(num_list)