from math import sqrt


def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


l, r = map(int, input().split())
for i in range(l, r + 1):
    for j in range(i + 1, r + 1):
        if gcd(i, j) == 1:
            for z in range(j + 1, r + 1):
                if gcd(i, z) == 1 and gcd(j, z) == 1:
                    print('({}, {}, {})'.format(i, j, z))