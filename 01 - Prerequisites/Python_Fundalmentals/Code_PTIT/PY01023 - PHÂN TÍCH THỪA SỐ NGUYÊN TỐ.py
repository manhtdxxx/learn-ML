from math import sqrt, ceil


for _ in range(int(input())):
    x = int(input())

    print(1, end=' ')

    i = 2
    # có thể dùng for i in range(2, int(sqrt(x)) + 1):
    # dùng while thì chỉnh được thêm x
    while i <= ceil(sqrt(x)):  # phải có =, k tin thì tính trong TH x == 9 nhé!!!
        count = 0
        # đếm số lần i là thừa số của x --> x = i^count * ...
        while x % i == 0:
            count += 1
            x //= i

        if count > 0:
            print('* ' + str(i) + '^' + str(count), end=' ')

        i += 1

    # khi x còn lại không thể chia hết cho i trong vòng lặp while
    # --> x còn lại là thừa số còn lại ^1
    if x > 1:
        print('* ' + str(x) + '^' + str(1), end='')
        # thêm end vì mặc định end là \n + thêm lệnh print() sẽ thừa 1 blank

    print()  # thêm vì có end ở print trong vòng for, cần xuống dòng để nhập input
