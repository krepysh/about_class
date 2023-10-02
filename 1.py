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


class Coffee_Machine:
    def __init__(self):
        self.money = 0
        self.inventory = INVENTORY
        self.menu = MENU
        self.is_on = True

    def report(self):
        print(f"Water: {self.inventory['water']}ml")
        print(f"Milk: {self.inventory['milk']}ml")
        print(f"Coffee: {self.inventory['coffee']}g")
        print(f"Money: ${self.money}")

    def check_resources(self, drink):
        for item in self.menu[drink]['ingredients']:
            if self.inventory[item] < self.menu[drink]['ingredients'][item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True
    
    def clean_input_money(input):
        if input.isdigit() == False:
            return 0
        else:
            return input
        
    def process_coins(self):
        print("Please insert coins.")
        total = 0
        total += int(Coffee_Machine.clean_input_money(input("How many quarters?: "))) * 0.25
        total += int(Coffee_Machine.clean_input_money(input("How many dimes?: "))) * 0.1
        total += int(Coffee_Machine.clean_input_money(input("How many nickles?: "))) * 0.05
        total += int(Coffee_Machine.clean_input_money(input("How many pennies?: "))) * 0.01
        return total

    def make_coffee(self, drink):
        for item in self.menu[drink]['ingredients']:
            self.inventory[item] -= self.menu[drink]['ingredients'][item]
        self.money += self.menu[drink]['price']
        print(f"Here is your {drink}. Enjoy!")

    def turn_off(self):
        self.is_on = False

    
def __main__():
    coffee_machine = Coffee_Machine()
    while coffee_machine.is_on:
        choice = input("What would you like? (espresso/latte/flat white): ").lower()
        if choice != 'espresso' and choice != 'latte' and choice != 'flat white' and choice != 'off'  and choice != 'report':
            print('your choise is not valid, please try again')
            __main__()
        if choice == 'off':
            coffee_machine.turn_off()
        elif choice == 'report':
            coffee_machine.report()
        else:
            if coffee_machine.check_resources(choice):
                payment = coffee_machine.process_coins()
                if payment < coffee_machine.menu[choice]['price']:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    change = round(payment - coffee_machine.menu[choice]['price'], 2)
                    print(f"Here is ${change} in change.")
                    coffee_machine.make_coffee(choice)


__main__()