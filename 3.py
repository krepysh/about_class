class CoffeeMachine:
    def __init__(self):
        self.MENU = {
            'espresso': {'ingredients': {'coffee': 19, 'water': 35}, 'price': 1.99},
            'latte': {'ingredients': {'coffee': 24, 'water': 50, 'milk': 150}, 'price': 2.39},
            'flat white': {'ingredients': {'coffee': 24, 'water': 60, 'milk': 50}, 'price': 3.19},
        }

        self.INVENTORY = {'coffee': 100, 'water': 300, 'milk': 300, 'money': 0}

    def check_resources(self, drink):
        needed = self.MENU[drink]["ingredients"].keys()
        for key in needed:
            if self.INVENTORY[key] < self.MENU[drink]["ingredients"][key]:
                return False
        return True

    def process_order(self, command):
        if command in self.MENU and self.check_resources(command):
            transaction = Transaction(self.MENU[command]['price'])
            if transaction.insert_money():
                self.INVENTORY["money"] += transaction.amount
                for ingredient, quantity in self.MENU[command]["ingredients"].items():
                    self.INVENTORY[ingredient] -= quantity
                change = transaction.calculate_change()
                if self.INVENTORY[ingredient] < 0 :
                    print ("sorry there is not enough resources! ")
                else:
                    print(f"Here is your {command} and change: {change:.2f}")
            else:
                print("Sorry, that is not enough money. Money refunded.")
        elif command in self.MENU and not self.check_resources(command):
            print("There is not enough ingredients in the machine for this drink.")
        else:
            print("Invalid command. Please choose a valid drink from the menu.")

    def display_report(self):
        print(self.INVENTORY)


class Transaction:
    def __init__(self, price):
        self.price = price
        self.amount = 0

    def insert_money(self):
        inserted_quarters = input("Enter the amount of quarters: ")
        inserted_dimes = input("Enter the amount of dimes: ")
        inserted_nickels = input("Enter the amount of nickels: ")
        inserted_pennies = input("Enter the amount of pennies: ")
        self.amount = int(inserted_quarters) * 0.25 + int(inserted_dimes) * 0.1 + \
                      int(inserted_nickels) * 0.05 + int(inserted_pennies) * 0.01
        return self.amount >= self.price

    def calculate_change(self):
        return self.amount - self.price


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    while True:
        command = input("What would you like? (Type 'off' to turn off the machine): ").lower()

        if command == "off":
            print("Thank you for using the machine.")
            break
        elif command == "report":
            coffee_machine.display_report()
        else:
            coffee_machine.process_order(command)
