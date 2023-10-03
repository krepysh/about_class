from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()

is_on = True
while is_on:
    order_name = input(menu.get_items())    
    if order_name == "Off":
        break
    elif order_name == "report":
        print(coffe_maker.report())
    elif order_name not in menu.get_items():
        print('we do not have it')
    else:
        drink = menu.find_drink(order_name)
         
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
        else:
            print("goodbye")
            break

        