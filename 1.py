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
        'ingredients':{
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

while True:
    input_coffee = input("What would you like? (espresso/latte/flat white): ").lower()

    if input_coffee == 'off':
        exit()
    elif input_coffee == 'report':
        print(f"Water: {INVENTORY['water']}ml")
        print(f"Milk: {INVENTORY['milk']}ml")
        print(f"Coffee: {INVENTORY['coffee']}g")
        print(f"Money: ${INVENTORY['money']}")
    
    coffee = MENU.get(input_coffee)
    if coffee:
        not_enough_resource = False
        for ingredient, quantity in coffee['ingredients'].items():
            if INVENTORY.get(ingredient, 0) < quantity:
                print(f"Sorry there is not enough {ingredient}.")
                not_enough_resource = True
                break
        
        if not_enough_resource:
            continue
    

        cost = coffee['price']
        print(f"The price of the {input_coffee} is ${cost}")
        print("Please insert coins!")
        try:
            quarters = int(input("How many quarters? ")) * 0.25
        except ValueError:
            quarters = 0
            
        try:
            dimes = int(input("How many dimes? ")) * 0.10
        except ValueError:
            dimes = 0

        try:
            nickels = int(input("How many nickels? ")) * 0.05
        except ValueError:
            nickels = 0

        try:
            pennies = int(input("How many pennies? ")) * 0.01
        except ValueError:
            pennies = 0
        
        total_inserted = quarters + dimes + nickels + pennies



        if total_inserted < cost:
            print("That's not enough money!")
            print(f"{total_inserted}$ refunded.")
        else:
            change = total_inserted - cost
            change = round(change, 2)
            INVENTORY['money'] += cost
            print(f"Here is your {input_coffee}. Enjoy!")

            for ingredient, quantity in coffee['ingredients'].items():
                INVENTORY[ingredient] -= quantity

            if change > 0:
                print(f"Here is ${change}$ in change")
    else:
        print("Invalid selection; Please choose from either espresso, latte, or flat white")



