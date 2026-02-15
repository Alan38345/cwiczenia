liczby = [] 
inpt = input("podaj liczby do uporzadkowania oddzielone spacja ") 
for x in inpt.split(): liczby.append(int(x)) 
def merge_sort(liczby): 
    if len(liczby) <= 1: 
        return liczby
    srodek = len(liczby) // 2
    lewa = liczby[:srodek]
    prawa = liczby[srodek:]
    lewa = merge_sort(lewa)
    prawa = merge_sort(prawa)
    return merge(lewa, prawa)
def merge(lewa, prawa):
    result = [] 
    x = y = 0
    while x < len(lewa) and y < len(prawa):
        if lewa[x] < prawa[y]:
             result.append(lewa[x])
             x += 1
        else:
            result.append(prawa[y])
            y += 1
    resztax = lewa[x:]
    resztay = prawa[y:]
    for x in resztax:
        result.append(x)
    for y in resztay:
        result.append(y) 
    return result 
dupa = merge_sort(liczby)
print(dupa)