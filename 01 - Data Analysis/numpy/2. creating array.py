# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:36:10 2024

@author: Administrator
"""

import numpy as np


# np.arange(start,stop,step) : tạo mảng 1 chièu
b = np.arange(10)
print('ARRAY RANGE:',b)
print('KIỂU DỮ LIỆU CÁC PHẦN TỬ TRONG B:',b.dtype) # kiểu object
print('HÌNH DẠNG CỦA B:',b.shape,'\n') 

# np.zeros(size)
# np.ones(size)
x = np.zeros((3,4))
print('ZEROS:\n',x)
print('SHAPE:',x.shape)
print('DATA TYPE:',x.dtype,'\n') # luôn là float

# np.full(size,value)
x = np.full((3,4),100)
print('FULL:\n',x)
print('SHAPE:',x.shape)
print('DATA TYPE:',x.dtype,'\n')

# np.eye(rows, columns) : ma trận đơn vị
x = np.eye(4,6)
print('EYE:\n',x)
print('SHAPE:',x.shape)
print('DATA TYPE:',x.dtype,'\n')

# np.linspace(start,stop,size) : tạo mảng 1 chiều gồm n phần tử cách đều nhau
x = np.linspace(1,5,17)
print('LINSPACE:\n',x)
print('SHAPE:',x.shape)
print('DATA TYPE:',x.dtype,'\n')


print('-------------------------------------')

print('TẠO MẢNG NGẪU NHIÊN')
print()

# np.random.random(size) : generate random float numbers from 0 to 1
x = np.random.random((4,3))
print(x)
print()

# np.random.rand(rows,columns) : tương tự random
x = np.random.rand(4,3)
print(x)
print()

# np.random.randint(start, stop, size) : generate random int numbers from a to b
x = np.random.randint(0,10,(4,5))
print(x)
print()

print('-'*100)
print('TẠO MẢNG NGẪU NHIÊN GIẢ (PSEUDO RANDOM) = SEED')
print()

rng = np.random.default_rng(0)  # có seed nên luôn random cùng 1 kết quả với seed tương ứng

# rng.random(size) : generate random float numbers from 0 to 1
x = rng.random((3,4)) 
print(x)
print()

# rng.intergers (start, stop, size) :generate random int numbers from a to b
y = rng.integers(0,10,(3,4))
print(y)
print()

# rng.uniform (start, stop, size) : generate random float numbers from a to b
y = rng.uniform(0,10,(3,4))
print(y)
print()

# rng.normal(mean,std,size)
y = rng.normal(0,1,(3,3))
print(y)
print()

# rng.choice(array,size)
y = rng.choice([3,5,7,9],size=(3,4))
print(y)
print()

y = rng.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(4,6))
print(y)





























