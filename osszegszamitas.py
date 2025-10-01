"""Összegszámítás"""

szam = int(input("Adjon meg egy egész számot 1-től, mínuszba nem mehet!"))
osszeg = 0
for i in range(1, szam + 1):
    osszeg += i
print(f"Az 1-től {szam}-ig az összeg:{osszeg}")