def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for _ in range(int(input())):
    x = int(input())
    reversed_x = int(str(x)[::-1])
    ucln = gcd(x, reversed_x)

    if ucln == 1:
        print('YES')
    else:
        print('NO')

