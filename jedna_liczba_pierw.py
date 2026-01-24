from funkcja_na_1_liczbe_pierw import spr
def main():
    liczba = input("podaj liczbe do weryfikacji")

    if spr(liczba) == True:
        print( " ta liczbajest liczbą pierwszą")
    else:
        print("ta liczba nie jest liczba pierwsza")
main()