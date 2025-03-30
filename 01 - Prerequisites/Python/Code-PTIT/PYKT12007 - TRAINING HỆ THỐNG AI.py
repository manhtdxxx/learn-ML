'''
Một hệ thống nhận diện khuôn mặt gồm có N module.
Mỗi module có khả năng hoạt động chính xác bằng P[i].
Xác suất hoạt động chính xác của hệ thống = tích P của tất cả các module.
Để tăng P hệ thống, bạn phải thực hiện train dữ liệu cho mỗi module.
Tuy nhiên, việc này mất rất nhiều thời gian và bạn chỉ có tổng cộng U đơn vị thời gian.
Train một module trong X đơn vị thời gian, độ chính xác của module này tăng lên thêm X
Bạn hãy xác định xem sau khi training, độ chính xác lớn nhất mà hệ thống đạt được là bao nhiêu?

Input:
Dòng đầu tiên là số lượng bộ test T (1 ≤ T ≤ 100).
Mỗi test gồm số nguyên dương N (1 ≤ N ≤ 50).
Dòng tiếp theo là số thực U.
Dòng cuối gồm N số thực P[i] (0 ≤ P[i] ≤ 1).

Output:
Với mỗi test in ra trên một dòng đáp án tìm được với độ chính xác 10^-6.
'''


n_cases = int(input())

while n_cases > 0:
    len_P = int(input())
    U = float(input())
    P = map(float, input().split())  # 0 <= P[i] <= 1

    dict_P = {}  # chứa Probability: Count occurrences
    for i in P:
        dict_P.setdefault(i)
        # dict.setdefault(key [, value]) thêm key vào dict, nếu không cho value thì value = None
        if dict_P.get(i) is None:  # dict.get(key) là đọc value của key đó
            dict_P[i] = 1  # P[i] xuất hiện 1 lần
        else:
            dict_P[i] += 1  # nếu P[i] đã xuất hiện thì + thêm 1

    # sorted(dict.keys()) = sorted(dict) : sort theo key và chỉ hiện key trong list
    # sorted(dict.values()) : sort theo value và chỉ hiện value trong list
    # sorted(dict.items()) : sort theo key và hiện cặp tuple (key, value) trong list
    list_P = [[i, dict_P[i]] for i in sorted(dict_P)]  # sắp xếp P tăng dần

    while len(list_P) > 1:  # lặp tới khi list_P còn 1 cặp (key, value)
        P_difference = list_P[1][0] - list_P[0][0]  # P tăng lên
        training_U = P_difference  # train bao nhiêu thời gian sẽ tăng bấy nhiêu P
        sum_of_training_U = training_U * list_P[0][1]  # time to train 1 P * số lần xuất hiên P
        if U > sum_of_training_U:  # nếu còn dư time
            U -= sum_of_training_U  # time còn lại
            list_P[1][1] += list_P[0][1]
            # occurrences mới của P lớn hơn = occurrences cũ của P lớn hơn + occurrences của P nhỏ hơn
            list_P.pop(0)  # vì P nhỏ đã train thành P lớn hơn nên bỏ P nhỏ đi
        else:
            break

    # Khi U <= sum_of_training_U --> P nhỏ hơn != với P lớn hơn nên không gộp lại được
    # --> len() > 1 và lặp vô tận --> không bỏ trong while
    training_U = U / list_P[0][1]  # time to train each P = remaining U / số lần xuất hiện P
    P_difference = training_U  # time to train each P = xác xuất tăng lên for each P
    list_P[0][0] += P_difference
    U = 0

    # xác suất của hệ thống là :
    P_product = 1
    for i in list_P:
        P_product *= i[0]**i[1]
    print('{:6f}'.format(P_product))

    n_cases -= 1
