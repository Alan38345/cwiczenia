liczba = int(input("wypisz liczbe ktora chcesz sprawdzic:"))
pierw = int((liczba**0.5))
for x in range(2,pierw+1):
    reszta = liczba % x
    if reszta == 0:
        print("to nie jest liczba pierwsza")
        break
    if x == pierw:
        print("to jest liczba pierwsza")


