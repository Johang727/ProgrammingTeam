name = input()
newName = name[0]

for i in range(1, len(name)):
    if name[i] != name[i-1]:
        newName += name[i]
print(newName)