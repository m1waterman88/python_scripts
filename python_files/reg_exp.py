#!/usr/bin/env python3

"""Learn regular expressions."""

import re

s = input("Do you agree?\n")

# search arg2 to see if arg1 is inside
# can design input to be stict or loose
if re.search("^y(es)?$", s, re.IGNORECASE):
    print("Agreed.")
elif re.search("^n(o)?", s.casefold()):
    print("Not agreed.")
