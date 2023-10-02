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

# def check()

while True:
    order = input("​What would you like? (espresso/latte/cappuccino): ")
    if order == "Off":
        print("coffee machine is Turned off")
        break
    elif order == "report":
        print(INVENTORY)
    elif order == "espresso":
        if INVENTORY['coffee'] - MENU['espresso']['ingredients']['coffee'] > 0 :
            print("okey")
            INVENTORY['coffee'] = INVENTORY['coffee'] - MENU['espresso']['ingredients']['coffee']
            print(INVENTORY, end=" ")
        else:
            print("Sorry there is not enough water")
    # elif order == "latte":
    # elif order == "cappuccino":
