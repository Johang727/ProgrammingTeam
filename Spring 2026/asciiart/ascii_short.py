q=input().replace(" ","");c=q[13];x=lambda:f"Problem {c} is about ";f="#"*15;o="   "+"#"*8;r="#"*4;t=" "*7;l="/____\\";e=" /  \\";g="  /\\";s=" |"*4;z=lambda:print("I am not sure how to answer that.")
if len(q)!=20:z()
else:
 if c=="A":print(fr"""{x()}Ascii Art
   _     __   __  _   _
  / \   / /  / /{s}
 / _ \  \ \ | | {s}
/_/ \_\ /_/  \_\ |_| |_|""")
 elif c=="B":print(f"""{x()}Fortnite
{f}
{f}
{r}{t}/###
{r}{o}
{r}{t}{r}
{r}{o}
{r}{o}
{r}{o}
{r}_~<{"#"*8}
{f}""")
 elif c=="C":print(f"""{x()}The Legend of Zelda
   {g}
   {e}
   {l}
{g}  {g}
{e} {e}
{l*2}""")
 else:z()