"""
Cho số nguyên dương N, hãy liệt kê
các số thuận nghịch nhỏ hơn N thỏa mãn điều kiện:
    Chỉ có các chữ số 0,2,4,6,8
    Số chữ số của N chia cho 2 dư 1

Input
Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)

Output
Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.
"""


def is_even(x: int):
    for i in str(x):
        if int(i) % 2 == 1:
            return False
    return True


palindromes = []
# chỉ có các chữ số 0,2,4,6,8 ==> min == 2 và max == 888
num = 2
while num <= 888:
    if is_even(num):
        palindromes.append(int(str(num) + str(num)[::-1]))  # tạo số thuận nghịch
        # 22 < num < 10**6 ==> max == 888.888
    num += 2

for _ in range(int(input())):
    n = int(input())

    for i in palindromes:
        if i >= n:
            break
        print(i, end=' ')

    print()
