from idlelib.configdialog import changes

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

make_coffee = True


def resource_report():
    for key, value in resources.items():
        if key == 'water' or key == 'milk':
            print(f"{key} : {value}ml")
        elif key == 'money':
            print(f"{key} : {value}$")
        else:
            print(f"{key} : {value}g")


def check_if_sufficient(quarters, dimes, nickels, pennies, coffee):
    total_amount = 0.25 * float(quarters) + 0.10 * float(dimes) + 0.05 * float(nickels) + 0.01 * float(pennies)
    if total_amount > MENU[coffee]['cost']:
        change = total_amount - MENU[coffee]['cost']
        return True, change, MENU[coffee]['cost']
    else:
        return False, total_amount


def process_payment(in_coffee):
    print("Please insert coins....")
    quarters = input("How many quarters? : ")
    dimes = input("How many dimes? : ")
    nickels = input("How many nickels? : ")
    pennies = input("How many pennies? : ")
    res = check_if_sufficient(quarters, dimes, nickels, pennies, in_coffee)
    if len(res) == 3:
        change = res[1]
        if change > 0:
            print(f"Here are your :{round(change, 2)}$")
        cost = res[2]
        resources['money'] += cost
        print("Transaction is successful...")
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded:  {res[1]}")
        return False


def check_is_available(water, milk, coffee, resources_in):
    return resources_in['water'] - water >= 0 and resources_in['milk'] - milk >= 0 and resources_in[
        'coffee'] - coffee >= 0


def check_resources(in_coffee):
    water = MENU[in_coffee]['ingredients']['water']
    coffee = MENU[in_coffee]['ingredients']['coffee']
    milk = MENU[in_coffee]['ingredients']['milk']
    return check_is_available(water, milk, coffee, resources)


def consume_resources(in_coffee):
    water = MENU[in_coffee]['ingredients']['water']
    coffee = MENU[in_coffee]['ingredients']['coffee']
    milk = MENU[in_coffee]['ingredients']['milk']
    resources['water'] -= water
    resources['coffee'] -= coffee
    resources['milk'] -= milk


def process_coffee(input_coffee):
    if input_coffee == 'cappuccino' or input_coffee == 'espresso' or input_coffee == 'latte':
        if check_resources(input_coffee):
            if process_payment(input_coffee):
                consume_resources(input_coffee)
                print(f"Here is your {input_coffee}. Enjoy!.")
            else:
                print("Sorry transaction failed..Not enough money!!!")
        else:
            print("Please refill the milk, coffee, water...!!")
    else:
        print("Please check the input coffee if correct?")


def make_ccd():
    while make_coffee:
        input_coffee = str(input("What would you like? (espresso/ latte/ cappuccino: )"))
        if input_coffee == 'report':
            resource_report()
        elif input_coffee == 'off':
            print("Turning off....")
            break
        else:
            process_coffee(input_coffee)
            resource_report()


make_ccd()
