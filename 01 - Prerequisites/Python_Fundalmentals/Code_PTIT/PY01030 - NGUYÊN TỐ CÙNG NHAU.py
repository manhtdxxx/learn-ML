"""
Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau
nếu a và b có ước chung lớn nhất bằng 1.

Cho hai số nguyên dương N và K trong đó 10 < N < 10000; 1 < K < 6.

Hãy liệt kê các số có K chữ số thỏa mãn nguyên tố cùng nhau với N.
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


n, k = map(int, input().split())
min_num = 10 ** (k-1)
max_num = 10 ** k

count = 0
for i in range(min_num, max_num):
    if gcd(n, i) == 1:
        count += 1
        print(i, end=' ')
        if count == 10:
            print()
            count = 0






