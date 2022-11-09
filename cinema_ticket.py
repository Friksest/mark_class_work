#IO
#types
#operation

#flow control if/else

#DATA
m_title_1 = "Avatar 2"
m_title_2 = "Teminator 9"
m_title_3 = "Titanic Zombie"

m_1_ticket_cost_a = 100
m_1_ticket_cost_b = 120
m_2_ticket_cost_a = 100
m_2_ticket_cost_b = 120
m_3_ticket_cost_a = 120

###move board
from os import system
system("clear")
print(
f"""
1. {m_title_1}:
    a. 18.00
    b. 20.00

2. {m_title_2}:
    a. 16.00
    b. 23.00

3. {m_title_3}:
    a. 18.00
"""
)


movie_number = input('Choose a movie: ')

if movie_number == '1':
    print(f'You have chosen "{m_title_1}"')
    time = input('Choase time: ')
    cost = 0
    if time == 'a':
        print(f'time: 18:00, ticket cost {m_1_ticket_cost_a}')
        cost = 100
    if time =='b':
        print(f'time: 20.00, ticket cost {m_1_ticket_cost_b}')
        cost = 120
    amount = int(input('How many tickets: '))
    
    total = amount * cost


if movie_number == '2':
    print(f'You have chosen "{m_title_2}"')
    time = input('Choase time: ')
    cost = 0
    if time == 'a':
        print(f'time: 16:00, ticket cost {m_2_ticket_cost_a}')
        cost = 100
    if time =='b':
        print(f'time: 16:00, ticket cost {m_2_ticket_cost_b}')
        cost = 120
    amount = int(input('How many tickets: '))
    
    total = amount * cost

        
if movie_number =='3':
    print(f'You have chosen "{m_title_3}"')
    time = input('Choase time: ')
    cost = 0
    if time == 'a':
        print(f'time: 18:00, ticket cost {m_3_ticket_cost_a}')
        cost = 120
    amount = int(input('How many tickets: '))
    
    total = amount * cost

print(f'{amount} x {cost} = {total}')



# Дописать про VIP места











