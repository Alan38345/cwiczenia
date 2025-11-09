import sys


commands = [
    "summing",
    "subtraction",
    "multiplication",
    "division",
    "exponentiation",
    "root extraction",
    "percentage calculation",
    "logarithms",
    "intersection point of two lines",
    "prime numbers",
    "gcd",
    "lcm",
    "?"
]


def summing(a, b):
    total = a + b
    return total
def subtraction(a, b):
    difference = a - b
    return difference
def division(a, b):
    quotient = a / b
    return quotient
def exponentiation(a, b):
    power = a ** b
    return power
answer = 'yes'

while answer == 'yes':
    command = input('write a command (if you dont know any commands write "?" ')
    if command in commands:

        if command == "?":
            print("""
                addition
                subtraction
                multiplication
                division
                exponentiation
                root extraction
                percentage calculation
                logarithms
                intersection point of two lines
                prime numbers
                gcd
                lcm""")
        if command == 'summing':
            a = float(input('Provide the first addend: '))
            b = float(input('Provide the second addend: '))
            summing(a, b)
            summing = summing(a, b)
            print(f'Your result is {summing}')
        elif command == 'multiplication':
            current_number = 0
            amount = int(input('How many numbers do you want to multiply? '))
            result = 1
            for y in range(amount):
                current_number += 1
                number = int(input(f'Enter number {current_number}: '))
                result *= number
            print(f'Your multiplication result is {result}')
        elif command == 'subtraction':
            a = float(input('Enter the minuend: '))
            b = float(input('Enter the subtrahend: '))
            difference = subtraction(a, b)
            print(f'The result of subtraction is {difference}')

        elif command == "division":
            divisor = float(input('Enter the divisor: '))
            amount = int(input('Enter how many numbers you want to divide by this number: '))
            z = 0
            for x in range(1, amount+1):
                z += 1
                y = float(input(f'write a {z}. number that you want to devide by '))
                if y==0:

                    sys.exit("nawet nie probuj gagatku")
                    divisor /= y
                    print(f'The result of the division is: {divisor}')
    else:
        print('Something is wrong with the command')
    answer = ''
    answer = input('Do you want to continue? ')

input('Press enter to exit')




