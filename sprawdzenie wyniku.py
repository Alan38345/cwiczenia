def sprawdzenie_wyniku(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0 and a != 0:
        pierwiastek = int(delta ** 0.5)
        x1 = round((-b - pierwiastek) / (2 * a),2)
        x2 = round((-b + pierwiastek) / (2 * a),2)
        return sorted([x1, x2])
    elif delta == 0 and a != 0:
        pierwiastek = int(delta ** 0.5)
        x0 = -b / (2 * a)
        return[x0]
    else:
        return[]

testy = [
    (1, -3, 2, [1.0, 2.0]),
    (1, 2, 1, [-1.0]),
    (1, 0, 1, []),
    (2, -7, 3, [0.5, 3.0]),
    (0, 2, 1, [])
]
for test in testy:
    a, b, c, oczekiwany = test
    wynik = sprawdzenie_wyniku(a, b, c)
    if wynik == oczekiwany:
        print('test dobrze poszedl')
    else:
        print('zle wyszedl test')