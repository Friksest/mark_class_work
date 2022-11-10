# 2. order completion? (yes/no - True/False)
#   - select food
#   - confirm order (online)
#   - enter client info
#   - delivery info
#   - payment 
#   - delivery (physical)
#   - client seticfyed

select_food = False

food_1_name                 = 'Pizza'
food_1_price                = 75.00
delivery_cost               = 100.00
client_is_vip               = False
amount_for_free_delivery    = 1000



print("Do you want", food_1_name, "(yes/no)?")
food_1_confirm = input()

if food_1_confirm == 'yes':

    food_1_quantity = int(input(" - how many? "))
    food_1_cost     = food_1_price * food_1_quantity
    print(food_1_name, " x ", food_1_quantity, " = ", food_1_cost)

    select_food = True

    confirm_order = input("confirm (yes/no)")

    if confirm_order == 'yes':
        delivery_wanted_str = input('Do you want delivery (Yes/No)? ')
        if delivery_wanted_str == 'yes':
            confirm_delivery = True
            if food_1_cost >= amount_for_free_delivery or client_is_vip:
                free_delivery = True
                print("You'have got free delivery")
            else:
                print("You've to pay 100.00 for delivery")
                total_charge_with_delivery = food_1_price * food_1_quantity + delivery_cost
                print(food_1_name, " x ", food_1_quantity, " + ", delivery_cost," = ", total_charge_with_delivery)
        # HW2:
        # embed here the delivery logic for pt.1











