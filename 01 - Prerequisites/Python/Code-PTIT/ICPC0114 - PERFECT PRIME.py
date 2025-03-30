"""
Một số nguyên dương N được gọi là Perfect Prime nếu N là số nguyên tố;
đảo ngược các chữ số của N cũng là một số nguyên tố;
tổng các chữ số của N là một số nguyên tố và mỗi chữ số của N cũng là một số nguyên tố.
Cho số nguyên dương N, hãy kiểm tra N có phải là Perfect Prime hay không?
Đưa ra “Yes” nếu N là Perfect Prime, ngược lại đưa ra “No”.

Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤107;

Output:
Đưa ra kết quả mỗi test theo từng dòng.
"""

from math import sqrt, ceil

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
                # if return is executed, it will break the loop,
                # and no subsequent code in the function will be executed
        return True


def are_all_prime_digits(x: int):
    prime_digits = [2, 3, 5, 7]
    for i in str(x):
        if int(i) not in prime_digits:
            return False
    return True


n_cases = int(input())
while n_cases > 0:
    x = int(input())

    reversed_x = int(str(x)[::-1])

    sum_digits = 0
    for i in str(x):
        sum_digits += int(i)

    #
    if is_prime(x) and is_prime(reversed_x) and is_prime(sum_digits) and are_all_prime_digits(x):
        print('Yes')
    else:
        print('No')

    n_cases -= 1
