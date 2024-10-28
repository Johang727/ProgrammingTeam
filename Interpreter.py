import sys

ram = [0] * 1000
registers = [0] * 10

for i, val in enumerate([int(x) for x in sys.stdin.readlines()]):
    ram[i] = val

pc = 0
num_exec = 0
is_running = True

while is_running:
    num_exec += 1
    instruction = '{:03d}'.format(ram[pc])
    opcode = instruction[0]
    d = int(instruction[1])
    n = int(instruction[2])
    if opcode == '1':
        is_running = False
    elif opcode == '2':
        registers[d] = n
        pc += 1
    elif opcode == '3':
        registers[d] = (registers[d] + n) % 1000
        pc += 1
    elif opcode == '4':
        registers[d] = (registers[d] * n) % 1000
        pc += 1
    elif opcode == '5':
        registers[d] = registers[n]
        pc += 1
    elif opcode == '6':
        registers[d] = (registers[d] + registers[n]) % 1000
        pc += 1
    elif opcode == '7':
        registers[d] = (registers[d] * registers[n]) % 1000
        pc += 1
    elif opcode == '8':
        registers[d] = ram[registers[n]]
        pc += 1
    elif opcode == '9':
        ram[registers[n]] = registers[d]
        pc += 1
    elif opcode == '0':
        if registers[n] != 0:
            pc = registers[d]
        else:
            pc += 1
    else:
        print('KERNEL PANIC! ABORT!')
        exit()

print(num_exec)