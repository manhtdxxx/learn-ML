# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:13:50 2024

@author: Administrator
"""

import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a,'\n')
b = np.array([[6,5],[4,3],[2,1]])
print(b,'\n')

### NHÂN 2 MA TRẬN
c = a @ b # (3,3) @ (3,2) = (3,2)
#c = a.dot(b)
print('TÍCH 2 MA TRẬN:\n',c,'\n')

#c = b @ a ; print(c) # error do nhân sai quy tắc ma trận



### NHÂN 2 VECTO
a = np.array([1,2,3])
b = a @ a
print('TÍCH VÔ HƯỚNG CỦA 2 VECTO:',b)