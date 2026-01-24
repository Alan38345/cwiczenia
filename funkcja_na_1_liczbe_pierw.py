import sys
def spr(liczba):
    dupsko = float(liczba)
    dupa = int(dupsko)
    if dupa < 2:
        return False
    if not liczba.isdigit():
        print("ulamek nigdy nie jest liczba pierwsza")
        sys.exit()
    for x in range(2,int(dupa**0.5)+1):
        if dupa % x == 0:
            return False
    return True  