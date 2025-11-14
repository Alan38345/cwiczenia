import sys
from operation import operation
from question_mark import quest
from power import power
from differentop import op
from difpower import difpower


commands = [
    "addition",
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



result = ""
command = input('write a command (if you dont know any commands write "?" ')
if command in commands:
    if command == "?":
        quest()
    if command == 'multiplication':
        result = operation("*")
        print(f"the result is {result}")

    elif command == 'subtraction':
        result = operation("-")
        print(f"the result is {result}")

    elif command == 'addition':
        result = operation("+")
        print(f"the result is {result}")
    elif command == "division":
        result = operation("/")
        print(f"the result is {result}")
    elif command == "exponentiation":
        result = power()
        print(f"the result is {result}")
else:
    print('Something is wrong with the command')

answer = input('Do you want to continue(yes or not)? ')


while answer == "yes":
    secque = input("Do you want to continue with your result (yes) or you want to start again (no)")
    if secque =="yes":
        command = input('write a command (if you dont know any commands write "?" ')
        if command in commands:
            if command == "?":
                quest()
            if command == 'multiplication':
                result = op("*", result)
                print(f"the result is {result}")

            elif command == 'subtraction':
                result = op("-", result)
                print(f"the result is {result}")

            elif command == 'addition':
                result = op("+", result)
                print(f"the result is {result}")
            elif command == "division":
                result = op("/", result)
                print(f"the result is {result}")
            elif command == "exponentiation":
                result = difpower(result)
                print(f"the result is {result}")
        else:
            print('Something is wrong with the command')
    if secque == "not":
        command = input('write a command (if you dont know any commands write "?" ')
        if command in commands:
            if command == "?":
                quest()
            if command == 'multiplication':
                result = operation("*")
                print(f"the result is {result}")

            elif command == 'subtraction':
                result = operation("-")
                print(f"the result is {result}")

            elif command == 'addition':
                result = operation("+")
                print(f"the result is {result}")
            elif command == "division":
                result = operation("/")
                print(f"the result is {result}")
            elif command == "exponentiation":
                result = power()
                print(f"the result is {result}")
        else:
            print('Something is wrong with the command')
    answer = input('Do you want to continue(yes or not)? ')








input('Press enter to exit')

# zostało         exponentiation
#                 root extraction
#                 percentage calculation
#                 logarithms
#                 intersection point of two lines
#                 prime numbers
#                 gcd
#                 lcm
# asdf





