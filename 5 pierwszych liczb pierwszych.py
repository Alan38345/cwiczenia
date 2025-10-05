y = 0
import itertools
dupa = int(input("ile pierwszych liczb pierwszych mam wypisac?"))
for liczba in itertools.count(2):
    pierw = int((liczba ** 0.5))
    for x in range(2, pierw + 1):
        reszta = liczba % x
        if y == dupa:
            exit()
        if reszta == 0:
            break
        if x == pierw:
            print(f"pierwszą liczbą pierwszą jest:{liczba}")
            y = y+1


