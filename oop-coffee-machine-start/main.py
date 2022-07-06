from random import choice
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker
money_machine = MoneyMachine
menu = Menu()

is_on = True

while is_on:
    print("\n\nCoffee Machine is ON!")
    options = menu.get_items()
    choice = input(f"What would you like? {options}:  ")
    if choice == "off":
        is_on = False
        print("Coffee Machine is OFF!")
    elif choice == "report":
        print("Your coffee machine report!\n")
        print(coffee_machine.report())
        print("Profit till now is!\n")
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        print
        print("\n\nYou choosed the drink: ", drink.name, "\nThe Cost of drink is: $", drink.cost,"\n\n")
        if money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)

