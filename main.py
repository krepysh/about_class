from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()
while True:
    choice = input("enter your choice(latte, espresso, cappucinno!: ")
    if choice == "off":
        break 
    elif choice == "report":
        menu.get_items()
        machine.report()
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
              machine.make_coffee(drink)
    else:
        print("your order is not in the menu! ")




