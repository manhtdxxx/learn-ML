# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:22:59 2024

@author: Administrator
"""

'''
Phép toán cơ bản
- cộng
- trừ
- nhân
- chia
- chia lấy phần dư ( % )
- chia lấy phần nguyên ( // )
- mũ ( ** )

'''
a = int(input('Nhập dữ liệu vào a: '))
print ('Kiểu dữ liệu của a: ', type(a))
b = int(input ('Nhập dữ liệu vào b: '))
print ('Kiểu dữ liệu của b: ',type(b))

print('{0} + {1} == {2}' .format(a,b,a+b))
print('{0} - {1} == {2}' .format(a,b,a-b))
print('{0} * {1} == {2}' .format(a,b,a*b))
print('{0} / {1} == {2}' .format(a,b,a/b))
print('{0} // {1} == {2}' .format(a,b,a//b))
print('{0} % {1} == {2}' .format(a,b,a%b))
print('{0} ** {1} == {2}' .format(a,b,a**b))


print('-----------------------------------------')
'''
TOÁN TỬ GÁN:
=
+=
-=
*=
/=
//=
%=
**=

'''
x = y = z = d = e = f = int(input('Nhập giá trị: '))
x+=9 # ==> x = x + 9
print(x)

y-=10
print(y)

z*=8
print(z)

d/=5
print(d)

e%=2
print(e)

f**=3
print(f)

