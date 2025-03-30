# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 19:40:03 2024

@author: Administrator
"""

'''
THƯ VIỆN TOÁN HỌC MATH

math.ceil(x)        : trả về int min > hoặc = x
math.floor(x)       : trả về int max < hoặc = x

math.sqrt()

math.fabs(x)        : |x|

math.pow(x,y)       : x**y
math.exp(x)         : e**x

math.log(x [,base]) : log[base](x) nếu k có base thì mặc định là log[e](x)
math.log10(x)
math.log2(x)

math.pi
math.e

math.radians
math.degrees
'''
import math

x = float(input('x: '))

#print(math.log(x))
#print(math.log(x,10))

print('log10(a):',math.log2(4))

print('e lũy thừa x:',math.exp(x))  
print('x lũy thừa y:',math.pow(x,2)) 

print('căn bậc 2:',math.sqrt(x))

print('giá trị tuyệt đối:',math.fabs(x))

print('giá trị trần:',math.ceil(x))
print('giá trị sàn:',math.floor(x))

print('số pi:',math.pi)
print('số e:',math.e)

print(math.degrees(math.pi))
print(math.radians(180))

# k cần thư viện math
print('round:',round(x,2)) # làm tròn thành 2 số sau dấu thập phân
