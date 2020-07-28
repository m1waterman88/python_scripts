#!/usr/bin/env python3

"""See who's a good pupper."""


def hi(name):
    """Greet puppers."""
    print(f"Welcome, {name}!")


dogs = ["Swagger", "Crannie", "Goose", "Rookie",
        "Keekee", "Link", "Cha-cha", "Snoops"]

for name in dogs:
    hi(name)

    print("Who's a good pupper?!")

    if name != dogs[-1]:
        print("Next dog")
    else:
        print("Look at all of these dogs!")
