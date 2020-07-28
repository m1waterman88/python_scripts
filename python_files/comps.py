def staircase(n: int) -> str:
    for i in range(n):
        spc = " " * (n - 1 - i)
        pnd = "#" * (i + 1)

        print(spc + pnd)


staircase(6)
