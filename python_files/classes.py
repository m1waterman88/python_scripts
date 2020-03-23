#!/usr/bin/env python3

"""Learn classes."""

class Animal:
    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

    # can assign variable outside of attributes
    appearance = "handsome"

    # methods: functions called within classes; they act on objects
    def eat(self):
        return "*nom-nom*"


# Inheritance: Dog, Cat share attributes __init__ def
# from Animal, the superclass. Methods in each class below
# are particular to the new class and not callable to the
# superclass or other subclasses (e.g., Dog can call pur).
# If a superclass and subclass both have an attribute with
# the same name, the subclass takes over.
class Dog(Animal):
    # methods: not __init__ functions within classes
    def bark(self):
        super().eat()
        return '"Woof!"'


class Cat(Animal):
    def pur(self):
        super().eat()
        return '"Purr..."'


swags = Dog("Swagger", "beagle", "tri-color", 7)
cran = Dog("Crannie", "beagle", "tri-color", 7)
dogs = [swags, cran]

for dog in dogs:
    print(f"{dog.name} is a {dog.appearance} {dog.age}-year-old "
          f"{dog.color} {dog.breed}.")
    print(f"{dog.name} says, {dog.bark()}")
    print(f"...unless {dog.name} is eating. Then it's, {dog.eat()}\n")

