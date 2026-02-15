liczby = []
tekst = input("podaj liczby oddzielone spacja")
for x in tekst.split():
    liczby.append(int(x))
n = len(liczby)
for y in range(n-1):
    for x in range(n-1):
        if liczby[x]>liczby[x+1]:
            liczby[x], liczby[x+1] = liczby[x+1], liczby[x]
print(liczby) 