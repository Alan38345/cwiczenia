help = input()
if help == 'help':
    print('start - to start the car')
    print('stop - to stop the car')
    print('quit - to exit')
else:
    print('i dont understand the command')
komenda = input()

if komenda == 'start':
    print('car start driving')
elif komenda == 'stop':
    print('car stop driving')
else:
    print('sorry i dont understand this command')

while True:
    komenda2 = input()
    if komenda2 == 'start':
            print('car start driving')
    elif komenda2 == 'stop':
            print('car stop driving')
    elif komenda2 == 'exit':
        print('koniec gierki')
        break
    else:
        print('nie rozumiiem tej komendy')


