# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:04:54 2024

@author: Administrator
"""
'''
CÁC HÀM XỬ LÝ CHUỖI TRẢ VỀ TRUE/FALSE

'''

# KIỂM TRA CHUỖI BẮT ĐẦU / KẾT THÚC BẰNG CHUỖI NÀY KHÔNG
s = 'nsschannel'
a = s.startswith('n')
b = s.startswith('a')
c = s.endswith('el')
print(a)
print(b)
print(c)

s1 = s.isalpha()
print('is alphabetic:',s1) # có dấu cách là False

s2 = s.isdecimal()
print('is decimal:',s2)

s3 = s.isnumeric()
print('is numeric:',s3)

s4 = s.isalnum()
print('is alpha & numeric:',s4) 

# s5 = s.islower()
# s6 = s.isupper()
# s7 = s.istitle()
# s8 = s.isspace() # trả về True nếu tất cả là space