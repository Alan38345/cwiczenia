
dzialanie = input('wcisnij pytajnik by dowiedziec sie jakie sa komendy? ')
if dzialanie == '?':
    print("""O to komendy
          dodawanie
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
    print('nie kojarze tej komendy')


def dodawanie(a, b):
      suma = a+b
      return suma
def mnożenie(a, b):
      iloczyn = a*b
      return iloczyn
def odejmowanie(a,b ):
      różnica = a-b
      return różnica
def dzielenie(a, b):
      iloraz = a/b
      return iloraz
def potegowanie(a, b):
    liczba = 1
    for x in range(b):
        liczba *= a
    return liczba




komenda = input('podaj komende  ')
if komenda == 'dodawanie':
      a = float(input('pierwsza liczba  '))
      b = float(input('druga liczba  '))
      dodawanie(a, b)
      suma = dodawanie(a, b)
      print(suma)


