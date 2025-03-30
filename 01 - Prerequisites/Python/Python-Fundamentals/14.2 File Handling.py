# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:07:01 2024

@author: Administrator
"""

'''
'''
# R+
f = open('.\\file_handling\\file_2.txt', 'r+', encoding='utf-8')

# read when open
r = f.read()
print(r)
print('-'*100)


# overriding từ vị trí con trỏ chuột
f.seek(0)
w1 = f.write('Hôm này trời mưa to tầm tã\ntại sao phải ngồi trong nhà')
print('LEN:', len(('Hôm này trời mưa to tầm tã\ntại sao phải ngồi trong nhà')))
print('WRITE:', w1)

f.seek(0)
r = f.read()
print(r)
print('-'*100)


# overriding chỉ trong giới hạn kí tự cần ghi đè
f.seek(0)
w2 = f.write('Vì em covid ghé thăm.')

f.seek(0)
r3 = f.read()
print(r3)
print('-'*100)


f.close()
print('CHECK ĐÓNG FILE:', f.closed)
print('CHECK MODE:', f.mode)
print('CHEK NAME:', f.name)
print('-'*100)

import os
# ĐỔI TÊN
# os.rename('.\\file_handling\\file2.txt', '.\\file_handling\\file_2.txt')

# XÓA FILE
# os.remove('.\\file_handling\\file_2.txt')

# remove file if exists
if os.path.exists("demo_file.txt"):
    os.remove("demo_file.txt")
else:
    print("The file does not exist")

# TẠO THƯ MỤC (make directory)
# os.mkdir('hoc')

# GET CURRENT WORK DIRECTORY
print('GET CURRENT WORK DIRECTORY', os.getcwd())

# XÓA THƯ MỤC
# os.rmdir('hoc')

