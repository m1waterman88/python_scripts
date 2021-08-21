#!/usr/bin/env python3

"""Return number of characters in given text."""

import string

alpha = string.ascii_lowercase
nums = string.digits
any_char = string.printable
spec_chars = string.whitespace + string.punctuation

text = """Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcenfr fv orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orgnf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arrire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""


def count_characters(text: str, character: str) -> int:
    """Count chars in text."""
    count = 0
    for char in text.casefold():
        if char == character:
            count += 1
    return count


letter_percentage = 0
number_percentage = 0
special_percentage = 0


for char in any_char:
    perc = 100 * count_characters(text, char) / len(text)

    if char in alpha:
        letter_percentage += perc
        print(f"{char.upper()} - {round(perc, 2)}%")
    elif char in nums:
        number_percentage += perc
    elif char in spec_chars:
        special_percentage += perc

total_percentage = letter_percentage + number_percentage + special_percentage

# DON'T use parentheses with asserts
assert total_percentage == 100, f"total percentage must equal 100\npercentage is {sum}"

print("",
      f"letters: {round(letter_percentage, 2)}%",
      f"numbers: {round(number_percentage, 2)}%",
      f"special chars: {round(special_percentage, 2)}%",
      f"total: {total_percentage}%",
      "",
      sep="\n")
