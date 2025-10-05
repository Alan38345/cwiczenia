def spr(n):
    if n < 2:
        return False
    for x in range(2,int(n**0.5)+1):
        if n % x == 0:
            return False
    return True
liczba = int(input("jaka liczbe mam sprawdzic czy jest pierwsza:"))

if spr(liczba) == True:
    wynik = f"{liczba} jest liczbą pierwszą"
else:
    wynik = f"{liczba} nie jest liczba pierwsza"
with open("wynik.txt", "w") as plik:
    plik.write(wynik)