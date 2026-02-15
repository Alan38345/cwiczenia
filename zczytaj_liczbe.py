def zczytanie():
    while True:
        x = input("podaj liczbe")
        try:
            liczba = float(x)
            break
        except ValueError:
            print("to nie jest liczba")
    
    while True:
        y = input("podaj liczbe")
        try:
            liczba = float(y)
            break
        except ValueError:
            print("to nie jest liczba")
    return x,y
        

    
