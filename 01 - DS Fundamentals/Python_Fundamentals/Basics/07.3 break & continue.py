# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:52:57 2024

@author: Administrator
"""

'''
BREAK: THOÁT KHỎI VÒNG LẶP HIỆN TẠI VÀ KHÔNG LẶP NỮA

CONTINUE: THOÁT KHỎI VÒNG LẶP HIỆN TẠI VÀ LẶP VÒNG TIẾP THEO

'''

# BREAK
for i in range(10):
    print(i)
    if i>=5: # đi đến giá trị 5 sẽ dừng
        break

n = 100
while n>0:
    print('n cũ =',n)
    n = n // 2
    print('n mới =',n)
    if n<50: 
        break # đi đến giá trị 25 sẽ dừng

for i in range(2,10):
    print ('Bảng cửu chương ',i)
    for j in range (1,10):
        print('{0}*{1}={2}'.format(i,j,i*j))
        if j > 5:
            break # dừng tại j = 6
    if i > 3:
        break # dừng tại i = 4
        
# CONTINUE
for i in range(10):
    if(i%2==1):
        continue # bỏ qua câu lệnh bên dưới nếu ĐK đúng
    print(i)

print('---------------------------')
for i in range(5):
    if i == 3:
        continue
    print(i)
print('---------------------------')
for i in range(5):
    if i == 3: 
        break
    print(i)