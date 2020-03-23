#!/usr/bin/env python3

"""Learn classes."""

class Person():
    """Create empty class for person."""

    pass


person = Person()


first_key = "first"
first_val = "Mike"
setattr(person, first_key, first_val)
# print(person.first)


first = getattr(person, first_key)
print(first)


# person.first = "Mike"
# person.last = "Waterman"

# print(person.first)
# print(person.last)
