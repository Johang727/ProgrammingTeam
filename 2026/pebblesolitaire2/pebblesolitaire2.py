import sys

inp:list[str] = [x.strip() for x in sys.stdin.readlines()]


# curr_board:next_board
next_step:dict[str, str] = {}


# board:answer
board_answers:dict[str,int] = {}

def solve(game:str) -> int:
    if board_answers.get(game, None):
        return int(board_answers[game])
    elif next_step.get(game, None):
        solve(next_step[game])

    minimum_plays:int = game.count("o")
    board:list[str] = list(game)

    for i in range(len(board) - 2):

        if board[i] == "o" and board[i+1] == "o" and board[i+2] == "-":
            board_copy = board[:]
            board_copy[i:i+3] = ["-", "-", "o"]

            if solve("".join(board_copy)) < minimum_plays:
                minimum_plays = solve("".join(board_copy))
                next_step[game] = "".join(board_copy)
    
        if board[i] == "-" and board[i+1] == "o" and board[i+2] == "o":
            board_copy = board[:]
            board_copy[i:i+3] = ["o", "-", "-"]
            if solve("".join(board_copy)) < minimum_plays:
                minimum_plays = solve("".join(board_copy))
                next_step[game] = "".join(board_copy)
        
    board_answers[game] = minimum_plays
    return minimum_plays

    
inp.pop(0)

for board in inp:
    print(solve(board))
    

