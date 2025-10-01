"""Nem feltétlen úgy kell megoldani, hogy a felhasználó beírja kő/papír/olló.
Meg lehet oldani számokkal is, pl (kő (1), papír (2), olló (3). Ez legyen jelezve az inputnál is!
Legalább 2-3 if-re szükséged lesz a megoldáshoz."""

import random
random_szam = random.randint(1, 3)
valasztas = int(input("Válassz: kő (1), papír (2), olló (3): "))
if valasztas < 1 or valasztas >3:
    print("Hibás választás!")
if valasztas == random_szam:
    print("Döntetlen!")
elif (valasztas == 1 and random_szam == 3) or (valasztas == 2 and random_szam == 1) or (valasztas == 3 and random_szam == 2):
    print("Nyertél!")
else:
    print("Vesztettél!")