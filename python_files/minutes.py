#!/usr/bin/env python

"""
Solve this GitHub code problem.

https://github.com/dvitsios/codesignal-my-solutions/tree/master/phoneCall
"""


def get_max_minutes(min1: int, min2_10: int, min11: int, cents: int) -> int:
    """Get the max number of minutes for the number of cents provided."""
    minutes = 0
    rate = min1

    while cents:
        minutes += 1

        if minutes == 2:
            rate = min2_10
        elif minutes > 10:
            rate = min11

        cents -= rate

        if cents < 0:
            minutes -= 1

    return minutes


print(get_max_minutes(3, 1, 2, 20))
