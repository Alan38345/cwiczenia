import random

slowa = [
"rower",
"serce",
"miska",
"maska",
"lalka",
"fotel",
"radio",
"banan",
"mango",
"cyfra",
"kamyk",
"kotek",
"pióro",
"zegar",
"wózek",
"plaża",
"rzeka",
"burza",
"śnieg",
"wiatr",
"iskra",
"lampa",
"dymek",
"ogień",
"kwiat",
"krzak",
"drzew",
"skała",
"mleko",
"cukru",
"serek",
"słowo",
"obraz",
"klucz",
"pilot",
"model",
"panel",
"ramka",
"belka",
"kubek",
"garnek",
"koszt",
"wynik",
"zakup",
"praca",
"zabór",
"torba",
"szafa",
"biurko"
]
def sprawdz(litery, wlotana, wynik):
    for x in range(5):
        if litery[x] == wlotana:
            wynik.append(f"({wlotana})")
            return wynik
    wynik.append("x")
    return wynik

def losowanie(slowa):
    pick = "dupa"
    while len(pick) != 5:
        pick = random.choice(slowa)
    return pick

def main():
    pick = "dupa"
    wlot = "elo"
    y = 0
    pick = losowanie(slowa)
    litery = list(str(pick))
    while y <= 5:
        wynik = []
        wlot = list(input("podaj 5 literowo slowe ktore zgadujesz: "))
        if pick == "".join(wlot):
            print("zgadles gg")
            quit()
        if "".join(wlot) == "2137":
            print(pick)
            quit()
        for x in range(5):
            if litery[x] == wlot[x]:
                wynik.append(litery[x])
            else:
                sprawdz(litery, wlot[x], wynik)
                
        y +=1
        print(wynik)
    print(pick)
main()
