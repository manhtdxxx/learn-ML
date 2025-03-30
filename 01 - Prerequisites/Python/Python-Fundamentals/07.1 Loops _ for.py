# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:45:05 2024

@author: Administrator
"""

# VD1: >=0 & <10
for i in range(10):
    print(i)
    
# VD2: Tính tổng từ 0 đến n
n = int(input('Nhập vào giá trị n: '))
tong = -1
for i in range(n+1):
    tong = tong + i
    print(tong,i)
print('tong = ',tong)

# VD3: range (start, end, increment)
for i in range(0,10,2):
    print (i)

for i in range(10,0,-1):
    print(i)
    
# VD4: duyệt phần tử trong list
colors = ['red','green','yellow','purple']
for i in colors:
    print(i)
    
for i in range(len(colors)):
    print(colors[i])