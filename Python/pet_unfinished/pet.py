# Get all inputs

def i():
    return input()

x1 = i()
#x2 = i()
#x3 = i()
#x4 = i()
#x5 = i()


def split(x):
    return list(str.split(x))

x1 = split(x1)
#x2 = split(x2)
#x3 = split(x3)
#x4 = split(x4)
#x5 = split(x5)

print(x1[1])

def a(x):
    a = 0
    for i in range(5):
        a += x[i]
    return a

x1 = a(x1)
print (x1)