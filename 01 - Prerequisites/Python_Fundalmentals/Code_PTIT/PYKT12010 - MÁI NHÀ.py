"""
Cho dãy số A[] gồm có N phần tử.
Bạn được phép tăng, giảm một phần tử mỗi lần 1 đơn vị.
Nhiệm vụ của bạn là hãy sử dụng ít bước nhất có thể để
chuyển dãy số đã cho về dạng dãy số ‘mái nhà’, với các tính chất sau :

Một phần tử lớn nhất là đỉnh (giả sử là phần tử thứ i)
Các phần tử bên trái và bên phải giảm dần đi 1 đơn vị, tức là với mọi j, A[j] = A[i] - |i-j|
Tất cả các phần tử A[j] đều phải lớn hơn 0.

Input:
Dòng đầu tiên là số nguyên N (N ≤ 5000).
Dòng tiếp theo gồm N phần tử của dãy số (1 ≤ A[i] ≤ 5000).

Output:
In ra số bước ít nhất để có thể hoàn thành bài toán trên.
"""


n = int(input())
x = list(map(int, input().split()))

costs = []
roofTops = []
for i in range(len(x)):
    peak_val = x[i]
    preceding_vals = []
    following_vals = []
    # fill numbers before peak value
    step1 = 1
    for j in range(i):
        val1 = peak_val - step1
        if val1 > 0:
            preceding_vals.append(val1)
            step1 += 1
        else:
            break

    # fill numbers after peak value
    # đặt if vì nếu th trên break thì th dưới cx k cần thực hiện
    if i == len(preceding_vals):
        step2 = 1
        for k in range(i+1, len(x)):
            val2 = peak_val - step2
            if val2 > 0:
                following_vals.append(val2)
                step2 += 1
            else:
                break

    # rooftop y
    preceding_vals.reverse()
    preceding_vals.append(peak_val)
    y = preceding_vals + following_vals

    if len(x) == len(y):
        roofTops.append(y)
        # tính tổng steps để đạt rooftop y
        steps = []
        for idx in range(len(x)):
            step = abs(x[idx] - y[idx])
            steps.append(step)

        sum_of_steps = sum(steps)
        costs.append(sum_of_steps)

#
min_cost = min(costs)
print(min_cost)

'''
min_index = costs.index(min_cost)
min_roofTop = roofTops[min_index]
print(min_roofTop)
'''
