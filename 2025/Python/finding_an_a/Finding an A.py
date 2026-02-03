'''
input a string length 1 - 1000
lowercase, no spaces, has to contain a

delete everything before the first a
'''

s = input()

# Find the a in the string
i = s.find('a')

# Print everything after the a, including the a
print(s[i:])