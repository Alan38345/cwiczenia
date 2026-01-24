
def czy_pierwsza(n):
    if n < 2:
        return False
    else:
        for x in range(2,int(n**0.5)+1):
            if n % x == 0:
                return False
    return True
ile = int(input("Ile kolejnych liczb pierwszych mam wypisac?"))
liczba = 2
sprawdzone = 0
while sprawdzone<ile:
    if czy_pierwsza(liczba):
        print(liczba)
        sprawdzone+=1
    liczba+=1

