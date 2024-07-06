# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:33:21 2024

@author: Administrator
"""


'''
JOINING ARRAYS:
    np.concatenate
    np.vstack
    np.hstack
    np.dstack

SPLITTING ARRAY:
    np.split
    np.array_split
    np.hsplit
    np.vsplit
    np.dsplit
    
'''

import numpy as np

a1 = [4,6,2,7]
a2 = [8,4,6,9]
a3 = [5,1,7,8]
b = np.array([a1,a2,a3])
print(b)
print('-'*100)

#
c = np.vstack([a1,a2]) # vertical stack khi 2 columns =
print(c)
print()

#
c = np.hstack([a1,a2]) # horizontal stack khi 2 rows =
print(c)
print()

#
c = np.concatenate((a1,a2),axis=0) # axis = 0 là trục dọc, thể hiện cho rows
print(c)
print()

#
c = np.dstack([a1,a2]) # depth stack giống như ma trận chuyển vị của vstack
print(c)
print('-'*100)


#
arr = np.array([1, 2, 3, 4, 5, 6, 7])
newarr = np.array_split(arr, 3) # split into 3 1D-array, axis=0 
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
print('-'*50)

#
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3) # split into 3 2D-array
print(newarr)
print('-'*50)


#
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(arr)
print()
newarr = np.array_split(arr, 3, axis=1) # axis=1 là trục ngang, thể hiện cho columns
print(newarr)
print('-'*50)


#
x = np.arange(10)
y = np.split(x,[3,5,7]) # subarray bắt đầu từ index 3, r lại 5, r 7
print(y)










