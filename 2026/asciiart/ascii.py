"""
Inital planning:

Input:
Friends Question

Strip
Consecutive Spaces = 1 space

----

Gotcha's Found:

- Inital submission didn't account for no spaces, therefore causing a runtime error.
- "Any other questions are too confusing": might need to check if its the *exact* question.
    - Just made sure the question length is 20, since there are 20 chars in What is problem X about?

"""


question:str = input().strip().replace(" ","")

q:str = question[13]

if len(question) != 20:
    print("I am not sure how to answer that.")
else:
    if q == "A":
        print("""Problem A is about Ascii Art
   _     __   __  _   _
  / \\   / /  / / | | | |
 / _ \\  \\ \\ | |  | | | |
/_/ \\_\\ /_/  \\_\\ |_| |_|""")
    elif q == "B":
        print("""Problem B is about Fortnite
###############
###############
####       /###
####   ########
####       ####
####   ########
####   ########
####   ########
####_~<########
###############""")
    elif q == "C":
        print("""Problem C is about The Legend of Zelda
     /\\
    /  \\
   /____\\
  /\\    /\\
 /  \\  /  \\
/____\\/____\\""")
    else:
        print("I am not sure how to answer that.")

