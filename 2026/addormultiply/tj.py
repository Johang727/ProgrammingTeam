import sys

inp = sys.stdin.readlines()

firstLine = inp.pop(0).split()
numInts = int(firstLine[0])
numOperations = int(firstLine[1])
expression = inp.pop(0).strip()

numbers = []
symbols = []
groups = []

for num in range(len(expression)):
    if(num%2 == 0):
        numbers.append(expression[num])
    else:
        symbols.append(expression[num])

#print(numbers)
#print(symbols)

output = compile(expression, "<string>", "eval")

print(eval(output)%1000000007)
for op in inp:
    operation = op.strip().split()
    if(operation[0] == 's'):
        firstNum = numbers[int(operation[1]) - 1] #sets FirstNum = the first number in the swap
        secondNum = numbers[int(operation[2]) - 1] #sets SecondNum = the second number in the swap
        numbers[int(operation[1]) - 1] = secondNum #Sets the first position = the second num
        numbers[int(operation[2]) - 1] = firstNum #Sets the second position = the first num
    elif(operation[0] == 'f'):
        if(symbols[int(operation[1]) - 1] == '+'): #if symbol to swap is a +, swap to *, otherwise, swap to +
            symbols[int(operation[1]) - 1] = '*'
        else:
            symbols[int(operation[1]) - 1] = '+'
    else:
        for symbol in range(len(symbols)):
            if symbols[symbol] == '+':
                symbols[symbol] = '*'
            else:
                symbols[symbol] = '+'
    

    expression = '' #sets expression back to blank
    for i in range(len(symbols)): #loops through symbols, adding to expression the numbers and the symbols
        expression += numbers[i]
        expression += symbols[i]
    expression += numbers[len(symbols)]
    
    output = compile(expression, "<string>", "eval")

    print(eval(output)%1000000007)