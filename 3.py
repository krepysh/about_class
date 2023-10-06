class makecoffee:
    def __init__(self):
        self.MENU = {
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
        self.INVENTORY = {
            'coffee': 100,
            'water': 300,
            'milk': 300,
            'money': 0,
        }
    def check(self,order):
        self.order = order
        if self.INVENTORY['coffee'] - self.MENU[order]['ingredients']['coffee'] > 0 :            
            self.INVENTORY['coffee'] = self.INVENTORY['coffee'] - self.MENU[order]['ingredients']['coffee']  

        if self.INVENTORY['water'] - self.MENU[order]['ingredients']['water'] > 0 :           
            self.INVENTORY['water'] = self.INVENTORY['water'] - self.MENU[order]['ingredients']['water']
            
        if self.INVENTORY['milk'] - self.MENU[order]['ingredients']['milk'] > 0 :    
            self.INVENTORY['milk'] = self.INVENTORY['milk'] - self.MENU[order]['ingredients']['milk']
            print(self.INVENTORY)    
        else:
            print("Sorry there is not enough water")


    def check_money(self):
        ask_quarters = int(input("quarters ? "))
        ask_dimes = int(input("dimes ? "))
        ask_nickles = int(input("nickles ? "))
        ask_pennies = int(input("pennies ? "))
        total = ask_quarters * quarters + ask_dimes * dimes + ask_nickles * nickles + ask_pennies * pennies
        self.INVENTORY['money'] = self.INVENTORY['money'] + total
        if self.INVENTORY['money'] > self.MENU[order]['price']:
            self.INVENTORY['money'] = self.INVENTORY['money'] - self.MENU[order]['price']
            print("You have enough money. ")
        else:
            print("Sorry that's not enough money. Money refunded")



make_coffee = makecoffee()
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01 



while True:
    order = input("​What would you like? (espresso/latte/cappuccino): ")
    if order == "Off":
        print("coffee machine is Turned off")
        break
    elif order == "report":
        print(make_coffee.INVENTORY)
    elif order == "espresso":
        make_coffee.check(order)
    elif order == "latte":
        make_coffee.check(order)
    elif order == "cappuccino":
        make_coffee.check(order)
    
    print("insert coins(quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 )")
    make_coffee.check_money()
    print(f'I will make your coffe and here is your change {make_coffee.INVENTORY["money"]} $')
