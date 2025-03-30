from math import ceil, sqrt


def is_prime(x: int):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    if x > 2:
        for i in range(3, ceil(sqrt(x)), 2):
            if x % i == 0:
                return False
        return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a  # b == 0 thì return a lun
# a = 0, b = 0 ==> KHÔNG TỒN TẠI GCD


for _ in range(int(input())):
    n = int(input())  # n != 0
    count = 0
    for i in range(n):
        if gcd(i, n) == 1:
            count += 1

    if is_prime(count):
        print('YES')
    else:
        print('NO')

