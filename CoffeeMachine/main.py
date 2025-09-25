# Data

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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


# Functions

def report(Resources):
    """Reports the remaining resources and profit"""
    print(f"Water: {Resources['water']}ml")
    print(f"Milk: {Resources['milk']}ml")
    print(f"Coffee: {Resources['coffee']}g")
    print(f"Money: ${Resources['money']}")


def checkResources(choice, res):
    """ Checks if there are sufficient resources"""
    choice = MENU[choice]['ingredients']
    for j in choice:
        if res[j] < choice[j]:
            print(f"Sorry there is not enough {j}")
            return False
    return True


def payement():
    """Calculates total payment"""
    print("Please insert coins.")
    total = 0
    total += (int(input("How many quarters?: ")) * 0.25) + (int(input("How many dimes?: ")) * 0.10)
    total += (int(input("How many nickels?: ")) * 0.05) + (int(input("How many pennies?: ")) * 0.01)
    return total


# Main Loop

while True:
    nextAction = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if nextAction == "report":
        report(resources)
    elif nextAction == "off":
        exit()
    elif nextAction in ['espresso', 'latte', 'cappuccino']:
        if checkResources(nextAction, resources):
            moneyEntered = payement()
            cost = MENU[nextAction]['cost']
            if moneyEntered < cost:
                print(f"Sorry that's not enough money as {nextAction} costs ${cost}. Money refunded.")
                continue
            elif moneyEntered > cost:
                print(f"Here is ${'{0:.2f}'.format(moneyEntered - cost)} in change.")

            for i in MENU[nextAction]['ingredients']:
                resources[i] -= MENU[nextAction]['ingredients'][i]
            resources['money'] += MENU[nextAction]['cost']
            print(f"Here is your {nextAction}  Enjoy!")
    else:
        print("Invalid input")
