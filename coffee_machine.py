from typing import Dict

class CoffeeMachine:
    __menu = {
        'espresso': {
            'ingredients': {
                'coffee': 19,
                'water': 35,
                'milk': 0
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
    __inventory = {
        'coffee': 100,
        'water': 300,
        'milk': 300,
        'money': 0,
    }

    __coin_value = {
        'quarter': 0.25,
        'dime': 0.10,
        'nickel': 0.05,
        'pennie': 0.01
    }

    def __init__(self):
        self.__current_balance = 0

    def current_balance(self) -> float:
        return self.__current_balance

    def beverage_price(self, beverage_name):
        self.check_beverage_existence(beverage_name)

        return self.__menu[beverage_name]['price']

    def check_beverage_existence(self, beverage_name: str):
        if beverage_name not in self.__menu:
            raise AttributeError('There is no drink with this name')

    def enough_resources_for_drink(self, drink_name: str) -> bool:
        self.check_beverage_existence(drink_name)

        drink_ingredients = self.__menu[drink_name]['ingredients']
        if drink_ingredients['water'] > self.__inventory['water']:
            raise AttributeError('Sorry, there is not enough water')

        if drink_ingredients['coffee'] > self.__inventory['coffee']:
            raise AttributeError('Sorry, there is not enough coffee')

        if drink_ingredients['milk'] > self.__inventory['milk']:
            raise AttributeError('Sorry, there is not enough milk')

        return True

    def top_up(self, coin: str):
        if coin not in self.__coin_value:
            raise AttributeError('Coin name is invalid')

        self.__current_balance += self.__coin_value[coin]

    def refund(self, amount: float):
        if amount > self.__current_balance:
            raise AttributeError('Refund amount is more than balance.')

        self.__current_balance -= amount

    def buy_drink(self, name: str):
        self.check_beverage_existence(name)

        beverage = self.__menu[name]
        if beverage['price'] > self.__current_balance:
            raise AttributeError("Sorry, that's not enough money. Money refunded")

        beverage_ingredients = beverage['ingredients']
        if self.enough_resources_for_drink(name):
            self.__inventory['milk'] -= beverage_ingredients['milk']
            self.__inventory['water'] -= beverage_ingredients['water']
            self.__inventory['coffee'] -= beverage_ingredients['coffee']

            if self.__current_balance > beverage['price']:
                refund_amount = self.__current_balance - beverage['price']
                print(f'Current balance is greater than beverage. Refund amount is ${refund_amount}')
                self.refund(refund_amount)

            self.__inventory['money'] += self.__current_balance
            self.__current_balance = 0

    def balance_enough_for(self, beverage_name: str) -> bool:
        self.check_beverage_existence(beverage_name)

        return self.__current_balance >= self.__menu[beverage_name]['price']

    def report(self) -> str:
        return f"""
            Water: {self.__inventory['water']}
            Milk: {self.__inventory['milk']}
            Coffee: {self.__inventory['coffee']}
            Money: {self.__inventory['money']}
        """