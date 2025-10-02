class Czlowiek:
    def __init__(self, imie):
        self.imie = imie  # <-- Zapisujemy imię w obiekcie

adam = Czlowiek("Adam")
print(adam.imie)  # wynik: Adam


class Osoba:                           # Tworzymy klasę "Osoba"
    def __init__(self, imie, wiek):    # Konstruktor: tworzy nową osobę
        self.imie = imie               # Zapisuje imię w obiekcie
        self.wiek = wiek               # Zapisuje wiek w obiekcie

    def przedstaw_sie(self):           # Metoda, która przedstawia osobę
        print(f"Cześć! Mam na imię {self.imie} i mam {self.wiek} lat.")


class User:
    def __init__(self, name, age):
        self.imie = name
        self.wiek = age
        print("konstrukcja")



def greet_user(a):
    print(f"hi there {a.imie} you are {a.wiek}")
    print('welcome aboard')


michal = User("michal", 25)
maciek = User("maciek", 28)
greet_user(michal)

