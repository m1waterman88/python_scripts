#!/usr/bin/env python3

"""
Learn properties.

Properties provide a way of customizing access to instance
attributes. They are created by putting the property decorator
above a method, which means when the instance attribute with
the same name as the method is accessed, the method will be
called instead.

One common use of a property is to make an attribute read-only.

Properties can also be set by defining setter/getter functions.
The setter function sets the corresponding property's value.
The getter gets the value.
To define a setter, you need to use a decorator of the same name
as the property, followed by a dot and the setter keyword.
The same applies to defining getter functions.
"""

from getpass import getpass


class Pizza:
    """Make a pizza."""

    def __init__(self, toppings: list) -> None:
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value: bool) -> None:
        """Apparently the owner has pineapple locked down."""
        if value:
            password = getpass("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")


pizza = Pizza(["cheese", "tomato"])
# print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True
# print(pizza.pineapple_allowed)
for index, topping in enumerate(pizza.toppings):
    print(f"{index + 1}: {topping}")
