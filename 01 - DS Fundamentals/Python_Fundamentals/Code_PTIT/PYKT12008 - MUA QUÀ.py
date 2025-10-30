'''
Tí và Tèo được cô giáo cử đi mua quà để thưởng cho các thành viên trong lớp.
Lớp học có tất cả M bạn học sinh, vì vậy hai bạn phải mua M món quà.
Tại cửa hàng quà lưu niệm có tất cả N món quà, món thứ i có giá bán bằng c[i].
Tuy nhiên, có A món quà mà Tí thích, và B món quà mà Tèo thích.
Hai bạn tranh nhau một hồi, cuối cùng họ quyết định chọn một danh sách quà sao cho
có ít nhất K món đồ mà cả 2 bạn cùng thích.
Các bạn hãy xác định xem số tiền ít nhất cần phải chi trả
để Tí và Tèo có thể mua được đủ số quà và thỏa mãn điều kiện của hai bạn hay không?

Input:
Dòng đầu tiên là N, M, K (1 ≤ N ≤ 100 000, 1 ≤ M, K ≤ N).
Dòng tiếp theo gồm N số nguyên lần lượt là giá bán c[i] của món quà thứ i (1 ≤ c[i] ≤ 10^9).
Dòng tiếp gồm số nguyên A, theo sau A số nguyên x[i], lần lượt là số thứ tự các món quà mà Tí thích.
Dòng tiếp gồm số nguyên B, theo sau B số nguyên y[i], lần lượt là số thứ tự các món quà mà Tèo thích.
(1 ≤ x[i], y[i] ≤ N).
Output:
In ra một số nguyên là đáp án tìm được. Nếu không có phương án nào thỏa mãn, in ra -1.
'''

N, M, K = map(int, input().split())
# N : gifts available
# M : gifts needed for M students
# K : (min) gifts both liked by Ti & Teo

prices = list(map(int, input().split()))  # including price of each gift in N gifts available

A = int(input())
x = map(int, input().split())  # including position of each gift in A gifts liked by Ti
B = int(input())
y = map(int, input().split())  # including position of each gift in B gifts liked by Teo

# x, y contain position of each gift starting from 1
# which needs converting into index starting from 0
ti_indices = [i - 1 for i in x]
teo_indices = [i - 1 for i in y]

# index of each gift BOTH liked by Ti & Teo
common_indices = set(ti_indices).intersection(set(teo_indices))
common_indices = list(common_indices)

# index of each gift ONLY liked by Ti, not liked by Teo
only_ti_indices = set(ti_indices) - set(common_indices)
only_ti_indices = list(only_ti_indices)

# index of each gift ONLY liked by Teo, not liked by Ti
only_teo_indices = set(teo_indices) - set(common_indices)
only_teo_indices = list(only_teo_indices)

# index of each gift not liked by Ti & Teo / the rest
not_liked_indices = set(range(len(prices))) - set(common_indices) - set(only_ti_indices) - set(only_teo_indices)
not_liked_indices = list(not_liked_indices)

#
common_prices = sorted([prices[i] for i in common_indices])
only_ti_prices = sorted([prices[i] for i in only_ti_indices])
only_teo_prices = sorted([prices[i] for i in only_teo_indices])
not_liked_prices = sorted([prices[i] for i in not_liked_indices])

#
total_cost = 0
if len(common_indices) < K:
    print(-1)
elif len(common_indices) == K:
    total_cost = sum(common_prices)
    M -= K
    rest_prices = sorted(only_ti_prices + only_teo_prices + not_liked_prices)
    for i in rest_prices[:M]:
        total_cost += i
    print(total_cost)
else:
    total_cost = sum(common_prices[:K])
    M -= K
    remaining_common_prices = common_prices[K:len(common_prices)]
    rest_prices = sorted(remaining_common_prices + only_ti_prices + only_teo_prices + not_liked_prices)
    for i in rest_prices[:M]:
        total_cost += i
    print(total_cost)


