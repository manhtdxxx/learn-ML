# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:36:01 2024

@author: Administrator
"""

# EXCEPION INFOR
import sys
try: 
    x = 2 + 'd'
    print(x)
except:
    a = sys.exc_info()
    print(a) # là 1 tuple
    b = a[0]
    print('LOẠI ERROR:',b)
    c = a[1]
    print('CỤ THỂ:',c)
    


print('')
# RAISE EXCEPTION
a = int(input('Hãy nhập vào 1 số nguyên dương nhỏ hơn 10: '))
loi = 'Số {} vừa nhập sai ĐK'.format(a)
if a < 1 or a >= 10:
    raise Exception(loi)
    


print('')
# ASSERT
a = int(input('Hãy nhập vào 1 số nguyên dương nhỏ hơn 10: '))
loi = 'Số {} vừa nhập sai ĐK'.format(a)
assert a >= 1 and a < 10, loi



print('')
# ỨNG DỤNG
def check_age(age):
    #assert age>0, 'Age cannot be negative number or zero'
    if age <= 0:
        raise Exception('Age cannot be negative number or zero')
    print(age)
    
try:
    check_age(-1)
except Exception as e:
    print(e)
    print('LỖI')