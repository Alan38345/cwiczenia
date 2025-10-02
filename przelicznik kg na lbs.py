weight = int(input("Ile ważysz"))
jednostka = input("kilogramy(kg) czy (lbs)")
if jednostka == "kg":
    waga = weight * 2.2
elif    jednostka == "lbs":
    waga = weight * 0.46
print(f"twoja waga to {waga}{jednostka}")