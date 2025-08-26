"""
First line of input contains 2 ints; len of message + number

2nd line contains N positive integers, smaller or equal to C; the message itself

Input EX:

N C

X Y Z A B

more frequent appears before less frequent

if numbers are the same frequency, they appear in order of message
"""

# inp = input().split() # i knew this was unnecessary

input()

"""n = int(inp[0]) # length of message
c = int(inp[1]) # max value"""

msg = [int(x) for x in input().split()]

"""print(n)
print(c)"""
print(msg)

"""msg_sort = msg[:] # we keep the original to maintain indexes

msg_sort.sort(reverse=True)

print(msg_sort)"""

"""out_list = []

counted = []"""

counts = {}

firsts = {}


for i, n in enumerate(msg):
    counts[n] = counts.get(n,0) + 1
    if n not in firsts:
        firsts[n] = 1

msg.sort(key=lambda x: (-counts[x], firsts[x]))


print(' '.join([str(x) for x in msg]))


"""for i in range(len(msg)):
    if i != 0:
        if msg[i] not in counted:
            # check count of previous to check where to place
            count1 = msg.count(msg[i])
            count0 = msg.count(msg[i-1]
            if count1 > count0:
                # is greater, put left of i-1
            elif count1 < count0:
                # is less, put right of i-1
            else: # is equal
                # determine based on msg list where put. 

    else:
        for j in range(msg.count(msg[i])):
            out_list.append(msg[i])
            print(out_list)
        counted.append(msg[i])
"""