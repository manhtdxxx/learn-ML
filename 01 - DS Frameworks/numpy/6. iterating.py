# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 20:53:33 2024

@author: Administrator
"""

import numpy as np

a1 = np.arange(10,20,2)
a2 = np.arange(40,50,2)
b = np.int16([a1,a2])
print(b)
print('-'*100)

###
for i in b:
    print('LOOPING 1D-ARRAY FROM 2D-ARRAY:',i)

print('-'*100)


# DUYỆT ELEMENTS TRONG MẢNG 2 CHIỀU TRỞ LÊN

# cách 1 : dùng for liên tiếp
for i in b:
    for j in i:
        print('LOOPING ELEMENTS FROM 2D-ARRAY:',j)
        
print('-'*100)


# cách 2 : chuyển về mảng 1 chiều dùng 4 hàm đã học
for i in np.ravel(b,order='F'): 
    print(i)
    
print('-'*100)


# cách 3  : dùng b.flat
print(b.flat)
for i in b.flat:
    print(i)
    
print('-'*100)


# cách 4 : dùng np.nditer(b) - N-Dimensional Iterator
print(np.nditer(b))
for i in np.nditer(b):
    print(i)
    
print('-'*100)


# cách 5 : dùng np.ndenumerate(b) sẽ duyệt luôn cả index
print(np.ndenumerate(b))
for idx, i in np.ndenumerate(b):
    print(idx,i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    