# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:29:57 2024

@author: Administrator
"""

'''
LAMBDA ARGUMENTS : EXPRESSION
    1 hàm lambda là 1 hàm ẩn danh nhỏ
    có thể nhiều arguments, nhưng chỉ 1 expression
    
'''

checkSoChan = lambda a : a%2==0
print('check số chẵn:',checkSoChan(5))
print('check số chẵn:',checkSoChan(6))

tinhTong = lambda a,b : a+b
print('tính tổng:',tinhTong(5,10))
print('tính tổng:',tinhTong(-5,100))

#
def hamMu_n(n):
    return lambda x : x**n

hamMu2 = hamMu_n(2)
hamMu3 = hamMu_n(3)

print(hamMu2(2))
print(hamMu3(3))


