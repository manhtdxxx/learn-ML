# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:32:05 2024

@author: Administrator
"""

'''
Toán tử so sánh ---> Trả về TRUE/FALSE
- >
- <
- ==
- !=
- >=
- <=

Toán tử logic
- and
- or
- not

'''

x = int(input('Nhập dữ liệu a: '))
y = int(input('Nhập dữ liệu b: '))

print ('{0} < {1} là {2}'.format(x,y,x<y))
print ('{0} > {1} là {2}'.format(x,y,x>y))
print ('{0} == {1} là {2}'.format(x,y,x==y))
print ('{0} != {1} là {2}'.format(x,y,x!=y))

z = int(input('Nhập dữ liệu c: '))

print ((x<y)and(y<z))
print('({0}<{1}) and ({1}<{2}) là {3}'. format(x,y,z,(x<y)and(y<z)))

print ((x<y)or(y<z))
print ('{0}<{1} and {1}<{2} là {3}'.format(x,y,z,(x<y)and(x<z)))

print(not(x>z))
print ('not ({0}>{1} là {2}'.format(x,z,not(x>z)))       

