import math

print('Position Calculator by Kolter Saurey (March 2023)')
again = 'y'
while(again == 'y'):
    print('X : ', end='')
    x = float(input())
    print('Y : ', end='')
    y = float(input())

    position = round(2.0 * math.sqrt((x**2.0) + (y**2.0)), 4);

    print(f'Position: {position}')
    while True:
        again = ""
        print('Again? (y/n): ', end='')
        again = input()
        if again == 'y' or again == 'n':
            break
    print()
