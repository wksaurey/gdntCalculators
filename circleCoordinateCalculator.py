import math

print('Circle Coordinate Calculator by Kolter Saurey (March 2023)')
again = 'y'
while(again == 'y'):
    print('Radius: ', end='')
    radius = float(input())
    print('Angle : ', end='')
    angle = float(input())

    x = round(radius * math.sin(math.radians(angle)), 4)
    y = round(radius * math.cos(math.radians(angle)), 4)

    print(f'x = {x}')
    print(f'y = {y}')
    while True:
        again = ""
        print('Again? (y/n): ', end='')
        again = input()
        if again == 'y' or again == 'n':
            break
    print()
