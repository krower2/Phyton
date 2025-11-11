from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True

while machine_on:
    options = menu.get_items()
    coffe_choose = input(f"Which coffee would you like? ({options}): ")
    if coffe_choose == "off":
        machine_on = False
    elif coffe_choose == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffe_choose)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


