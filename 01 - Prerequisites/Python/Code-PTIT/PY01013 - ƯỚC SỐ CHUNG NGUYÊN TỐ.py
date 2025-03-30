from math import sqrt


def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(x: int):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:  # chia cho số chẵn
        return False
    if x > 2:
        for i in range(3, int(sqrt(x) + 1), 2):  # chia cho số lẻ
            if x % i == 0:
                return False
        return True


for _ in range(int(input())):
    x, y = map(int, input().split())
    ucln = gcd(x, y)

    sum_digits = 0
    for i in str(ucln):
        sum_digits += int(i)

    if is_prime(sum_digits):
        print('YES')
    else:
        print('NO')

