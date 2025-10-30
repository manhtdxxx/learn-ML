N = int(input())
matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))

K = int(input())

sum_upper = 0
sum_lower = 0
for i in range(N):  # XÉT VỊ TRÍ HÀNG NGANG TỪ 0 -> 4
    for j in range(N):  # XÉT VỊ TRÍ HÀNG DỌC TỪ 0 -> 4
        if i + j < N - 1:  # CÁC SỐ NẰM TRÊN ĐƯỜNG CHÉO PHỤ CÓ TỔNG VỊ TRÍ TỪ 0 -> 3
            sum_upper += matrix[i][j]
        elif i + j > N - 1:
            sum_lower += matrix[i][j]

difference = abs(sum_upper - sum_lower)

if difference <= K:
    print("YES")
else:
    print("NO")

print(difference)
