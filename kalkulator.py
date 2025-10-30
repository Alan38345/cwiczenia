
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
      a = float(input('podaj pierwszy składnik  '))
      b = float(input('podaj drugi składnik  '))
      dodawanie(a, b)
      suma = dodawanie(a, b)
      print(f'twoj wynik to {suma}')
elif komenda == 'mnożenie':
    a = float(input('podaj pierwszy czynnik  '))
    b = float(input('podaj drugi czynnik '))
    iloczyn = mnożenie(a, b)
    odp = float(input('jesli chcesz podac jeszcze kolejny czynnik wcisnij 1 jesli nie wcisnij 2 '))
    if odp == 1:
        c = float(input('podaj trzeci skladnik '))
        iloczyn *= c
        odp2 = float(input('jesli chcesz podac jeszcze kolejny czynnik wcisnij 1 jesli nie wcisnij 2 '))
        if odp2 == 1:
            d = float(input('podaj czwarta liczbe '))
            iloczyn *= d
            odp3 = float(input('ostatni raz mozesz dodac jeszcze jednen czynnik jesli chcesz to uczynic kliknij 1 jesli nie 2 '))
            if odp3 == 1:
                e = float(input('podaj ostatni czynnik '))
                iloczyn *= e
                print('mozesz dodac maksymalnie 5 czynnikow, więc: ')
    iloczyn = int(iloczyn)
    print(f'wynik twojego mnozenia to  {iloczyn}' )





input('nacisnij enter zeby zakonczyc')


