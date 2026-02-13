def multiplication(a):
    number = 1
    for x in (a+1):
        while True:
            try:
                number = float(input(f"write the {x+1}. number:"))
                break
            except ValueError:
                print("I was expecting a number!")



