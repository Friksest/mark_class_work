# move a car on road
#
# w - forward
# s - backward
# ---------
# |   :   |
# |   :   |
# |   :   |
# |   :   |
# |   :   |
# |   :   |
# |   :   | 4
# |   :   | 3
# |   :   | 2
# |   : # | 1
# ---------
#   1   2   ---- Lane



from os import system

roadLen = 10
carY    = 1
lane    = 2

while True:
    ##### DRAWING THE MAP ##########
    system("clear")
    print("---------")
    for y in range(roadLen, 0, -1):
        carL = " "
        carR = " "
        
        if y == carY:
            if lane == 1:
                carL = "#"
            if lane == 2:
                carR = "#"
        print(f"| {carL} : {carR} |")
    print("---------")
    ##### DRAWING THE MAP ##########

    ##### USER INTERECTION ##########
    
    move = input("move (w/s)> ")
    if move == "w":
        carY += 1       
        if carY > roadLen:
            if lane == 2:
                lane = 1
            elif lane == 1:
                lane = 2
            carY -= 1
    if move == "s":
        carY -= 1
        if carY < 1:
            if lane == 2:
                lane = 1
            elif lane == 1:
                lane = 2
            carY += 1

    ##### USER INTERECTION ##########