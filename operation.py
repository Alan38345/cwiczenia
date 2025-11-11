def operation(a):
    amount = int(input("How many numbers does your action have?"))
    result = float(input("what is your first number of the operation? "))
    for x in range(amount):
        numbers = float(input(f"Write the {x+1}. number"))
        if a == '*':
            result *= numbers

        elif a == '+':
            result += numbers

        elif a == '**':
            result **= numbers

        elif a == '/':
            result /= numbers

        elif a == '-':
            result /= numbers

    return result
wynik = operation(input("jakie dzialanie chcesz wykonac"))
print(wynik)

