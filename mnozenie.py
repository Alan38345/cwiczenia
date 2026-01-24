def druga_liczba():
        dupa = float(input("podaj druga liczbe"))
        return dupa


def dzialanie():
    komenda = input("Podaj symbol operacji ktora chcesz wykonac ")
    return komenda


def main():
    wynik = float(input("podaj pierwsza liczbe "))
    while True:
        komenda = dzialanie()
        if komenda == "*":
            a = druga_liczba()
            wynik *= a
        if komenda == "+":
            a = druga_liczba()
            wynik += a
        if komenda == "-":
            a = druga_liczba()
            wynik -= a
        if komenda == "/":
            a = druga_liczba()
            wynik /= a
        if komenda == "**":
            a = druga_liczba()
            wynik **= a
        print(f"obecny wynik to: {wynik}")
        if komenda == "c":
            wynik = float(input("podaj pierwsza liczbe dzialania "))
        

main()
            
        

