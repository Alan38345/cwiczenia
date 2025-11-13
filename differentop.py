def op(a, b):
    amount = int(input("How many numbers does your action have? "))
    for x in range(amount):
        numbers = float(input(f"Write the {x+1}. number: "))
        result = b
        if a == '*':
            result *= numbers

        elif a == '+':
            result += numbers

        elif a == '**':
            result **= numbers

        elif a == '/':
            if numbers == 0:
                print("pamietaj nie dziel przez zero")
            result /= numbers

        elif a == '-':
            result /= numbers

    return result