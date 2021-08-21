#!/usr/bin/env python3

"""Work in progress."""


def roman_numeral_converter(numeral):
    """Convert between Roman and Arabic numerals."""
    is_roman = False

    roman_translation = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    for character in str(numeral):
        if character in roman_translation:
            is_roman = True
            break

    sum = 0

    # numeral is Roman.
    if is_roman:
        for character in str(numeral):
            sum += roman_translation[character]

        return sum

    for character in str(numeral):
        pass

    # numeral is Arabic.
    return sum


# test_list = ['VIC', 5632]
test_list = ['MMXVIII']

for numeral in map(roman_numeral_converter, test_list):
    print(numeral)
