# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:41:16 2024

@author: Administrator
"""

'''
TRY: 
    ĐOẠN CODE DỰ ĐOÁN CÓ LỖI
    
EXCEPT ERROR 1:
    PHƯƠNG ÁN XỬ LÍ ERROR 2
    
EXCEPT ERROR 2:
    PHƯƠNG ÁN XỬ LÍ ERROR 2
    
EXCEPT ERROR 3:
    PHƯƠNG ÁN XỬ LÍ ERROR 3
            
ELSE:
    THỰC THI ĐOẠN NÀY NẾU KHỐI TRY KHÔNG LỖI
    
FINALLY:
    THỰC THI BẤT KỂ KHỐI TRY CÓ LỖI HAY KHÔNG

'''

try:
    a = int(input('Nhập vào số nguyên a: '))
    print(str(a)+' + 5 = ',str(a+5))
except Exception as e: 
    print(e)
else:
    print('Không có lỗi xảy ra')
finally:
    print('Kết thúc chương trình')


print('')
'''
SOME COMMON ERRORS:
    IOError : input output 
    ZeroDivisionError : a/0
    ValueError : int('a')
    ImportError : import sai module
    IndexError : gọi index không tồn tại trong tập hợp
    TypeError : int + str
    
'''

try:
    a = [2,3]
    b = a[2]
    print(b)
except ZeroDivisionError:
    print('Xảy ra lỗi chia cho 0')
except ValueError:
    print('Xảy ra lỗi value')
except ImportError:
    print('Xảy ra lỗi import')
except IndexError:
    print('Xảy ra lỗi index')
