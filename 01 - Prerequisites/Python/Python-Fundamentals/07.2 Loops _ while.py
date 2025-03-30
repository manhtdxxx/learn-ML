# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:55:31 2024

@author: Administrator
"""

# VD1: NHẬP VÀO SỐ N > 0. NẾU SAI THÌ NHẬP LẠI
n = -1
while n<=0:
    n = int(input('Nhập vào n > 0: '))

# VD2: TÍNH TỔNG TỪ i ĐẾN n
i = 0
tong = 0
while i <= n:
    tong = tong + i
    i = i + 1
    print(tong,i)
print('tong =',tong)

i = 0
tong = 0
while i <= n-1:
    i = i + 1
    tong = tong + i
    print(tong,i)
print('tong =',tong)

# ELSE
j = 0
while j<=10:
    print(j,'Bên trong vòng lặp')
    j = j + 1
else:
    print(j,'Bên ngoài vòng lặp')

print('------------------------')

j = 0
while j<=10:
    j = j + 1
    print(j,'Bên trong vòng lặp')
else:
    print(j,'Bên ngoài vòng lặp')

print('--------------------------')

# BREAK ĐƯỢC THỰC THI THÌ ELSE SẼ KHÔNG ĐƯỢC THỰC THI
j = 0
while j<=10:
    j+=1
    print(j,'Bên trong vòng lặp')
    if j >= 5:
        break
else:
    print(j,'Bên ngoài vòng lặp')




















