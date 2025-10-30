# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:02:27 2024

@author: Administrator
"""

'''
CÁC PHƯƠNG THỨC XỬ LÝ CHUỖI

'''

# VIẾT HOA CHỮ CÁI ĐẦU MỖI CÂU
s = 'hôm nay trời đẹp quá'
s = s.capitalize()
print('viết hoa chữ cái đầu mỗi câu:',s)

# VIẾT HOA CHỮ CÁI ĐẦU MỖI TỪ
s = s.title()
print('viết hoa chữ cái đầu mỗi từ:',s)

# VIẾT HOA TOÀN BỘ
s = s.upper()
print('viết hoa toàn bộ:',s)

# VIẾT THƯỜNG TOÀN BỘ
s = s.lower()
print('viết thường toàn bộ:',s)

# ĐỔI CHỮ HOA VỚI THƯỜNG
s = 'HELLO mạnh'
s = s.swapcase()
print('swapcase:',s)


# CĂN LỀ
    # s.center(width,fillchart)
    # s.rjust()
    # s.ljust()
print('s.center:',s.center(10,'*')) # len(s) == 10, the rest filled with *
print('s.right just:',s.rjust(10,'*'))
print('s.left just:',s.ljust(10,'*'))


# LOẠI BỎ KÝ TỰ 2 ĐẦU : 
    # s.strip(char)
    # s.lstrip()
    # s.rstrip()
s = '----- nss --- channel -------------'
s1 = s.strip('-')
s2 = s.strip('- ')
print(s1)
print(s2)

# ĐIỀN ĐẦY KÝ TỰ BÊN TRÁI = 0 CHO ĐỦ WIDTH
s = 'abc'
s = s.zfill(6)
print(s)

# EXPAND TABS(\t)
s = 'nss\tchannel'
print(s)
s = s.expandtabs(10)
print(s)    

# ENCODE, DECODE : utf-8, utf-16, utf-32
s = 'nss channel'
s1 = s.encode('utf-16')
print(s1)

s2 = s1.decode('utf-16')
print(s2)

# MIN,MAX : DỰA VÀO MÃ ASCII