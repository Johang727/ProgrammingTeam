import sys

"""IN_1
5 4 4 5
5 4 4 4
5 5 4 4
5 5 5 4
4 4 4 5

Expected: 4 19
"""
# Determine who is the winner and how many points they got



scores: list[int] = [int(x[:-1].replace(" ","")) for x in sys.stdin.readlines()]


#print(scores)


winner: int = 0
winnerScore: int = -1

for team in range(len(scores)):
    total: int = 0
    for score in str(scores[team]):
        total += int(score)
    
    if total > winnerScore:
        winnerScore = total
        winner = team+1

print(f"{winner} {winnerScore}")