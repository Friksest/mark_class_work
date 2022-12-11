# RESTORAN DATA x MULTIPLE LIST

# lists
# operations
# loops / conditionals
# sync


# ONE single waiter
# 3 tables
from os import system
# system("clear")

food_name  = [   "Pizza"  ,  "Soup"  ,   "Salad" ]
food_price = [   100.00   ,  50.00   ,   25.00   ]


#                 ti
#                 v

status    = [  "free",   "free",    "free"  ]
client    = [      "",       "",       ""   ]
dishes    = [      "",       "",       ""   ]
bill      = [     0.00,    0.00,     0.00   ]
tip       = [     0.00,    0.00,     0.00   ]


client[2] = "John"
status[2] = "not-free"

# HW2. enter data for sit 1,2 from KB
new_client   = input("Hello! Welcome to our restaurant! \nWhat is you name?")
choose_table = int(input("Choose a table number: "))

index = choose_table-1

#for index in range(len(status)):
if status[index] != "free":
        print(f"Table №{choose_table} is bussy")
elif status[index] == "free":
    client[index] = new_client
    status[index] = "not-free"
    prefered_dish = input("What do you prefer to order? \n'Pizza', 'Soup', 'Salad': \n")
    dishes[index] = prefered_dish

## 2. client "John" orders a "Soup" 
    client_name  = new_client
    ordered_dish = prefered_dish
    table_idx = -1
    for ti in range(len(client)):
        if client[ti] == client_name:
            table_idx = ti
            break

    food_idx = -1
    for fi in range(len(food_name)):
        if food_name[fi] == ordered_dish:
            food_idx = fi
            break

#print(client_name, " table -> ", table_idx)
    dishes[table_idx] = ordered_dish
    bill[table_idx]   = food_price[food_idx]
    tip[table_idx]    = bill[table_idx] * 0.1

## PRINT INFO
for ti in range(len(status)):
    print(f"table {ti+1}: {status[ti]}")
    if status[ti] != "free" and dishes[ti] == "":
        print(f"\t {client[ti]}")
        
    elif status[ti] != "free" and dishes[ti] != "":
        print(f"\t {client[ti]}: {dishes[ti]} -> {bill[ti]}")
        print(f"\t % {tip[ti]}")

# HW1: add conditional logic 
#      if client didn't order 

# table 1: not-free
#          Marry
# table 2: not-free
#          Kate
# table 3: not-free
#          John: Pizza -> 100.0
#         % 10.0