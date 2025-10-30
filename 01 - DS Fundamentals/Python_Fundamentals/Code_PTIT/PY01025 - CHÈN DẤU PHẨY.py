x = int(input())
parts = []
current = ''
'''
Khi  viết giá trị số nguyên trong Tiếng Anh, 
người ta thường thêm dấu phẩy để phân tách các nhóm 3 chữ số 
(tính từ cuối)
'''
for i in str(x)[::-1]:
    current += i
    if len(current) == 3:
        current = current[::-1]
        parts.append(current)
        current = ''

if len(current) > 0:  # và nhỏ hơn 3
    current = current[::-1]
    parts.append(current)

parts.reverse()
new_x = ','.join(parts)
print(new_x)
