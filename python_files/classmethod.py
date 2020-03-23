#!/usr/bin/env python3

"""
Learn class methods.

Denoted with a decorator: @classmethod.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        """
        new_square is a class method and is called on the class,
        rather than on an instance of the class. It returns a new 
        object of the class cls.
        """
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())

