from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


choice = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


item = choice.find_drink("espresso")

# print(item.ingredients)
coffee_maker.make_coffee(item)
# coffee_maker.report()


# choice.get_items()