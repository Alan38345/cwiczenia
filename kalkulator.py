komenda = input('podaj komende ')

komendy =["dodawanie",
          "odejmowanie",
          "mnożenie",
          "dzielenie",
          "potęgowanie",
          "pierwiastkowanie",
          "liczenie procentów",
          "logarytmy",
          "wspólny punkt dwóch prostych",
          "liczby pierwsze",
          "nwd",
          "nww",
          "?"]






def dodawanie(a, b):
      suma = a+b
      return suma
def odejmowanie(a,b ):
      różnica = a-b
      return różnica
def dzielenie(a, b):
      iloraz = a/b
      return iloraz
def potegowanie(a, b):
    potega = a**b
    return potega

if komenda in komendy:
    if komenda == 'dodawanie':
      a = float(input('podaj pierwszy składnik  '))
      b = float(input('podaj drugi składnik  '))
      dodawanie(a, b)
      suma = dodawanie(a, b)
      print(f'twoj wynik to {suma}')
    elif komenda == 'mnożenie':
        obecnaliczba = 0
        ilosc = int(input('ile liczb chcesz pomnożyć przez siebie?  '))
        wynik = 1
        for y in range(ilosc):
            obecnaliczba += 1
            liczba = int(input(f'podaj liczbe numer {obecnaliczba} '))
            wynik *= liczba
        print(f'wynik twojego mnozenia to  {wynik}' )
    elif komenda == 'odejmowanie':
        a = float(input('podaj odjemną'))
        b = float(input('podaj odjemnik'))
        roznica = odejmowanie(a, b)
        print(f'wynikiem odejmowanie jest {roznica}')
    elif komenda == "?":
        print("""dodawanie
          odejmowanie
          mnożenie
          dzielenie
          potęgowanie
          pierwiastkowanie
          liczenie procentów
          logarytmy
          wspólny punkt dwóch prostych
          liczby pierwsze
          nwd
          nww""")
    else:
        print('cos slaba komenda')




input('nacisnij enter zeby zakonczyc')



