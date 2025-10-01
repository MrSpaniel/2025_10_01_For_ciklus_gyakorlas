"""3. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""

jelszo = "titok"
while True:
    beirt_jelszo = input("Kérem a jelszót: ")
    if beirt_jelszo == jelszo:
        print("Sikeres belépés")
        break
    else:
        print("Helytelen jelszó, próbáld újra.")