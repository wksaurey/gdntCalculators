import math

print('Circle Coordinate Calculator by Kolter Saurey (March 2023)')
measurement = 1
while(True):
    print(f'\nMeasrement {measurement}')
    measurement = measurement + 1
    print('Radius: ', end='')
    radius = float(input())
    print('Angle : ', end='')
    angle = float(input())

    x = round(radius * math.sin(math.radians(angle)), 4)
    y = round(radius * math.cos(math.radians(angle)), 4)

    print(f'x = {x}')
    print(f'y = {y}')
    print()
