# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:18:49 2024

@author: Administrator
"""

import numpy as np

a1 = np.arange(10,20,2)
a2 = np.arange(40,50,2)
b = np.int16([a1,a2])
print(b)
print()


#
print('ACCESS 1 ELEMENT IN 2D-ARRAY:',b[0,1])
print('ACCESS 1D ARRAY IN 2D-ARRAY:',b[1])
print()

print('ACCESS 1 ELEMENT OF EACH 1D-ARRAY WITH THE SAME INDEX IN 2D-ARRAY:\n',b[0:2,1])
print()

print('ACCESSS ELEMENTS OF ONLY 1D-ARRAY IN 2D-ARRAY:\n', b[1,0:4])
print()

print('ACCESS ELEMENTS OF EACH 1D-ARRAYS WITH THE SAME INDEXES IN 2D-ARRAY:\n',b[0:2,0:4])
print()
