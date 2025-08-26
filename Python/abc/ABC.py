nums = input().split()
betterlist = []

for i in range(len(nums)):
    nums[i] = int(nums[i])

nums.sort()

letters = input()
output = ""

for letter in letters:
    output += str(nums[ord(letter)-65]) + " "
print(output.strip())


