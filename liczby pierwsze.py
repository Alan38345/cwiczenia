liczba = int(input("ile kolejnych cyfr od 1 mam sprawdzic czy sa pierwsze?:"))
to = 1
for x in range(liczba):
    pierw = int(x**0.5)
    for y in range(2, pierw+1):
        reszta = (x % y)
        if reszta == 0:
            print("ta liczb nie jest liczba pierwsza")




