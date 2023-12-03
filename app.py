# Advent of code 2024
# P1C1

from re import sub as s

def p1c1():
    with open("challenge1_input.txt", 'r') as f:
        n = [s(r"\D", "", l) for l in f.readlines()]
        return sum([int(s) for s in (map(lambda s: s[0]+s[-1],[c for c in n]))])


print(p1c1())  