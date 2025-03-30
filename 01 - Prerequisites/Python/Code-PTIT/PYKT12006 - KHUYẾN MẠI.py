"""
Một cửa hàng thời trang đang thực hiện chương trình khuyến mại giảm giá.
Ban đầu, giá của sản phẩm i là a[i], khi đến tuần giảm giá, giá của chúng giảm xuống còn b[i].
Tuy nhiên, chủ cửa hàng rất khôn, nhằm đánh lừa khách hàng,
mỗi số sản phẩm giá tăng lên chứ không hề giảm xuống.

Nhận biết được quy luật này, Tí mặc dù cần phải mua tổng cộng N sản phẩm,
nhưng cậu quyết định mua ít nhất K sản phẩm trước đợt khuyến mại,
và số sản phẩm còn lại sẽ mua trong đợt khuyến mại.

Giả sử rằng Tí chọn tối ưu được các sản phẩm ban đầu,
các bạn hãy tính xem số tiền ít nhất Tí cần bỏ ra để mua đủ N sản phẩm là bao nhiêu?

Input:
Mỗi test bắt đầu bằng số nguyên N và K (1 ≤ N, K ≤ 100 000).
Dòng thứ hai gồm N số nguyên a[i], giá sản phẩm thứ i mà trước đợt giảm giá.
Dòng cuối gồm N số nguyên b[i], là giá của sản phẩm sau khi giảm giá.
(1 ≤ a[i], b[i] ≤ 10^4).

Output:
In ra một số nguyên là đáp án của bài toán.
"""


n, k = map(int, input().split())
# n : số sp cần mua
# k : số sp mua trước khi giá thay đổi
a = list(map(int, input().split()))  # giá gốc
b = list(map(int, input().split()))  # giá thay đổi


ab = []  # chứa [giá gốc, giá thay đổi]
for i in range(n):
    ab.append([a[i], b[i]])

idx_ab = list(enumerate(ab))  # chứa (index, [giá gốc, giá thay đổi])
idx_ab.sort(key=lambda x: x[1][0] - x[1][1])
# x < 0 : giá đã tăng
# x > 0 : giá đã giảm
# thứ tự mua trước kì thay đổi giá:
# giá tăng nhiều nhất sau này --> giá giữ nguyên --> giá giảm nhiều nhất sau này

buying_order = []
total_price = 0
for i in range(k):
    total_price += idx_ab[i][1][0]
    buying_order.append(idx_ab[i][0])
    # mua trước những món có giá tăng nhiều nhất sau này
    # nếu không có món nào tăng giá, thì mua trước món đồ có giá giảm nhỏ nhất sau này

while k < n:  # mua nốt (n-k) món
    total_price += min(idx_ab[k][1][0], idx_ab[k][1][1])  # so sánh giá gốc và giá thay đổi
    buying_order.append(idx_ab[k][0])
    # nếu giá sau này tăng, mua giá gốc
    # nếu giá sau này giảm, mua giá giảm
    k += 1

#
buying_order = [i+1 for i in buying_order]

print(total_price)
#print(buying_order)