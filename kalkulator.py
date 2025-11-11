import sys
from operation import operation
from question_mark import quest
from structure import structure


commands = [
    "addition",
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



answer = 'yes'
secque = 'no'

while True:
    if answer == 'yes' and secque == 'no':
        result = ""
        command = input('write a command (if you dont know any commands write "?" ')
        if command in commands:
            if command == "?":
                quest()
            if command == 'multiplication':
               structure("*")

            elif command == 'subtraction':
                a = int(input("how many numbers do you want to substract from another?"))
                result = float(input("enter the minuend"))
                for x in range(a):
                    c = float(input(f"write the {x+1}. subtrahend"))
                    result -= c


                print(f'The result of subtraction is {result}')
            elif command == 'addition':
                a = int(input('how many numbers do you want to add together? '))
                result = float(input('write the 1. number '))
                for x in range(1, a):
                    c = float(input(f'write the {x+1}. number '))
                    result += c
                print(f'the result is {result} ')
            elif command == "division":
                amount = int(input('Enter how many numbers you want to divide by this number: '))
                result = float(input('Enter the divisor: '))
                z = 0
                for x in range(1, amount+1):
                    z += 1
                    y = float(input(f'write a {z}. number that you want to devide by '))
                    if y==0:
                        sys.exit("nawet nie probuj gagatku")
                    result /= y
                    print(f'The result of the division is: {result}')

            elif command == "exponentiation":
                result = float(input("Write a base"))
                b = float(input("write a power"))
                result **= b
                print(f"the result is:{result}")
        else:
            print('Something is wrong with the command')
    answer = ''
    secque = ''
    answer = input('Do you want to continue(yes or not)? ')
    if answer == "yes":
        secque = input("Do you want to continue with your result (yes) or you want to start again (no)")
    if secque =="yes":
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

            if command == 'multiplication':
                current_number = 0
                amount = int(input('How many numbers do you want to multiply this number? '))
                for y in range(amount):
                    current_number += 1
                    number = int(input(f'Enter number {current_number}: '))
                    result *= number
                print(f'Your multiplication result is {result}')
            elif command == 'subtraction':
                a = int(input("How many numbers you want to substract? "))
                current_number = 0
                for x in range(1, a):
                    current_number += 1
                    b = float(f"write the {current_number}. number you want to substract ")
                    result -= b
                print(f'The result of subtraction is {result}')
            elif command == 'addition':
                a = int(input('how many numbers do you want to add together? '))
                for x in range(1, a):
                    c = float(input(f'write the {x + 1}. number '))
                    result += c
                print(f'the result is {result} ')
            elif command == "division":
                amount = int(input('Enter how many numbers you want to divide by this number: '))
                z = 0
                for x in range(1, amount + 1):
                    z += 1
                    y = float(input(f'write a {z}. number that you want to devide by '))
                    result /= y
                    if y == 0:
                        sys.exit("nawet nie probuj gagatku")
                    print(f'The result of the division is: {result}')
            elif command == "exponentiation":
                a = float(input("Write a base"))
                b = float(input("write a power"))
                result = exponentiation(a, b)
                print(f"the result is:{result}")
        else:
            print('Something is wrong with the command')




input('Press enter to exit')

# zostało         exponentiation
#                 root extraction
#                 percentage calculation
#                 logarithms
#                 intersection point of two lines
#                 prime numbers
#                 gcd
#                 lcm





