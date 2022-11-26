# 1d game
# ~~~~x~~~~W~~~~
from os import system

w = 8
x = 2


while True:
    system("clear")
    # ############# DRAW MAP #################
    print()

    n = 1
    while n < 10:
        if   n == w:
            print("W", end=" ")
        elif n == x:
            print("x", end=" ")
        else:
            print("~", end=" ")

        n += 1

    print()
    # ############# DRAW MAP #################

    # ###################### INTERACTION ###################
    direction = input("enter direction (a/d): ")
    # HW1: add limits conditions 
    # HW2* add condition - mine, "BOOOOOMM!!!" stop main loop

    if direction == "a":
        w -= 1
    if direction == "d":
        w += 1
    # ###################### INTERACTION ###################

    # ###################### MOVEMENT LIMITS ###############
    if w < 1:
        w = 1
    if w > 9:
        w = 9
    # ###################### MOVEMENT LIMITS ###############

    # ###################### BOOOM CONDITION ###############
    if w == x:
        print("❌❌❌BOOOMMM !!!!❌❌❌")
        break
    # ###################### BOOOM CONDITION ###############