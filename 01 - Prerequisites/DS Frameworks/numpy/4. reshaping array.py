# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:20:41 2024

@author: Administrator
"""

'''
ATTRIUTES:
    x.dtype
    x.shape
    x.ndim : số chiều của mảng
    x.size : tổng số phần tử trong mảng
    x.itemsize : số byte mà 1 phần tử chiếm trong bộ nhớ

    x.reshape(shape) : returns another array
    np.resize(x,(shape))
'''


import numpy as np

a1 = [3,3,6,7]
a2 = [30,30,60,70]
b = np.array([a1,a2])
print('ARRAY:\n',b)
print('DTYPE:',b.dtype)
print('SHAPE',b.shape)
print('SỐ CHIỀU:',b.ndim)
print('TỔNG SÓ PHẦN TỬ:',b.size)
print('ITEMSIZE:',b.itemsize)  # int 32 bit chiếm 4 bytes trong bộ nhớ
print()


c = b.reshape(4,2)
print('ARRAY AFTER RESHAPE:\n',c)
print('ORIGINAL ARRAY:\n',b)
print()


c = np.resize(b,(8,1))
print('ARRAY AFTER RESIZE:\n',c)
print('ORGINAL ARRAY:\n',b)
print()

# pass -1 as the value if having one "unknown" dimension
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)
print()


print('-'*100)

# CHUYỂN TỪ N-DIMENSIONAL ARRAY SANG 1D-ARRAY
a1 = [4,6,2,7]
a2 = [8,4,6,9]
a3 = [5,1,7,8]
b = np.array([a1,a2,a3])
print(b)
print()

# b.reshape
c = b.reshape(1,b.size,order='F') # đọc theo column
print(c)  # vẫn còn dấu [] ngoài do là mảng 2 chiều
c = c[0]
print(c)
print()

# np.resize
c = np.resize(b,(1,b.size))
print(c)  # vẫn còn dấu [] ngoài do là mảng 2 chiều
c = c[0]
print(c)
print()

# np.ravel
c = np.ravel(b,order='C')  # đọc theo row
print(c)
print()

# b.flatten
c = b.flatten(order='F')
print(c)
print()

