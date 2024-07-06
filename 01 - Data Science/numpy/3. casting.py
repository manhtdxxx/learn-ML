# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:56:07 2024

@author: Administrator
"""

import numpy as np

# CÁC ELEMENTS TRONG ARRAY LUÔN CÙNG DATA TYPE
a = [2.,3,5,7]
b = np.array(a)
print('ARRAY:',b)
print('DATA TYPE:',b.dtype,'\n')

a = [2 + 3j,3,5,7]
b = np.array(a)
print('ARRAY:',b)
print('DATA TYPE:',b.dtype,'\n')


print('-'*100)

# CÁCH 1 : ÉP KIỂU TRONG LÚC TẠO MẢNG
a = [2,3,5,6]
b = np.array(a,dtype=float)
print('ARRAY:',b)
print('DATA TYPE:',b.dtype,'\n')

a = [2,3,5,6]
b = np.array(a,dtype=complex)
print('ARRAY:',b)
print('DATA TYPE:',b.dtype,'\n')


print('-'*100)

# CÁCH 2 : ÉP KIỂU TRONG LÚC TẠO MẢNG
'''
KIỂU INT:
    SIGNED:
        int_
        byte = int8
        short = int16
        intc = int32
        longlong = int64 = int0

    UNSIGNED: (THÊM TIỀN TỐ U)
        uint_
        ...

KIỂU FLOAT:
    float_
    float16
    single = float32
    double = float64
    longdouble = float128
    
KIỂU COMPLEX:
    complex_
    csingle = complex64
    cdouble = complex128
    clongdouble = complex256
    
KIỂU BOOLEAN:
    bool_
    bool8
'''
a = [2,3,5,6]
b = np.bool_(a)
print('ARRAY:',b)
print('DATA TYPE:',b.dtype,'\n')

print('-'*100)

# CÁCH 3 : ÉP KIỂU VỚI EXISTING ARRAY
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)


# LỖI TRÀN (OVERFLOW ERROR)


























