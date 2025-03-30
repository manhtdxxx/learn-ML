# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:35:16 2024

@author: Administrator
"""


'''
'''

# MỞ FILE KHÔNG DẤU
f = open('.\\file_handling\\file.txt', 'r')
print('OBJECT: ', f)
print()

r = f.read()  # đọc từ vị trí con trỏ đến hết
print(r)
print()

pointer_tell = f.tell()  # đã đọc hết nên file pointer ở cuối
print('Vị trí con trỏ file:', pointer_tell)

pointer_seek = f.seek(0)  # adjust con trỏ về vị trí 0
print('Điều chỉnh con trỏ file:', pointer_seek)

pointer_tell = f.tell() 
print('Vị trí con trỏ file sau seek:', pointer_tell)
print()

r = f.read(21)  # đọc từ vị trí con trỏ với giới hạn 22 kí tự
print(r)

f.seek(0)
r = f.read(22)  # đọc thêm dấu \n
print(r)

f.seek(0)
r = f.read(23)
print(r)

r = f.read(21)  # đọc tiếp
# nếu là 22 thì đọc thêm dấu \n
print(r)


f.close()  # đóng file
print('----------------------------')


# MỞ FILE CÓ DẤU
f = open('.\\file_handling\\file_unicode.txt', 'r', encoding='utf-8')
print(f)
print()

r = f.read(23)  # nếu 22 đọc thêm dấu \n
print(r)

pointer_tell = f.tell() 
print('Vị trí con trỏ file:', pointer_tell)  # do có dấu
print()

rline = f.readline()  # nếu dòng trước chưa xong thì đọc nốt,
print(rline)

rline = f.readline()  # đọc dòng tiếp theo
print(rline)
print()

f.seek(0)
rlines = f.readlines()
print(rlines)
print()

f.seek(0)
for i in f.readlines():
    print(i)
