
while True:
    komenda = input().lower()
    if komenda == 'start':
            print('car start driving')
    elif komenda == 'stop':
            print('car stop driving')
    elif komenda == 'quit':
        print('koniec gierki')
        break
    elif komenda == 'help':
            print('start - to start the car')
            print('stop - to stop the car')
            print('quit - to exit')
    elif komenda == 'start' and komenda2 == 'start':
        print('bro you have just started the car')
    elif komenda == 'stop' and komenda2 == 'stop':
        print('you have already stopped the car')
    else:
        print('i dont understand this command')
    komenda2 = input().lower()
    if komenda == 'start' and komenda2 == 'start':
            print('bro you have already started this car')
    elif komenda == 'stop' and komenda2 == 'stop':
            print('bro you have just stopped the car ')
    elif komenda2 == 'help':
            print('start - to start the car')
            print('stop - to stop the car')
            print('quit - to exit')
    elif komenda2 == 'start':
            print('car start driving')
    elif komenda2 == 'stop':
            print('car stop driving')
    elif komenda2 == 'quit':
        break

    else:
        print('nie rozumiiem tej komendy')



