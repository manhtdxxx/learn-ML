count_4 = 0
count_7 = 0

n = int(input())
for i in str(n):
    if i == '4':
        count_4 += 1
    elif i == '7':
        count_7 += 1

total = count_4 + count_7
if total == 4 or total == 7:
    print('YES')
else:
    print('NO')