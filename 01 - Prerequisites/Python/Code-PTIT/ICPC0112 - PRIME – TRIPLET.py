"""
Bộ ba số nguyên tố được gọi là Prime- Triplet
nếu nó là bộ ba số nguyên tố dưới dạng (p, p +2, p + 6) hoặc (p, p + 4, p+6),
trong đó p là một số nguyên tố.
Ví dụ các bộ ba số (5, 7, 11) hoặc (7, 11, 13) đều là các Prime-Triplet.
Cho số tự nhiên N, nhiệm vụ của bạn là đếm số các Prime-Triplet nhỏ hơn N.

Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤106;

Output:
Đưa ra kết quả mỗi test theo từng dòng.
"""
from math import ceil, sqrt

def primes_less_than(n):  # tìm primes < n
    if n <= 2:  # nếu < 2 thì không có primes
        return []
    else:
        is_prime = [True] * n
        # list * n ==> tạo n phần tử True bắt đầu từ 0 đến x - 1
        is_prime[0] = is_prime[1] = False  # số 0, 1 không phải là primes

        for i in range(2, ceil(sqrt(n))):
            if is_prime[i]:
                for j in range(i*i, n, i):  # thuật toán sieve of eratosthenes
                    is_prime[j] = False

        return [i for i in range(n) if is_prime[i]]


n_cases = int(input())
while n_cases > 0:
    n = int(input())

    primes = primes_less_than(n)  # trả về list chứa primes < n

    count = 0
    for i in range(len(primes)-2):
        p = primes[i]
        if p + 2 in primes and p + 6 in primes:
            count += 1
            #print(p, p+2, p+6)
        if p + 4 in primes and p + 6 in primes:
            count += 1
            #print(p, p+2, p+6)

    print(count)

    n_cases -= 1
