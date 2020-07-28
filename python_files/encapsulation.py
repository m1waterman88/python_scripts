#!/usr/bin/env python3

"""
Learn encapsulation/data hiding.

Weakly private methods and attributes have a single underscore at the beginning.
This signals that they are private, and shouldn't be used by external code. However, it is mostly only a convention, and does not stop external code from accessing them.
Its only actual effect is that from module_name import * won't import variables that start with a single underscore.
"""


class Queue:

    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)


"""
Strongly private methods and attributes have a double underscore at the beginning of their names. This causes their names to be mangled, which means that they can't be accessed from outside the class.
The purpose of this isn't to ensure that they are kept private, but to avoid bugs if there are subclasses that have methods or attributes with the same names.
Name mangled methods can still be accessed externally, but by a different name. The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.
"""

class Spam:

    __egg = 7

    def print_egg(self):
        print(self.__egg)


s = Spam()

# returns 7
s.print_egg()
# returns 7
print(s._Spam__egg)
# returns AttributeError
print(s.__egg)
