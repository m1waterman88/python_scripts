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


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


print("\n")
let_perc = 0
for char in 'abcdefghijklmnopqrstuvwxyz':
    perc = 100 * count_char(text.casefold(), char) / len(text)
    let_perc += perc
    print(f"{char.upper()} - {round(perc, 2)}%")

spec_perc = 0
for char in ". \n\r\t\"!?@$%^&#+-='*:;,_~`/|()[]{}<>":
    perc = 100 * count_char(text, char) / len(text)
    spec_perc += perc

sum = let_perc + spec_perc
assert sum == 100, "sum != 100"  # DON'T use parentheses with asserts

print("\n"
      f"letters: {round(let_perc, 2)}%\n"
      f"special chars: {round(spec_perc, 2)}%\n"
      f"total: {sum}%"
      "\n")
