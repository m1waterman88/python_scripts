#!/usr/bin/env python3

"""Learn classes."""


class Animal:
    """Superclass to Dog and Cat."""

    def __init__(self, name, breed, color, sex, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.sex = sex
        self.age = age

    # can assign variable outside of attributes
    appearance = "beautiful"

    # methods: functions called within classes; they act on objects
    def eat(self):
        return "*nom-nom*"


# Inheritance: Dog, Cat share attributes __init__ def
# from Animal, the superclass. Methods in each class below
# are particular to the new class and not callable to the
# superclass or other subclasses (e.g., Dog can't call pur).
# If a superclass and subclass both have an attribute with
# the same name, the subclass takes over.
class Dog(Animal):
    """Subclass to Animal."""

    def bark(self):
        return '"Woof!"'


class Cat(Animal):
    """Subclass to Animal."""

    def pur(self):
        return '"Purr..."'

    def eat(self):
        # seemingly unnecessary.
        return super().eat()


swags = Dog("Swagger", "beagle", "tri-color", "male", 7)
cran = Dog("Crannie", "beagle", "tri-color", "female", 7)
dogs = [swags, cran]

for dog in dogs:
    print(f"{dog.name} is a {dog.appearance} {dog.age}-year-old",
          f"{dog.color} {dog.breed}. {dog.name} says, {dog.bark()}",
          f"...unless {dog.name} is eating. Then it's, {dog.eat()}")
