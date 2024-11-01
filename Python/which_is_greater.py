nums = input()

i = nums.find(' ')

num1 = int(nums[:i])
num2 = int(nums[i:])

if num1 > num2:
    print("1")
else:
    print("0")