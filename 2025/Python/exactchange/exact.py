
validBills:list[int] = [150, 30, 15, 5, 1]
bR:dict[int,int] = {150:0, 30:0, 15:0, 5:0, 1:0}

changeNeeded:int = int(input())
runningTotal:int = 0

for bill in validBills:
    billAmount:int = (changeNeeded - runningTotal) // bill
    bR[bill] = billAmount
    runningTotal += (bill * billAmount) 

print(bR[1], bR[5], bR[15], bR[30], bR[150])