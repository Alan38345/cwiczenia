while True:
    try:
        value = float(input("Write a number: "))
        break  # jeśli się uda → przerywamy pętlę
    except ValueError:
        print("Error: please write a valid number!")
print(value)