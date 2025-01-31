nums = input().split()
betterlist = []

for num in nums:
    betterlist.append(int(num))

betterlist.sort()

letters = input()
output = ""

for letter in letters:
    output += str(betterlist[ord(letter)-65]) + " "
print(output.strip())


