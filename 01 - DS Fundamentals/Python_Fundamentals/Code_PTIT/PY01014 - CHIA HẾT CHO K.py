"""
Cho ba số nguyên dương a, K, N.
Hãy liệt kê tất cả các số nguyên dương b thỏa mãn cả hai điều kiện:
    a + b ≤ N  ==>  b ≤ N - a
    a + b chia hết cho K
"""
a, K, N = map(int, input().split())


start_b = K - a % K
'''
a = m.K + r
MUỐN a chia hết cho K thì r phải thêm một lượng là b để r == số chia của K
==> a + b = m.K + (r + b)
<=> a + b = m.K + K

==> b = K - r
'''
list_b = []
for b in range(start_b, N - a + 1, K):
    # step = K --> b = 2K - r, 3K - r, 4K - r, ...
    list_b.append(b)


if len(list_b) == 0:
    print(-1)


list_b = map(str, list_b)
print(' '.join(list_b))