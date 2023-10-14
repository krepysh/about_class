import Menu


def short_resources(coffe_needed,water_needed,milk_needed):
    short_resource = []
    if coffe_needed>Menu.INVENTORY['coffee']:
        short_resource.append('coffee')
    if milk_needed>Menu.INVENTORY['milk']:
        short_resource.append('milk')
    if water_needed>Menu.INVENTORY['water']:
        short_resource.append('water')
    print(f"There is not enough {', '.join(short_resource)}")

def have_resources(coffe_needed,water_needed,milk_needed):
    if coffe_needed <= Menu.INVENTORY['coffee'] and water_needed <= Menu.INVENTORY['water'] and milk_needed <= Menu.INVENTORY['milk']:
        return True
    else:
        short_resources(coffe_needed,water_needed,milk_needed)

def money_check(taken_order,money_needed):
    print(f"Price of Your drink {taken_order} is {money_needed}$")
    print("Insert coins(Only quarters, dimes, nickles and pennies)")
    quarters = int(input("How many quarters:"))
    dimes = int(input("How many dimes:"))
    nickles = int(input("How many nickles:"))
    pennies = int(input("How many pennies:"))
    money_inserted = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    if money_inserted >= money_needed:
        return money_inserted
    else:
        print( f"Sorry that's not enough money. Money refunded")
        return 0


def its_order(taken_order):
    money_needed = Menu.MENU[taken_order]['price']
    coffe_needed = Menu.MENU[taken_order]['ingredients']['coffee']
    water_needed = Menu.MENU[taken_order]['ingredients']['water']
    milk_needed = 0
    if taken_order != 'espresso':
        milk_needed = Menu.MENU[taken_order]['ingredients']['milk']

    if have_resources(coffe_needed,water_needed,milk_needed):
        money_inserted = money_check(taken_order, money_needed)
        if money_inserted!=0:
            Menu.INVENTORY['money'] += money_needed
            if money_inserted>money_needed:
                print(f"Here is {round(money_inserted-money_needed, 2)}$ in  change")
                Menu.INVENTORY['milk'] -= milk_needed
                Menu.INVENTORY['water'] -= water_needed
                Menu.INVENTORY['coffee'] -= coffe_needed
                print("Here is your order")

def report():
    for key in Menu.INVENTORY:
        post = "ml"
        if key=="coffe":
            post = "g"
        elif key=="money":
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
            its_order(order)
        else:
            print("Invalid input")