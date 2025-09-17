# 1. feladat
szam = int(input("Adj meg egy egész számot: "))

if szam % 3 == 0 and szam % 5 == 0:
    print("A szám osztható 3-mal és 5-tel is.")
elif szam % 3 == 0:
    print("A szám osztható 3-mal.")
elif szam % 5 == 0:
    print("A szám osztható 5-tel.")
else:
    print("A szám nem osztható sem 3-mal, sem 5-tel.")
