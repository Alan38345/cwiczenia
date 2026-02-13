ksiazka_telefoniczna = []

def wypisanie_listy():
    for x in range(len(ksiazka_telefoniczna)):
        print(x)
        print(f"imię:{ksiazka_telefoniczna[x]["imie"]}")
        print(f"nazwisko:{ksiazka_telefoniczna[x]["nazwisko"]}")
        print(f"numer telefonu:{ksiazka_telefoniczna[x]["numer"]}")
        print(f"email:{ksiazka_telefoniczna[x]["email"]}")
        print("")
def wypisywanie_jednej_osoby(x):
        print("")
        print(f"imię:{ksiazka_telefoniczna[x]["imie"]}")
        print(f"nazwisko:{ksiazka_telefoniczna[x]["nazwisko"]}")
        print(f"numer telefonu:{ksiazka_telefoniczna[x]["numer"]}")
        print(f"email:{ksiazka_telefoniczna[x]["email"]}")

def dodawanie():
    imie = input("podaj imie osoby ktorą chcesz dodac: ")
    nazwisko = input("podaj nazwisko osoby ktorą chcesz dodac: ")
    numer = input("podaj numer telefonu osoby ktorą chcesz dodac: ")
    email = input("podaj email osoby ktorą chcesz dodac: ")
    dodany_element ={"imie": imie, "nazwisko": nazwisko, "numer": numer, "email": email}
    ksiazka_telefoniczna.append(dodany_element)


def main():
    while True:
        dzialanie = input("co chcesz zrobic?")
        if dzialanie == "dodawanie":
           dodawanie()
        if dzialanie == "wypisywanie":
            wypisanie_listy()
        if dzialanie == "usuwanie":
            usuwanie_kontaktu()
        if dzialanie == "szukanie":
            szukanie_kontaktu()
        if dzialanie == "edycja":
            edycja_elementu()

def usuwanie_kontaktu():
    numer = int(input("Podaj numer kontaktu który chcesz usunąć: "))-1
    ksiazka_telefoniczna.pop(numer)
def szukanie_kontaktu():
    dana = ["imie", "nazwisko", "numer", "email"]
    skrut = input("napisz skrrut")
    for x  in range(len(ksiazka_telefoniczna)):
        for y in dana:
            if ksiazka_telefoniczna[x][y] == skrut:
                wypisywanie_jednej_osoby(x)
def edycja_elementu():
    osoba = int(input("napisz mi indeks osoby ktorej chcesz zedytowac dane:")-1)
    kontakt = ksiazka_telefoniczna[osoba]
    dozmiany = input("naisz którą daną o tej osobie chcesz zmienic:")
    if dozmiany == "imię":
        korekcja = input("na jakie imie chcesz zmienic")
        kontakt["imię"] = korekcja
    if dozmiany == "nazwisko":
        korekcja = input("na jakie nazwisko chcesz zmienic")
        kontakt["nazwisko"] = korekcja
    if dozmiany == "numer":
        korekcja = input("na jaki numer telefonu chcesz zmienic")
        kontakt["numer"] = korekcja
    if dozmiany == "email":
        korekcja = input("na jaki adres email chcesz zmienic")
        kontakt["email"] = korekcja





main()








