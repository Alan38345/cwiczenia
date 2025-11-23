def addition(a):
    number = 0
    for x in range(a):
        while True:
            try:
                addend = float(input(f"write the {x+1}. addend: "))
                break
            except ValueError:
                print("you had to write a number")
        number += addend
    return number
