# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 22:26:09 2024

@author: Administrator
"""

import numpy as np


# LIST CHUYỂN ĐƯỢC QUA ARRAY
a = [4,7,3]
b = np.array(a)
print('LIST -> ARRAY:',b)
print('KIỂU DỮ LIỆU CỦA B:',type(b))
print('KIỂU DỮ LIỆU CÁC PHẦN TỬ TRONG B:',b.dtype) # kiểu int64bit
print('HÌNH DẠNG CỦA B:',b.shape,'\n')

# TUPLE CHUYỂN ĐƯỢC QUA ARRAY
a = (4,7,3)
b = np.array(a)
print('TUPLE -> ARRAY:',b)
print('KIỂU DỮ LIỆU CỦA B:',type(b))
print('KIỂU DỮ LIỆU CÁC PHẦN TỬ TRONG B:',b.dtype) # kiêu int64bit
print('HÌNH DẠNG CỦA B:',b.shape,'\n')

# SET KHÔNG CHUYỂN ĐƯỢC QUA ARRAY VÌ SET KHÔNG CÓ THỨ TỰ
a = {4,7,3}
b = np.array(a)   # giữ nguyên
print('SET -> ARRAY:',b)
print('KIỂU DỮ LIỆU CỦA B:',type(b))
print('KIỂU DỮ LIỆU CÁC PHẦN TỬ TRONG B:',b.dtype)  # kiểu object
print('HÌNH DẠNG CỦA B:',b.shape,'\n')


# MẢNG 2 CHIỀU TẠO THÀNH TỪ CÁC MẢNG 1 CHIỀU
a1 = [4,6,7,9]  # có thể là list hoặc tuple
a2 = [6,2,8,3]  # các mảng 1 chiều phải cùng số lượng phần tử
a3 = [5,0,2,1]
b = np.array([a1,a2,a3])
print('2-DIMENSIONAL ARRAY:\n',b)
print('SHAPE:',b.shape,'\n')  # 3 mảng 1 chiều, mỗi mảng gồm 4 phần tử


a1 = range(10)
a2 = range (20,30)
a3 = range (30,40)
b = np.array([a1,a2,a3])
print('2-DIMENSIONAL ARRAY:\n',b)
print('SHAPE:',b.shape,'\n')


# MẢNG 3 CHIỀU : GỒM CÁC MẢNG N CHIỀU TẠO THÀNH
a1 = [[1,4,6,8],[2,5,7,3],[5,7,3,6]]
a2 = [[10,40,60,80],[20,50,70,30],[50,70,30,60]]
b = np.array([a1,a2])
print('3-DIMENSIONAL ARRAY:\n',b)
print('SHAPE:',b.shape,'\n') 
# 2 mảng 2 chiều, mỗi mảng 2 chiều gồm 3 mảng 1 chiều, mỗi mảng 1 chiều gồm 4 phần tử


# MẢNG N CHIỀU : GỒM CÁC MẢNG N-1 CHIỀU TẠO THÀNH






























