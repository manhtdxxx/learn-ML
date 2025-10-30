# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:12:47 2024

@author: Administrator
"""

# Toán tử [n]
s = 'abcd'
print('Toán tử [n]:',s[0])
print('Toán tử [n]:',s[1])
print('Toán tử [n]:',s[-1]) # lấy từ cuối lên

print('--------------------')
# Toán tử [n:m]
s = 'abcdefgh'
print('Toán tử [n:m]:',s[2:4])
print('Toán tử [n:m]:',s[:4])
print('Toán tử [n:m]:',s[4:])
print('Toán tử [n:m]:',s[-5:-2]) # empty when typing [-2:-5]

# Cộng chuỗi 
s1='Xin chào'
s2='TITV'
s3=s1+' '+s2
print('Cộng chuỗi:',s3)

# CHUỖI NHIỀU DÒNG
chuoi_nhieu_dong = '''
Dòng 1
Dòng 2
Dòng 3 
'''
print(chuoi_nhieu_dong)

# LẶP CHUỖI & XUỐNG DÒNG
chep_phat = 'Em hứa làm bài tập đầy đủ\n' # \n để xuống dòng
chep_phat_5 = chep_phat * 5
print(chep_phat_5)

# LOOPING
for i in 'banana':
    print(i)
    
# KIỂM TRA CHUỖI CON
chuoi_1 = 'Xin chào TITV'
chuoi_2 = 'TITV'
chuoi_3 = 'VN'
if chuoi_2 in chuoi_1:
    print ("Chuỗi 2 là chuỗi con của chuỗi 1")
else:
    print('Chuỗi 2 không là chuỗi con của chuỗi 1')

if chuoi_3 in chuoi_1:
    print ('Chuỗi 3 là chuỗi con của chuỗi 1')
else:
    print('Chuỗi 3 không là chuỗi con của chuỗi 1')



# REPR() NA NÁ STR() BUT THERE ARE SOME DIFFERENCES
s = 12
z = repr(s) # tạo bản sao của các data type khác thành string với id mới
print(s, type(s), id(s))
print(z, type(z), id(z))

# CHR() : MÃ ASCII
s = 65
print(chr(s))

# CHOICE() TRONG THƯ VIỆN RANDOM : TRẢ VỀ NGẪU NHIÊN 1 KÍ TỰ
import random
s ='abcdef'
print('random choice:',random.choice(s))

# LEN() TRẢ VỀ ĐỘ DÀI CHUỖI
print('độ dài chuỗi:',len(s))
























