# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:14:10 2024

@author: Administrator
"""

import numpy as np

a1 = np.arange(10,20,2)
a2 = np.arange(40,50,2)
b = np.int16([a1,a2])
print(a1)
print()
print(a2)
print()
print(b)


print('-------------------------------')
# CỘNG : + hoặc np.add(x,y)
# NHÂN : * hoặc np.multiply(x,y)
c = a1 + 1
print('MẢNG + SỐ:',c)
print()

c = a1 + a2
print('MẢNG + MẢNG',c)
print()

c = a1 + b
print('2D-ARRAY + 1D-ARRAY:\n',c)
print()


# TRỪ : - hoặc np.subtract(x,y)
# CHIA : / hoặc np.divide(x,y)
c = b - a1
print('2D-ARRAY - 1D-ARRAY:\n',c)
print()

c = a1 - b  # = -(b-a1)
print('1D-ARRAY - 2D-ARRAY:\n',c)
print()

c = 1/b
print('CHIA MẢNG VỚI 1 SỐ:\n',c)
print()

c = b/a1
print('2D-ARRAY / 1D-ARRAY:\n',c)
print()

c = a1/b # = 1/(b/a1)
print('1D-ARRAY / 2D ARRAY:\n',c)
print()