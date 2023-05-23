# Trying to mimic the McDonalds Drive Through


# Modules for project
import math


# SUBTOTAL BEGINNING = 0
subtotal = 0


special_menu = {
    
        "1": 15.99,
        "2": 7.99,
        "3": 18.99
        }


regular_menu = {
        
        "1": 3.99,
        "2": 5.99,
        "3": 11.99,
        "4": 11.99,
        "5": 6.99
        }


# IF ELSE STATEMENTS - AND PRICETAG OF EACH SPECIAL-MENU
def special_menu_method():

    # Start - DIFF. PRINT STATEMENTS
    print("HELLO AND WELCOME TO MCDONALDS DRIVE-THROUGH\n")
    print("------------------------------")
    print("WHAT WOULD YOU LIKE TO ORDER?\n")
    print("NR 01 - SPECIAL BURGER WITH FRIES --- 15.99")
    print("NR 02 - SPECIAL ICE CREAM WITH LARG COLA --- 7.99")
    print("NR 03 - SURPRISE MENU --- 18.99\n")

    print("------------------------------")

    # USER CHOOSES
    user_input_special = int(input("CHOSE 1 - 3: "))

    if user_input_special == 1:
        print("NR 01 IS SELECTED")

    elif user_input_special == 2:
        print("NR 01 IS SELECTED")

    elif user_input_special == 3:
        print("NR 03 IS SELECTED")

    else:
       print("INVALID INPUT")
            
special_menu_method()

print("------------------------------")

# NEXT ORDER
def regular_menu_method():
    
    # REGULAR MENU ITEMS 
    print("NOW TO OUR REGULAR MENU ITEMS...\n")
    print("NR 01 - LARG FRIES --- 4.99")
    print("NR 02 - LARG CHEESE BURGER --- 5.99")
    print("NR 03 - LARG DOPPLE WOPPER ROYAL --- 8.99")
    print("NR 04 - SALAD W/ ONIONS AND CHICKEN --- 11.99")
    print("NR 05 - LAVA CAKE WITH ICE CREAM --- 6.99\n")

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

regular_menu_method()

# SUBTOTAL
while True:
    special_menu_method = input("Enter the item (or 'done' to finish): ")
    if special_menu_method == "done":
        break

    # Check if the item is in the menu
    if special_menu_method in special_menu:
        # Add the price of the item to the subtotal
        subtotal += special_menu[special_menu_method]
    else:
        print("Invalid item. Please try again.")

# Print the subtotal
print("Subtotal: $", subtotal)
