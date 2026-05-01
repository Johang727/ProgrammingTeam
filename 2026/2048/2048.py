"""
2 0 0 2
4 16 8 2
2 64 32 4
1024 1024 64 0
0
"""

import sys

inp:list[str] = sys.stdin.read().split()

it = iter(inp)

board:list[list[int]] = []
board_check:list[list[int]] = []

n = lambda: int(next(it))

def print_board():
    global board
    print(f"""{board[0][0]} {board[0][1]} {board[0][2]} {board[0][3]}
{board[1][0]} {board[1][1]} {board[1][2]} {board[1][3]}
{board[2][0]} {board[2][1]} {board[2][2]} {board[2][3]}
{board[3][0]} {board[3][1]} {board[3][2]} {board[3][3]}
---""")

for _ in range(4):
    board.append([n(), n(), n(), n()])
    board_check.append([0]*4)


next_move:int = n()

match next_move:
    case 0:
        # left
        for row in range(4):
            for val in range(1,4):
                temp = val
                while(temp > 0):
                    if(board[row][temp-1] == 0):
                        board[row][temp-1] = board[row][temp]
                        board[row][temp] = 0
                    elif(board[row][temp-1] == board[row][temp] and board_check[row][temp-1] == 0 and board_check[row][temp] == 0):
                        board[row][temp-1] = board[row][temp-1]*2
                        board[row][temp] = 0
                        board_check[row][temp-1] = 1
                    else:
                        break
                    temp -= 1
    case 1:
        # up
        for col in range(4):
            for row in range(1, 4):
                temp = row
                while(temp > 0):
                    if(board[temp-1][col] == 0):
                        board[temp-1][col] = board[temp][col]
                        board[temp][col] = 0
                    elif(board[temp-1][col] == board[temp][col] and board_check[temp-1][col] == 0 and board_check[temp][col] == 0):
                        board[temp-1][col] = board[temp-1][col]*2
                        board[temp][col] = 0
                        board_check[temp-1][col] = 1
                    else:
                        break
                    temp -= 1
    case 2:
        # right
        for row in board:
            row.reverse()
        for row in range(4):
            for val in range(1,4):
                temp = val
                while(temp > 0):
                    if(board[row][temp-1] == 0):
                        board[row][temp-1] = board[row][temp]
                        board[row][temp] = 0
                    elif(board[row][temp-1] == board[row][temp] and board_check[row][temp-1] == 0 and board_check[row][temp] == 0):
                        board[row][temp-1] = board[row][temp-1]*2
                        board[row][temp] = 0
                        board_check[row][temp-1] = 1
                    else:
                        break
                    temp -= 1
        for row in board:
            row.reverse()

    case 3:
        # down
        board.reverse()
        for row in board:
            row.reverse()
        for col in range(4):
            for row in range(1, 4):
                temp = row
                while(temp > 0):
                    if(board[temp-1][col] == 0):
                        board[temp-1][col] = board[temp][col]
                        board[temp][col] = 0
                    elif(board[temp-1][col] == board[temp][col] and board_check[temp-1][col] == 0 and board_check[temp][col] == 0):
                        board[temp-1][col] = board[temp-1][col]*2
                        board[temp][col] = 0
                        board_check[temp-1][col] = 1
                    else:
                        break
                    temp -= 1
        for row in board:
            row.reverse()
        board.reverse()


print(f"""{board[0][0]} {board[0][1]} {board[0][2]} {board[0][3]}
{board[1][0]} {board[1][1]} {board[1][2]} {board[1][3]}
{board[2][0]} {board[2][1]} {board[2][2]} {board[2][3]}
{board[3][0]} {board[3][1]} {board[3][2]} {board[3][3]}""")

