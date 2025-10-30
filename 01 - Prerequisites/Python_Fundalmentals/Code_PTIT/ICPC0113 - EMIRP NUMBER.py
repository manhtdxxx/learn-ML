"""
Một số nguyên dương K được gọi là Emirp Number nếu K là số nguyên tố,
đảo các chữ số của K cũng là một số nguyên tố nhưng không phải chính nó (không đối xứng).
Ví dụ số 11 không phải là số Emirp Number.
Cho số tự nhiên N, bạn hãy liệt kê tất cả các số Emirp Number nhỏ hơn N.

Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤106;

Output:
Đưa ra kết quả mỗi test theo từng dòng.
Chú ý: ghi theo các cặp số thỏa mãn từ nhỏ đến lớn, xem ví dụ để hiểu hơn về cách hiển thị kết quả.
"""

from math import ceil, sqrt

def primes_less_than(n):  # tìm primes < n
    if n <= 2:
        return []
    else:
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = 0
        for i in range(2, ceil(sqrt(n))):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False

        return [i for i in range(len(is_prime)) if is_prime[i]]


n_cases = int(input())
while n_cases > 0:
    n = int(input())

    primes = primes_less_than(n)
    primes = list(map(str, primes))

    x = []
    for i in primes:
        reversed_i = i[::-1]
        if reversed_i in primes and i != reversed_i and i not in x:  # tránh lặp
            x.append(i)
            x.append(reversed_i)

    x = ' '.join(x)
    print(x)

    n_cases -= 1
