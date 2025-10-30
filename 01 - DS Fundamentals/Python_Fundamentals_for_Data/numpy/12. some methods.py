# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 00:05:22 2024

@author: Administrator
"""

import numpy as np

rng = np.random.default_rng(0)

x = rng.integers(0,10,(3,4))
print(x)
print('-'*100)

# unique : returns 1D-array containing unique values
y = np.unique(x)
print('UNIQUE:',y)
print('-'*100)

# transpose : ma trận chuyển vị
y = x.T
print('TRANSPOSE:\n',y)
print('-'*100)

# flip 1D-array
y = np.arange(10)
print('1D-ARRAY:',y)
print()

y = np.flip(y)
print('FLIP 1D-ARRAY:',y)
print('-'*100)

# flip 2D-array
y = np.flip(x) # lật theo đường chéo
print('2D-ARRAY:\n',y)
print()

y = np.flip(x,axis=0) # lật theo trục
print(y)
print()

y = np.flip(x,axis=1)
print(y)
print('-'*100)



# shuffle() makes changes to the original array
x = np.array([1, 2, 3, 4, 5])
print('ORIGINAL ARRAY:',x)
y = np.random.shuffle(x)
print('SHUFFLE IN-PLACE:',x)
print('''SHUFFLE () DOESN'T RETURN NEW ARRAY:''',y)
print()

# permutation() returns a re-arranged array (and leaves the original array un-changed).
x = np.array([1, 2, 3, 4, 5])
y = np.random.permutation(x)
print('ORIGINAL ARRAY:',x)
print('PERMUTATION RETURNS NEW ARRAY:',y)































