def bubble_sort(tablica):
    n = len(tablica)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    return tablica


# przykład użycia
liczby = [5, 2, 9, 1, 5, 6]
print(bubble_sort(liczby))
