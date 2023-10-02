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
    'cappuccino': {
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

def check(order):
    if INVENTORY['coffee'] - MENU[order]['ingredients']['coffee'] > 0 :            
        INVENTORY['coffee'] = INVENTORY['coffee'] - MENU[order]['ingredients']['coffee']  

    if INVENTORY['water'] - MENU[order]['ingredients']['water'] > 0 :           
        INVENTORY['water'] = INVENTORY['water'] - MENU[order]['ingredients']['water']
        
    if INVENTORY['milk'] - MENU[order]['ingredients']['milk'] > 0 :    
        INVENTORY['milk'] = INVENTORY['milk'] - MENU[order]['ingredients']['milk']
        print(INVENTORY)    
    else:
        print("Sorry there is not enough water")

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01 

def check_money():
    ask_quarters = int(input("quarters ? "))
    ask_dimes = int(input("dimes ? "))
    ask_nickles = int(input("nickles ? "))
    ask_pennies = int(input("pennies ? "))
    total = ask_quarters * quarters + ask_dimes * dimes + ask_nickles * nickles + ask_pennies * pennies
    INVENTORY['money'] = INVENTORY['money'] + total
    if INVENTORY['money'] > MENU[order]['price']:
        INVENTORY['money'] = INVENTORY['money'] - MENU[order]['price']
        print("You have enough money. ")
    else:
        print("Sorry that's not enough money. Money refunded")

    

while True:
    order = input("​What would you like? (espresso/latte/cappuccino): ")
    if order == "Off":
        print("coffee machine is Turned off")
        break
    elif order == "report":
        print(INVENTORY)
    elif order == "espresso":
        check(order)
    elif order == "latte":
        check(order)
    elif order == "cappuccino":
        check(order)
    
    print("insert coins(quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 )")
    check_money()
    print(f'I will make your coffe and here is your change {INVENTORY["money"]} $')
