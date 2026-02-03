import sys

ram = [0] * 1000
reg = [0] * 10

#print('before loop')

for i, val in enumerate([int(x) for x in sys.stdin.readlines()]):
    ram[i] = val
    #print(str(i) + ' ' + str(val))

#print('after loop')

pc = 0
num_exec = 0
is_running = True

while is_running:
    num_exec += 1
    inst = '{:03d}'.format(ram[pc])
    i1 = int(inst[0])
    i2 = int(inst[1])
    i3 = int(inst[2])
    if i1 == 1:
        is_running = False
    elif i1 == 2:   
        reg[i2] = i3
    elif i1 == 3:
        reg[i2] = (reg[i2] + i3) % 1000
    elif i1 == 4:
        reg[i2] = (reg[i2] * i3) % 1000
    elif i1 == 5:
        reg[i2] = reg[i3]
    elif i1 == 6:
        reg[i2] = (reg[i2] + reg[i3]) % 1000
    elif i1 == 7:
        reg[i2] = (reg[i2] * reg[i3]) % 1000
    elif i1 == 8:
        reg[i2] = ram[i3]
    elif i1 == 9:
        ram[reg[i3]] = reg[i2]
    elif i1 == 0:
        if reg[i3] != 0:
            pc = reg[i2] -1
    else:
        print('kernel panic')
        exit()
    pc += 1
print(num_exec)
