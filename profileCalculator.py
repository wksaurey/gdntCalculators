import math

print('Profile Calculator by Kolter Saurey (March 2023)')
again = 'y'
while(again == 'y'):
    print('Length : ', end='')
    length = float(input())
    print('Parallelism : ', end='')
    parallelism = float(input())

    minPoint = round(length - (parallelism/2.0), 4)
    maxPoint = round(length + (parallelism/2.0), 4)
    profile = round(2.0 * max(float(abs(minPoint)), float(abs(maxPoint))),4)

    print(f'Profile: {profile} ({minPoint}/{maxPoint})')
    while True:
        again = ""
        print('Again? (y/n): ', end='')
        again = input()
        if again == 'y' or again == 'n':
            break
    print()
