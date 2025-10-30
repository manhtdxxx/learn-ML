# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:22:50 2024

@author: Administrator
"""

# TÌM VỊ TRÍ BẮT ĐẦU CHUỖI CON: 
    # s.find('substring',start,end) : trả về -1 nếu không tìm thấy
    # s.index('substring',start,end) : error nếu tìm k thấy
    # s.rfind(), s.rindex() : tìm từ phải qua trái
s = 'Lập trình Python là xu hướng hiện nay. Các bạn nên học lập trình Python'
print('tìm vị trí bắt đầu chuỗi con: ',s.find('Python'))
print('tìm vị trí bắt đầu chuỗi con: ',s.find('PythonX')) # -1
print('tìm vị trí bắt đầu chuỗi con: ',s.rfind('Python')) # tìm từ phải qua
print(len(s))


# ĐẾM SỐ LẦN XUẤT HIỆN CỦA CHUỖI CON: 
    # s.count('substring',start,end)
print('đếm số lượng chuỗi con: ', s.count('Python'))

# THAY THẾ CHUỖI: 
    # s.replace(old, new, count)
s = s.replace('Python','PYTHON',1) # Thay thế 1 lần
print('replace:',s)


# NỐI CÁC PHẦN TỬ TRONG 1 LIST, TUPLE, SET THÀNH STRING
s1 = '---' # cầu nối
s2 = ['nss','channel','2021'] # PHẢI LÀ KIỂU STR HẾT
s = s1.join(s2)
print('join:',s)


print('')
# CẮT CHUỖI THÀNH 1 LIST
s = 'Lập trình Python là xu hướng hiện nay. Các bạn nên học lập trình Python'
list1 = s.split(' ') # chia theo dấu cách và bỏ luôn dấu cách
print(list1)

list2=s.split('.') # chia theo dấu . và bỏ luôn dấu .
print(list2)

s = 'Python Python Python Python'
list3 = s.split(' ',2) # cắt thành n+1 phần tử
print(list3)

list4 = s.split(' ',-1) # <0 sẽ chia hết
print(list4)


print('')
# CẮT CHUỖI NHIỀU DÒNG THÀNH 1 LIST
s = '''3 chìm 7 nổi với nước non
rắn nát mặc dầu tay kẻ nặn
mà em vẫn giữ tấm lòng son
'''
s1 = s.splitlines(True)
print(s1)
s2 = s.splitlines(False) 
print(s2)

