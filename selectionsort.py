liczby = [2, 3, 5, 6, 7, 4, 3, 2, 3] 
def najmnj_liczba(a): 
    result = a[0]
    for x in range(len(a)): 
        if a[x] <= result:
            result = a[x] 
    return result 
        
def selection(a):
    result = []
    dlugosc = len(a)
    while a:
        najmn = najmnj_liczba(a) 
        result.append(najmn)
        a.remove(najmn) 
    return result 
print(selection(liczby))