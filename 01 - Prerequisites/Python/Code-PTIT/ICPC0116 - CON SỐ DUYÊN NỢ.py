"""
Con số duyên nợ là con số có chữ số đầu và chữ số cuối giống nhau.
Viết chương trình kiểm tra xem một số nguyên dương n ghi trong hệ thập phân
có chữ số đầu và chữ số cuối giống nhau không?
"""

for _ in range(int(input())):
    x = input()  # số nguyên dương x ghi ở hệ thập phân.
    if x[0] == x[-1]:
        print('YES')
    else:
        print('NO')
