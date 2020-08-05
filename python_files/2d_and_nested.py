#!/usr/bin/env python3

"""."""

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# use nested for-loop for 2d array

"""
for row in number_grid:
    for col in row:
        print(col)
"""

# get the index of the row as well

for i, row in enumerate(number_grid):
    for j, col in enumerate(row):
        print(f"[{i}][{j}] - {col}")


def translate(phrase):
    """Giraffe language: change vowels to 'g's."""
    translation = ""

    for letter in phrase:
        if letter.casefold() in "aeiou":
            letter = "G" if letter.isupper() else "g"
        translation += letter
    print(translation)


"""
translate("Dog")
translate("Cat")
translate("Beagle")
translate("To be or not to be")
translate("Owl")
translate("The Office")
"""
