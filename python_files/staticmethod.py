#!/usr/bin/env python3

"""
Learn static methods.

Static methods are similar to class methods, except
they don't receive any additional arguments; they are
identical to normal functions that belong to a class.

Mark with decorator: @staticmethod.
"""


class Pizza:

    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True


ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
    print(pizza.toppings)
else:
    print("No!")
