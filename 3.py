import Menu

class coffee_shop:

    def __init__(self, order, left_coffee, left_milk, left_water, left_money, coffee_needed, milk_needed, water_needed, money_needed):
        self.order = order
        self.left_coffee = left_coffee
        self.left_milk = left_milk
        self.left_water = left_water
        self.left_money = left_money
        self.coffee_needed = coffee_needed
        self.milk_needed = milk_needed
        self.water_needed = water_needed
        self.money_needed = money_needed

    def short_resources(self):
        short_resource = []
        if self.coffee_needed > self.left_coffee:
            short_resource.append('coffee')
        if self.milk_needed > self.left_milk['milk']:
            short_resource.append('milk')
        if self.water_needed > self.left_water['water']:
            short_resource.append('water')
        print(f"There is not enough {', '.join(short_resource)}")

    def have_resources(self):
        if self.coffee_needed <= self.left_coffee and self.water_needed <= self.left_water and milk_needed <= self.left_milk:
            return True
        else:
            self.short_resources()

    def money_check(self):
        print(f"Price of Your drink {self.order} is {self.money_needed}$")
        print("Insert coins(Only quarters, dimes, nickles and pennies)")
        quarters = int(input("How many quarters:"))
        dimes = int(input("How many dimes:"))
        nickles = int(input("How many nickles:"))
        pennies = int(input("How many pennies:"))
        money_inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        if money_inserted >= self.money_needed:
            return money_inserted
        else:
            print(f"Sorry that's not enough money. Money refunded")
            return 0

    def its_order(self):
        if self.have_resources():
            money_inserted = self.money_check()
            if money_inserted != 0:
                if money_inserted > money_needed:
                    print(f"Here is {round(money_inserted-self.money_needed, 2)}$ in  change")
                    print("Here is your order")
                    return money_needed, milk_needed, water_needed, coffee_needed
        return 0, 0, 0, 0


def report():
    for key in Menu.INVENTORY:
        post = "ml"
        if key =="coffe":
            post = "g"
        elif key =="money":
            post = "$"
        print(f"{key}: {Menu.INVENTORY[key]}{post}")


continue_buying = True
while continue_buying:
    valid_order = ['espresso','latte', 'cappuccino']
    order = input("What would you like? (espresso/latte/cappuccino/off/report)")
    if order == "off":
        continue_buying = False
    elif order == "report":
        report()
    else:
        if order in valid_order:
            left_coffee = Menu.INVENTORY['coffee']
            left_milk = Menu.INVENTORY['milk']
            left_water = Menu.INVENTORY['water']
            left_money = Menu.INVENTORY['money']
            money_needed = Menu.MENU[order]['price']
            coffee_needed = Menu.MENU[order]['ingredients']['coffee']
            water_needed = Menu.MENU[order]['ingredients']['water']
            milk_needed = 0
            if order != 'espresso':
                milk_needed = Menu.MENU[order]['ingredients']['milk']
            c_m = coffee_shop(
                order,
                left_coffee,
                left_milk,
                left_water,
                left_money,
                coffee_needed,
                milk_needed,
                water_needed,
                money_needed,
            )
            changes = c_m.its_order()
            Menu.INVENTORY['money'] += changes[0]
            Menu.INVENTORY['milk'] -= changes[1]
            Menu.INVENTORY['water'] -= changes[2]
            Menu.INVENTORY['coffee'] -= changes[3]
        else:
            print("Invalid input")