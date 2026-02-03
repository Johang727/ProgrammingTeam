n = int(input())
vol = 7
for i in range(n):
    request = input()
    if request == "Skru op!":
        vol += 1
    else:
        vol -= 1

print(vol)