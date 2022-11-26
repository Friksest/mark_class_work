# allow user -> enter pin -> True

from os import system

correct_PIN = 1234
wrong       = True
attempts    = 0

# HW1: stop loop after 3 WRONG attempts
#system("clear")

while attempts != 3:
    user_PIN = int(input("Enter pin: "))
    attempts += 1
    if user_PIN == correct_PIN:
        print("Great, you have entered valid PIN!!!")
        break
    elif attempts == 3:
        print("You have lost 3 attempts. \nTry after 1 hour")
        break
    elif user_PIN != correct_PIN and attempts != 3:
        print("Wrong. You have last", 3 - attempts, "attempt(s)")
    
    
    



