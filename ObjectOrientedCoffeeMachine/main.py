from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

next_action = ''
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

while next_action != 'off':

    next_action = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    order = my_menu.find_drink(next_action)

    if next_action == "report":
        my_coffee_maker.report()
        my_money_machine.report()

    elif order != None:
        if my_coffee_maker.is_resource_sufficient(order):
            if my_money_machine.make_payment(order.cost):
                my_coffee_maker.make_coffee(order)