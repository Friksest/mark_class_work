from os import system
from random import randint
##########################################
# GAME MAP - list 10 x 10 
# - WHY ints ?
# LEGEND: 
# 0 - empty
# 1 - ROBOT
rx = randint(0, 9)
ry = randint(0, 9)
# 2 - BOMB
gm = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 2, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
]
##########################################
gm[ry][rx] = 1    # initial robot coord setup 

while True:
    #################### DRAW THE MAP #########
    system("clear")
    print("#"*20)
    for y in range(10):
        for x in range(10):
            if gm[y][x] == 1:
                print( "R", end=" " )
            elif gm[y][x] == 2:
                print( "X", end=" " )
            else: 
                print( ".", end=" " )
        print()
    print("#"*20)
    ##########################################
    option = input(">>> ")
    # HW2:  optimuze movement
    # HW3*: check for bomb / hp 
    if option == 'd':
        gm[ry][rx] = 0 # delete the robot
        rx += 1
        if gm[ry][rx] == 2:
            print("You burned! Game over")
            break
        else:
            gm[ry][rx] = 1
        
    if option == 'a':
        gm[ry][rx] = 0 # delete the robot
        rx -= 1
        if gm[ry][rx] == 2:
            print("You burned! Game over")
            break
        else:
            gm[ry][rx] = 1

    if option == 's':
        gm[ry][rx] = 0 # delete the robot
        ry += 1
        if gm[ry][rx] == 2:
            print("You burned! Game over")
            break
        else:
            gm[ry][rx] = 1

    if option == 'w':
        gm[ry][rx] = 0 # delete the robot
        ry -= 1
        if gm[ry][rx] == 2:
            print("You burned! Game over")
            break
        else:
            gm[ry][rx] = 1

# HW1:  add move left / up 












