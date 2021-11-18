from datetime import datetime
import json
from pizzas import *
import sys


def pizza_to_json(pizza):
    with open("purchased.json") as purchased_pizzas:
        purchased = json.load(purchased_pizzas)
    purchased.append(dict(pizza))
    with open("purchased.json", 'w') as purchased_pizzas:
        json.dump(purchased, purchased_pizzas, indent=4)
    print("Thank you!")


with open("pizzas_week.json") as pizzas_week:
    pizza_week = json.load(pizzas_week)
weekday = datetime.today().isoweekday()
pizza_name = pizza_week[str(weekday)]
pizza = eval(pizza_name + '()')

print("Pizza of the day:")
print(pizza, "price: ", pizza.price, sep='')

while True:
    print("\nEnter a number:\n"
          "1: Buy pizza of the day\n"
          "2: Add some extra ingredients")
    try:
        answer = int(input())
        if answer == 1:
            pizza_to_json(pizza)

        elif answer == 2:
            with open("extra_ingredients.json") as extra_ingr:
                extra = json.load(extra_ingr)
            print("Any extra ingredient costs 5 uah")
            for key, value in extra.items():
                print(key + ": " + value)
            num = input("Enter a number: ")
            if num not in extra.keys():
                raise ValueError("Enter a number from the list")
            setattr(pizza, extra[num], 50)
            setattr(pizza, 'price', pizza.price + 5)
            print("Current pizza price:", pizza.price, "uah")
            choice = input("Buy pizza (y) or add another ingredient(n)? ")
            if choice == 'y':
                pizza_to_json(pizza)

        elif not answer:
            sys.exit()

        else:
            print("Enter a number from the list")

    except(TypeError, ValueError) as error:
        print(error)
