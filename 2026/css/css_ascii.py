"""
2 - number cases
1 - scale of case 1
3 - scale of case 2
"""
import sys

inp:list[str] = sys.stdin.readlines()


for i in range(int(inp[0])):
    print(f"Case {i+1}:")
    scale:int = int(inp[i+1])
    top_bottom:str = f"{'C'*5*scale}{' '*5*scale}{'S'*5*scale}{' '*5*scale}{'S'*5*scale}\n"
    p2:str = f"{'C'*scale}{' '*9*scale}{'S'*scale}{' '*9*scale}{'S'*scale}{' '*4*scale}\n"
    mid:str = f"{'C'*scale}{' '*9*scale}{'S'*5*scale}{' '*5*scale}{'S'*5*scale}\n"
    p4:str = f"{'C'*scale}{' '*13*scale}{'S'*scale}{' '*9*scale}{'S'*scale}\n"
    print(f"""{top_bottom*scale}{p2*scale}{mid*scale}{p4*scale}{top_bottom*scale}""")
    print(f"{'\n'*4}")