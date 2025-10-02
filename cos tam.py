a = int(input("wypisz a fukcji kwadratowej w postaci ogólnej:"))
b = int(input("wypisz b fukcji kwadratowej w postaci ogólnej:"))
c = int(input("wypisz c fukcji kwadratowej w postaci ogólnej:"))
if a == 0:
    print("to nie jest fukcja kwadratowa")
delta = b*b-(4*a*c)
pierw = float(delta**0.5)
x1 = (-b-pierw)/2
x2 = (-b+pierw)/2
print(f"miejscami zerowymi funkcji są:{x1}, {x2}")
