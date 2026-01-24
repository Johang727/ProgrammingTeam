pv = list(str.split(input()))

length = int(pv[0])
width = int(pv[1])
mines = int(pv[2])

board = [['.' for j in range(width)]for i in range(length)]


for i in range(mines):
    IN = list(str.split(input()))
    In1 = int(IN[0]) -1
    In2 = int(IN[1]) -1
    board[In1][In2] = '*'


for i in range(length):
    temp = ''
    for j in range(width):
        temp += board[i][j]
    print(temp)

