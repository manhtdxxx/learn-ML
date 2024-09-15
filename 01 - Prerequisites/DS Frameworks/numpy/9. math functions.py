# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:50:50 2024

@author: Administrator
"""

import numpy as np


# MAX, MIN , SUM
a1 = [3,5,2,6]
a2 = [8,4,6,2]
a3 = [5,2,7,8]
b = np.array([a1,a2,a3])
print(b)
print()

d = b.max(axis=0)
print('ELEMENTS MAX THEO CHIỀU DỌC:',d) # axis = 0 là trục dọc
print()

d = b.min(axis=1)
print('ELEMENTS MIN THEO CHIỀU NGANG:',d) # axis = 1 là trục ngang
print()

d = b.max()
print('ELEMENT MAX:',d)
print()

d = b.sum()
print('TỔNG ELEMENTS:',d)
print()

d = b.sum(axis=0)
print('TỔNG ELEMENTS THEO CHIỀU DỌC:',d)
print()


# MEAN, VAR, STD
np.random.seed(0)
massive_array = np.random.random(1000)

x = np.mean(massive_array)
print('MEAN:',x)

x = np.var(massive_array)
print('VAR:',x)
x = np.sqrt(x)
print('SQRT ROOT OF VAR:',x)

x = np.std(massive_array)
print('STD:',x)






















