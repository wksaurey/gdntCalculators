import math

print('Profile Calculator by Kolter Saurey (March 2023)')
measurement = 1
while(True):
    print(f'\nMeasurement {measurement}')
    measurement = measurement + 1
    print('Length : ', end='')
    length = float(input())
    print('Parallelism : ', end='')
    parallelism = float(input())

    minPoint = round(length - (parallelism/2.0), 4)
    maxPoint = round(length + (parallelism/2.0), 4)
    profile = round(2.0 * max(float(abs(minPoint)), float(abs(maxPoint))),4)

    print(f'Profile: {profile} ({minPoint}/{maxPoint})')
    print()
