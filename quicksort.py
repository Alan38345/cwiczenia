liczby = [6, 7, 2, 3, 5, 1, 8, 9, 0]
dlugosc = len(liczby)-1
for x in range(dlugosc):
    pivot = liczby[x]
    y = 0
    z = 0
    while True:
        while liczby[y] <= pivot and y < dlugosc and liczby[dlugosc-z] > pivot and z < dlugosc:
            y += 1
            z +=1
        if liczby[y] <= pivot:
            dupa = liczby[x]
            del.liczby[x]
            liczby.append(dupa)
        if z+y >= dlugosc+2:
            liczby[x], liczby[y] = liczby[y], liczby[x]
            break

        else:
            liczby[z], liczby[y] = liczby[y], liczby[z]
print(liczby)
        




