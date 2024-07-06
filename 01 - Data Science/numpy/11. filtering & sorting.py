# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:13:10 2024

@author: Administrator
"""

import numpy as np

a1 = [3,5,2,6]
a2 = [8,4,6,2]
a3 = [5,2,7,8]
b = np.array([a1,a2,a3])
print(b)
print()


# FILTER
###
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print('FILTER USING BOOLEAN LIST:', newarr)
print()

#####
arr = np.array([41, 42, 43, 44])
filter_arr = []
# go through each element in arr
for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
# filter
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
print()


###
print('FILTER DIRECTLY:',b[b<6]) # duyệt theo từng cột
print()
print('FILTER DIRECTLY:',b[b%2==0])




print('-'*100)
# SORT
x = np.array([2,1,4,3,5])
print(x)
print()

#
y = np.sort(x) # returns a new array
print(y)
print()

# argument_sort returns indices of elements sorted to ascend
y = np.argsort(x)
print(y)
print()

#
np.random.seed(0)
x = np.random.randint(0,10,(4,6))
print(x)
print()

y = np.sort(x,axis=0)
print(y)
print()

y = np.sort(x,axis=1)
print(y)



print('-'*100)
# SEARCH
###
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4) # return indices of value
print(x)
print(x[0])
print()


# searchsorted() returns the index where the specified value would be inserted 
# to maintain the search order
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
# 2 should be inserted on index of 1
# 4 should be inserted on index of 2
# 6 should be inserted on index of 3
print()


###
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)
print()















