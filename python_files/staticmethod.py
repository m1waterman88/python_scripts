#!/usr/bin/env python3

"""
Learn static methods.

Static methods are similar to class methods, except
they don't receive any additional arguments; they are
identical to normal functions that belong to a class.

Mark with decorator: @staticmethod.
"""


class Pizza:
    """Make a pizza."""

    def __init__(self, toppings: "list[str]"):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping: str) -> bool:
        """Ensure no anchovies end up on a pie."""
        if topping == "anchovies":
            # raise ValueError("No anchovies!")
            return False

        return True


ingredients = ["cheese", "onion", "spam"]
# ingredients = ["cheese", "onion", "anchovies"]

if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

    print("Toppings:")
    for index, topping in enumerate(pizza.toppings):
        print(f"{index + 1}: {topping}")
else:
    print("No anchovies!")
