"""
Cho dãy số A[] gồm có N phần tử.

Tổng tuyệt đối của một DÃY SỐ là giá trị tuyệt đối của tổng tất cả các phần tử
(tính tổng xong mới lấy giá trị tuyệt đối).

Độ yếu của dãy số A[] = GTLN trong các tổng tuyệt đối của các dãy con liên tiếp của A.
(Dãy chứa các số liền kề nhau mà có tổng tuyệt đối lớn nhất)

Xác định số thực X sao cho dãy số A[1]-X, A[2]-X, …, A[N]-X có độ yếu là nhỏ nhất.
(Độ yếu min <=> Độ yếu = Tổng tuyệt đối lớn nhất)

Input:
Dòng đầu tiên gồm số nguyên N (1 ≤ N ≤ 100 000).
Dòng tiếp theo gồm N số nguyên A[i] (-10 000 ≤ A[i] ≤ 10 000).

Output:
In ra số độ yếu của dãy A[1]-X, A[2]-X, …, A[N] - X.
Kết quả ghi ra với 6 chữ số phần thập phân
"""


def weakness(a: list, x):
    # tổng là số dương lớn nhất và tổng là số âm nhỏ nhất
    max_positive_sum, min_negative_sum = 0, 0
    # lưu trữ tổng là số dương, tổng là số âm tạm thời để so sánh với 2 max, min
    current_positive_sum, current_negative_sum = 0, 0

    list_b = []
    for i in a:
        b_i = i - x
        list_b.append(b_i)

        if b_i > 0:
            current_positive_sum += b_i  # để tổng dương lớn nhất thì chỉ nên + với b dương
            current_negative_sum = 0
            # tổng là số âm + với b dương sẽ không đạt min thì nên reset về 0
            if current_positive_sum > max_positive_sum:
                max_positive_sum = current_positive_sum

        elif b_i < 0:
            current_negative_sum += b_i  # để tổng âm nhỏ nhất thì chỉ nên + với b âm
            current_positive_sum = 0
            # tổng là số dương + với b âm sẽ không đạt max thì nên bỏ để reset
            if current_negative_sum < min_negative_sum:
                min_negative_sum = current_negative_sum

        else:
            current_positive_sum += b_i
            current_negative_sum += b_i

    return round(max_positive_sum, 6), round(-min_negative_sum, 6), list_b


# weakness min <=> weakness = max_positive_sum = - min_negative_sum
# ---ĐỀ GỢI Ý VẬY---
n = int(input())
list_a = list(map(int, input().split()))

# x phải nằm trong kha min(a) và max(a)
# nếu x > max(a) thì a sẽ chứa toàn số âm ==> tổng âm > tổng dương (=0)
# nếu x < min(a) thì a sẽ chứa toàn số dương ==> tông dương > tổng âm (=0)
low_x, high_x = min(list_a), max(list_a)

# Binary Search to find x
max_positive_sum, abs_min_negative_sum = 1, 0  # để chạy while

while max_positive_sum != abs_min_negative_sum:

    middle_x = (low_x + high_x) / 2
    x = middle_x
    max_positive_sum, abs_min_negative_sum, list_b = weakness(list_a, x)

    if max_positive_sum > abs_min_negative_sum:
        # tổng âm phải tăng ==> X phải lớn hơn vì A[i] - X thì sẽ số âm xuất hiện nhiều hơn
        low_x = x
        # low_x tăng --> X tăng (X dịch phải)
    else:
        # tổng dương phải tăng ==> X phải nhỏ hơn
        high_x = x
        # high_x giảm --> X giảm (X dịch trái)


# x != độ yếu nhé!!!
print('{:.6f}'.format(max_positive_sum))
for i in list_b:
    print(i, end=' ')