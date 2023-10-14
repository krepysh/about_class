from coffee_machine import CoffeeMachine

coffee_machine = CoffeeMachine()

def start():
    while True:
        beverage = input('What would you like? (espresso/latte/flat white):')

        if beverage == 'off':
            break
        try:
            if coffee_machine.enough_resources_for_drink(beverage):
                print(f'Beverage price: {coffee_machine.beverage_price(beverage)}')
                while not coffee_machine.balance_enough_for(beverage):
                    coin = input('Put coin(quarter/dime/nickel/pennie):')
                    try:
                        coffee_machine.top_up(coin)
                        print(f"Current balance: {coffee_machine.current_balance()}")
                    except AttributeError as coin_error:
                        print(coin_error)
                coffee_machine.buy_drink(beverage)
                print(coffee_machine.report())
        except AttributeError as beverage_error:
            print(beverage_error)

start()