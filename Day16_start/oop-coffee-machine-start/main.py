from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

take_coffee = CoffeeMaker()
menu = Menu()
while is_on:
    input_coffee = str(input(f"What would you like? ({menu.get_items()}): "))
    if input_coffee != 'report' and input_coffee !='off':
        menu_item = menu.find_drink(input_coffee)
        if menu_item:
            check_resources = take_coffee.is_resource_sufficient(menu_item)
            if check_resources:
                process_order = MoneyMachine()
                is_payment = process_order.make_payment(menu_item.cost)
                if is_payment:
                    take_coffee.make_coffee(menu_item)
    elif input_coffee == 'report':
        take_coffee.report()
    else:
        print("Turning off..!!")
        break
