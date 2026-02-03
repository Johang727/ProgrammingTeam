tajna:str = input();

length:int = len(tajna);
rows:int = 1;

while True:

    if not length % (2**rows):
        # 0, therefore can be divided into another row
        print(2**rows);
        rows += 1;

    else:
        # no more rows
        print(f"{rows} rows");
        break;
    
while True:
    if 2**rows > length:
        print("bad");
        rows -= 1;  
    else:
        print(f"good now, should be {rows} rows!");
        break;

col:int = length//rows;

emptyRow:list[str] = ["null"]*col

emptyList:list[list[str]] = [emptyRow]*rows;

# TODO: Finish Later

for i in range(rows):
    emptyList[i][0]