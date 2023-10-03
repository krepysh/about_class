# MENU = {
#     'espresso': {
#         'ingredients': {
#             'coffee': 19,
#             'water': 35,
#         },
#         'price': 1.99,
#     },
#     'latte': {
#         'ingredients': {
#             'coffee': 24,
#             'water': 50,
#             'milk': 150,
#         },
#         'price': 2.39,
#     },
#     'flat white': {
#         'ingredients':{
#             'coffee': 24,
#             'water': 60,
#             'milk': 50,
#         },
#         'price': 3.19,
#     }
# }

# INVENTORY = {
#     'coffee': 100,
#     'water': 300,
#     'milk': 300,
#     'money': 0,
# }

# def check_resources(drink):
#     needed =  MENU[drink]["ingredients"].keys()
#     for key in needed:
#         if INVENTORY[key] >= MENU[drink]["ingredients"][key]:
#             return True
#         else:
#             return False

# def insert_money():
#     inserted_quarters = input("enter the amount of quarters!: ")
#     inserted_dimes = input("enter the amount of dimes!: ")
#     inserted_nickels = input("enter the amount of nickels!: ")
#     inserted_pennies = input("enter the amount of pennies!: ")
#     inserted_money = int(inserted_quarters) * 0.25 + int(inserted_dimes) * 0.1 +  int(inserted_nickels) * 0.05 + int(inserted_pennies) * 0.01
#     return inserted_money
        



# while True:
#     command = input("what would you like?: ")
#     if command == "off":
#         print("Thank you for using the machine ")
#         quit()
#     elif command == "report":
#         print(INVENTORY)
#     elif command == "espresso" and check_resources(command) == True:
#         if insert_money() > MENU[command]['price']:
#             INVENTORY["money"] += 1.99
#             INVENTORY["coffee"] -= MENU[command]["ingredients"]["coffee"]
#             INVENTORY["water"] -= MENU[command]["ingredients"]["water"]
#             print(f"here is your {command} and change {insert_money() - MENU[command]['price']}")
#         else:  
#             print("​Sorry that is not enough money. Money refunded.​")
#     elif command == "latte" and check_resources(command) == True:
#         if insert_money() > MENU[command]['price']:
#             INVENTORY["money"] += 2.39
#             INVENTORY["coffee"] -= MENU[command]["ingredients"]["coffee"]
#             INVENTORY["water"] -= MENU[command]["ingredients"]["water"]
#             INVENTORY["milk"] -= MENU[command]["ingredients"]["milk"]
#             print(f"here is your {command} and change {insert_money() - MENU[command]['price']}") 
#         else:
#             print("​Sorry that is not enough money. Money refunded.​")
#     elif command == "flat white" and check_resources(command) == True:
#         if insert_money() > MENU[command]['price']:
#             INVENTORY["money"] += 3.19
#             INVENTORY["coffee"] -= MENU[command]["ingredients"]["coffe"]
#             INVENTORY["water"] -= MENU[command]["ingredients"]["water"]
#             INVENTORY["milk"] -= MENU[command]["ingredients"]["milk"]
#             print(f"here is your {command} and change {insert_money() - MENU[command]['price']}")
#         else:
#             print("​Sorry that is not enough money. Money refunded.​")
#     elif command == "espresso" and check_resources(command) == False:
#         print("There is not enough ingredients in the machine")
#     elif command == "latte" and check_resources(command) == False:
#         print("There is not enough ingredients in the machine")
#     elif command == "flat white" and check_resources(command) == False:
#         print("There is not enough ingredients in the machine")
         
           
MENU = {
    'espresso': {
        'ingredients': {
            'coffee': 19,
            'water': 35,
        },
        'price': 1.99,
    },
    'latte': {
        'ingredients': {
            'coffee': 24,
            'water': 50,
            'milk': 150,
        },
        'price': 2.39,
    },
    'flat white': {
        'ingredients': {
            'coffee': 24,
            'water': 60,
            'milk': 50,
        },
        'price': 3.19,
    }
}

INVENTORY = {
    'coffee': 100,
    'water': 300,
    'milk': 300,
    'money': 0,
}

def check_resources(drink):
    needed = MENU[drink]["ingredients"].keys()
    for key in needed:
        if INVENTORY[key] >= MENU[drink]["ingredients"][key]:
            return True
        else:
          return False

def insert_money():
    inserted_quarters = input("Enter the amount of quarters: ")
    inserted_dimes = input("Enter the amount of dimes: ")
    inserted_nickels = input("Enter the amount of nickels: ")
    inserted_pennies = input("Enter the amount of pennies: ")
    inserted_money = int(inserted_quarters) * 0.25 + int(inserted_dimes) * 0.1 + \
                     int(inserted_nickels) * 0.05 + int(inserted_pennies) * 0.01
    return inserted_money

while True:
    command = input("What would you like? (Type 'off' to turn off the machine): ").lower()

    if command == "off":
        print("Thank you for using the machine.")
        break
    elif command == "report":
        print(INVENTORY)
    else:
        money = insert_money()
        if command in MENU and check_resources(command):
            if money >= MENU[command]['price']:
                INVENTORY["money"] += MENU[command]['price']
                for ingredient, quantity in MENU[command]["ingredients"].items():
                    INVENTORY[ingredient] -= quantity
                change = money - MENU[command]['price']
                if INVENTORY[ingredient] < 0: 
                  print("sorry there is not enough resources! ")
                else:
                  print(f"Here is your {command} and change: {change:.2f}")
            else:
                print("Sorry, that is not enough money. Money refunded.")
        elif command in MENU and  check_resources(command) == False:
            print("There is not enough ingredients in the machine for this drink.")
        else:
            print("Invalid command. Please choose a valid drink from the menu.")
      


