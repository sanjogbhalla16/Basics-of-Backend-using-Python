import math


def circumference(r):
    return 2 * math.pi * r


def area(r):
    return 2 * math.pi * (r**2)


print(round(circumference(2), 2))
print(round(area(2), 2))
