primes = {1: 2, 2: 3, 4: 7, 7: 17}
print(primes)   # primes prints the dictionary
print(primes[4])  # prints the value to the key "4", which is 7
print(primes[primes[4]])  # thus, primes[primes[4]] is primes[7], which is 17


# <key> in/not <dict>  ->  returns boolean value
print(1 in primes)  # True
print(1 not in primes)  # False
print(3 in primes)  # False
if 4 in primes:
    print(primes[4])

"""
A useful dictionary method is get. It does the same thing as indexing,
 but if the key is not found in the dictionary, it returns another
specified value instead; default is 'None', but you can specify with
a second positional argument.
"""
print(primes.get(2))  # in dict, so print value: 3
print(primes.get(5))  # not in dict and no explicit default, so 'None'
print(primes.get(6, "Nope"))  # not in dict, explicit default set, so 'Nope'

lister = [1, 54, 63, 53, 22, 39, 76, 2]
lister.sort()  # sort the list in asc order
print(lister[::-1])  # print in reverse
lister.reverse()

"""
List comprehensions are a useful way of quickly creating lists
whose contents obey a simple rule.
List comprehensions are inspired by set-builder notation in mathematics.
"""
cubes = [i**3 for i in range(5)]  # print cubes of range 5: [0, 1, 8, 27, 64]
print(cubes)

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)


# join is the opposite of split
print(", ".join(["spam", "eggs", "ham"]))  # prints "spam, eggs, ham"
print("Hello ME".replace("ME", "world"))  # prints "Hello world"
print("This is a sentence.".startswith("This"))  # prints "True"
print("This is a sentence.".endswith("sentence."))  # prints "True"
print("spam, eggs, ham".split(", "))  # prints "['spam', 'eggs', 'ham']"


# all, any, enumerate
if all([i > 5 for i in nums]):
    print("All larger than 5")  # True if all meet condition

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")  # True if some meet condition

for v in enumerate(nums):
    print(v)


def count_char(text: str, char: str) -> int:
    """Count chars in text."""
    count = 0
    for c in text.casefold():
        if c == char:
            count += 1
    return count


# write a file, read it, and print percentage of file each letter holds
file = open("newfile.txt", "w")
file.write("""Ornhgvshy vf orggre guna htyl.
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
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!""")
file.close()
filename = "newfile.txt"
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))
