# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:13:08 2024

@author: Administrator
"""

'''
Kiểu dữ liệu cơ bản
- int
- float
- Decimal() từ thư viện decimal
- complex: 1 + 2j
- Fraction() từ thư viện fractions
- str
- bool: TRUE/FALSE
- NoneType: None
'''

x=1
y=2.2
z=1+3j
e=True
d='abc'
f=None

# chỉ ra kiểu dữ liệu
print(type(x))
print(type(y))
print(type(z))
print(type(e))
print(type(d))
print(type(f))

a = 5
b = 2
c = a/b
print('Kiểu dữ liệu của c: ',type(c))

# ép kiểu dữ liệu
n = 100
m = '200'
print (n + int(m))
print (str(n) + m)

# Decimal() chuẩn hơn float
from decimal import *
getcontext().prec = 100 # 98 số sau dấu .
x = 10
y = 3
z = Decimal(x) / Decimal(y)
print(z)
print(type(z))

print(x/y)
print(type(x/y))

# complex
x = 3 + 2j
y = complex(5,6)
print(x)
print(y)
print(type(x))
print(x.real)
print(x.imag)

# Fraction()
from fractions import *
x = Fraction(1,3)
y = Fraction (1,2)
z = x + y
print(z)
print(type(z))


