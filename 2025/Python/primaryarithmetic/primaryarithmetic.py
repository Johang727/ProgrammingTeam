import sys

arith:list[str] = [x.strip("\n") for x in sys.stdin.readlines()]

def calculateOperations(num0:str, num1:str) -> int:
    carry:int = 0
    operationsNeeded:int = 0
    for i in range(len(num0)-1, -1, -1):
        result:int = int(num0[i]) + int(num1[i]) + carry
        if result > 9:
            carry = 1
            operationsNeeded += 1
        else:
            carry = 0
    return operationsNeeded

def padNumber(num:str, pad:int) -> str:
    num = "0"*pad + num
    return num




for item in arith:
    if item != "0 0":
        numbers:list[str] = item.split(" ")
        diff:int = len(numbers[0]) - len(numbers[1])
        if diff == 0:
            #if same size
            operationsNeeded = calculateOperations(numbers[0], numbers[1])
        elif diff > 0: # first one is greater length
            numbers[1] = padNumber(numbers[1], diff)
            operationsNeeded = calculateOperations(numbers[0], numbers[1])
        elif diff < 0: # 2nd is greater in length
            numbers[0] = padNumber(numbers[0], -diff)
            operationsNeeded = calculateOperations(numbers[0], numbers[1])
        else:
            print("I broke something :D")
            sys.exit(1)
        
        if operationsNeeded == 0:
            print("No carry operation.")
        elif operationsNeeded == 1:
            print("1 carry operation.")
        else:
            print(f"{operationsNeeded} carry operations.")
        
    else: #end 
        sys.exit(0)

