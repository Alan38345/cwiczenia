import random
def main():
    x = 0
    a = random.randint(1,100)
    liczba = 0
    while a != liczba and x <= 10:
        liczba = int(input("podal liczbe ktora obstawiasz"))
        if liczba > a:
            print("nizej")
        elif liczba == a:
            print("zgadles")
        else:
            print("wyzej")
        x +=1
    if x >= 11:
        print("przegrales moze kolejnym razem")
main()