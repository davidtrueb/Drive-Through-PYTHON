# Trying to mimic the McDonalds Drive Through


# Modules for project
import math


# SUBTOTAL BEGINNING = 0
subtotal = 0


special_menu = {
    
        "SPECIAL BURGER WITH FRIES": 15.99,
        "SPECIAL ICE CREAM WITH LARG COLA": 7.99,
        "SURPRISE MENU": 18.99
        }


regular_menu = {
        
        "LARG FRIES": 3.99,
        "LARG CHEESE BURGER": 5.99,
        "LARG DOPPLE WOPPER ROYAL": 11.99,

        }



# IF ELSE STATEMENTS - AND PRICETAG OF EACH SPECIAL-MENU
def special_menu():

    # Start - DIFF. PRINT STATEMENTS
    print("HELLO AND WELCOME TO MCDONALDS DRIVE-THROUGH\n")
    print("------------------------------")
    print("WHAT WOULD YOU LIKE TO ORDER?\n")
    print("NR 01 - SPECIAL BURGER WITH FRIES --- 15.00")
    print("NR 02 - SPECIAL ICE CREAM WITH LARG COLA --- 7.00")
    print("NR 03 - SURPRISE MENU --- 18.00\n")

    print("------------------------------")

    # USER CHOOSES
    user_input = int(input("CHOSE 1 - 3: "))

    if user_input == 1:
        print("NR 01 IS SELECTED")

    elif user_input == 2:
        print("NR 01 IS SELECTED")

    elif user_input == 3:
        print("NR 03 IS SELECTED")

    else:
       print("INVALID INPUT")
            
special_menu()

print("------------------------------")

# NEXT ORDER
def regular_menu():
    
    # REGULAR MENU ITEMS 
    print("NOW TO OUR REGULAR MENU ITEMS...\n")
    print("NR 01 - LARG FRIES --- 4.00")
    print("NR 02 - LARG CHEESE BURGER --- 5.00")
    print("NR 03 - LARG DOPPLE WOPPER ROYAL --- 8.00")
    print("NR 04 - SALAD W/ ONIONS AND CHICKEN --- 11.00")
    print("NR 05 - LAVA CAKE WITH ICE CREAM --- 6.00\n")

    print("------------------------------")

    # USER CHOOSES
    user_input_regular = int(input("CHOSE 1 - 5: "))
    
    if user_input_regular == 1:
        print("NR 01 IS SELECTED")

    elif user_input_regular == 2:
        print("NR 02 IS SELECTED")

    elif user_input_regular == 3:
        print("NR 03 IS SELECTED")

    elif user_input_regular == 4:
        print("NR 04 IS SELECTED")

    elif user_input_regular == 5:
        print("NR 05 IS SELECTED")

regular_menu()

# SUBTOTAL OF SPECIAL ITEMS



































