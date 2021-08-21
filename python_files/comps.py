#!/usr/bin/env python3

"""Don't create so many stairs that you won't climb them."""


def staircase(stair_count: int, symbol="#") -> str:
    """Make a stair case out of a symbol."""
    for stair in range(stair_count):
        space = " " * (stair_count - 1 - stair)
        stair_material = symbol * (stair + 1)

        print(space + stair_material)


staircase(8)
