import math

print('Position Calculator by Kolter Saurey (March 2023)')
measurement = 1
while(True):
    print(f'\nMeasurement {measurement}')
    measurement = measurement + 1
    print('X : ', end='')
    x = float(input())
    print('Y : ', end='')
    y = float(input())

    position = round(2.0 * math.sqrt((x**2.0) + (y**2.0)), 4);

    print(f'Position: {position}')
    print()
