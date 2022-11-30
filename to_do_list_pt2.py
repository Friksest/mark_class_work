# AP / TODO - plan your task 
from os import system
# dynamic _ batteries included

# ##### Data  #####
tasks = [
    "Learn Pyton",                  #0
    "Become a DEV",                 #1
    "Become a MILLIONARE!  :D",     #2
    #"Be mega happy!"               #3
]
# ##### Data  #####

# S##########INTERECTIVE MESSAGE #############
system("clear")
print("Text the number of actions: ", "1. Add task;", "2. Show tasks;", "3. Remove task;", "4. Clear todo;", "0. EXIT", sep="\n")
BUTTON = int(input())

# E##########INTERECTIVE MESSAGE #############

# S########## EXECUTE BUTTON 1 #############
if BUTTON == 1:
    while True:
        new_task = input("Add a new taks: ")
        if new_task == "":   #conditions -> stop input< ""
            break
        elif new_task not in tasks:
            tasks.append( new_task ) 
        
        else:
            print("This tasks already exists")

        # ##### print the tasks  #####
        print("TODO list (", len( tasks ) , "):")
        for i in range( len( tasks )):
            #print(f"New task: {new_task}, was adde in list")
            print("\t", [i], ">", tasks[i])

        # ##### print the tasks  #####
# E########## EXECUTE BUTTON 1 #############    

# S########## EXECUTE BUTTON 2 #############  
if BUTTON == 2:
    print("TODO list (", len( tasks ) , "):")
    for i in range( len( tasks )):
        print("\t", [i], ">", tasks[i])

# E########## EXECUTE BUTTON 2 #############  

# S########## EXECUTE BUTTON 3 #############  
if BUTTON == 3:
    print("what number TODO list remove(", len( tasks ) , "):")
    for i in range( len( tasks )):
        print("\t", [i], ">", tasks[i])
    remove_tsk = int(input())
    tasks.pop(remove_tsk)
    for i in range( len( tasks )):
        print("\t", [i], ">", tasks[i])

# E########## EXECUTE BUTTON 3 #############  

# S########## EXECUTE BUTTON 4 ############# 
if BUTTON == 4:
    tasks.clear()
    print("All tasks cleared")
# E########## EXECUTE BUTTON 4 #############  

# S########## EXECUTE BUTTON 5 ############# 
if BUTTON == 0:
    print("Programm closed")

# E########## EXECUTE BUTTON 5 ############# 


#   make it fully interactive:
#   MENU: 1. add task, 2. show tasks, 3.remove task, 4.clear todo, 0, exit  