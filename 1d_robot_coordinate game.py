from os import system

lenght     = 40
roboX      = 5
bombX      = 8
bombX2     = 20
bombX3     = 38
heartX     = 2
heartX2    = 15
heartX3    = 30
hp         = 100
charge     = 100
steps      = 0

money      = 6
money2      = 11
money3      = 25
money4      = 35
score      = 0
steps      = 0

# HW1:
#   + add "HP" health default : 100% , when bomb - 50%
#   + - game over -> HP == 0 !!!
#   + show HP 
#   + many bombs
#   + herts + 20% hp
#   + limits (a teleport / b ) or stop )
#   + charge = 100% , each step - 5% charge

while True:
    system("clear")
    
    
    # ####################### DRAWNING THE MAP ###############
    x = 1
    print("\n")
    print("You have ", hp, "% HP", " and ", charge, " % charge", sep="")
    while x <= lenght:
        
        if x == roboX:
            print("😶", end = "")
        elif x == bombX:
            print("💣", end = "")
        elif x == bombX2:
            print("💣", end = "")
        elif x == bombX3:
            print("💣", end = "")
        elif x == heartX:
            print("💓", end = "")
        elif x == heartX2:
            print("💓", end = "")
        elif x == heartX3:
            print("💓", end = "")
        elif x == money:
            print("💰", end = "")
        elif x == money2:
            print("💰", end = "")
        elif x == money3:
            print("💰", end = "")
        elif x == money4:
             print("💰", end = "")
        else:
            print("▬", end = "")
        x  += 1
        
    print("\nYou score is:",score)     

    print("\n")
    # #########################################################

    # ####################### CONTROL ###############
    direction = input("dir (a/d/x) > ")
    if direction == 'a':
        roboX   -= 1
        charge  -= 5
    if direction == 'd':
        roboX   += 1
        charge  -= 5
    if direction == 'x':
        system("clear")
        print("Thank you for your playing!!!")
        break
    
    # ##################### DECREASE HP ########################    
    if roboX == bombX or roboX == bombX2 or roboX == bombX3:
        hp -= 50
    
    # ##################### INCREASE HP ########################
    
    elif roboX == heartX or roboX == heartX2 or roboX == heartX3:
        hp += 20
   
    # ##################### COLLECT SCORE ########################
    if roboX in [money, money2, money3, money4]:
        score += 300


    # ############limits (a teleport / b ) or stop )###########
    if roboX < 1:
        roboX = lenght
    elif roboX > lenght:
        roboX = 1
    

    # ########################GAME OVER#########################
    if hp <= 0 or charge <= 0:
        print("❌❌❌GAME OVER :(❌❌❌")
        break