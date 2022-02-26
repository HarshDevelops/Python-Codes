import random
r1=['⬜️', '⬜️', '⬜️']
r2=['⬜️', '⬜️', '⬜️']
r3=['⬜️', '⬜️', '⬜️']
map=[r1,r2,r3]
print(f"{r1}\n{r2}\n{r3}\n")
position= input(("Where would you like to burry the treasure? "))#32

row=int(position[0])#3
column=int(position[1])#2
map[row-1][column-1]="X"
map=[r1,r2,r3]
print(f"{r1}\n{r2}\n{r3}\n")



#      1     2     3 
# 1 ['⬜️', '⬜️', '⬜️']
# 2 ['⬜️', '⬜️', '⬜️']
# 3 ['⬜️', '⬜️', '⬜️']
