# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:54:57 2024

@author: Administrator
"""

'''
DICTIONARY:
    LƯU TRỮ CÁC GIÁ TRỊ DỮ LIỆU TRONG CÁC CẶP KEY: VALUE
    SẮP XẾP THEO THỨ TỰ (PYTHON 3.7)
    CÓ THỂ THAY ĐỔI
    
    KEY:
        IMMUTABLE NÊN LIST, SET, DICT KHÔNG THỂ DÙNG LÀM KEY (TUPLE CÓ THỂ LÀM KEY)
        DUPLICATES NOT ALLOWED
        1 KEY INCLUDES 1 VALUE
        
    VALUE:
        IMMUTABLE OR MUTABLE
        DUPLICATES ALLOWED
    
'''

# TẠO 1 DICTIONARY
sinhVien = {
    'hoVaTen': 'Nguyen Van A',
    'maLop' : 'DH01',
    'diemTB': 8.5
        }
print('DICT:',sinhVien)

# COPY
copied = sinhVien.copy()
print('COPIED:',copied)


print('')
#
a = sinhVien.keys()
print(a)
print(type(a))

b = sinhVien.values()
print(b)
print(type(b))

c = sinhVien.items()
print(c)
print(type(c))


print('')
# KIỂM TRA SỰ TỒN TẠI
print('hoVaTen' in sinhVien)


print('')
# DUYỆT KEY, VALUE = FOR
for i in sinhVien:
    print('duyệt keys:', i)
    
print('--------------------------')
for i in sinhVien.keys():
    print('duyệt keys:',i)
    
print('--------------------------')
for i in sinhVien.values():
    print('duyệt values:',i)
    
print('--------------------------')
for i,j in sinhVien.items():
    print('duyệt items:',i+ ': ' +str(j))
    
# LEN
print('LEN:',len(sinhVien))

# MAX, MIN : CÁC KEY PHẢI CÙNG KIỂU DỮ LIỆU
print('MAX',max(sinhVien)) # returns key max
print('MIN:',min(sinhVien)) # returns key min
    

print('')
# ACCESS VALUE
print('ACCESS VALUE:',sinhVien['hoVaTen'])

x = sinhVien.get('hoVaTen')
print('GET 1 VALUE:',x)

y = sinhVien.get('diemTB','maLop')
print('GET 2 VALUES:',y) # only 1

z = sinhVien.get('lop') # get non-existing value
print('GET NON-EXISTING VALUE:',z) # returns None

e = sinhVien.get('lop','key không tồn tại') # get non-existing value
print('GET NON-EXISTING VALUE:',e) # returns 'key không tồn tại'

f = sinhVien.setdefault('hoVaTen')
print('SETDEFAULT TO ACCESS VALUE:',f)


   
print('')
# THAY ĐỔI VALUE
sinhVien['maLop'] = 'DH02'
print('CHANGE VALUE:',sinhVien)

sinhVien.update({'maLop':'DH03'})
print('UPDATE 1 VALUE TO CHANGE:',sinhVien)

sinhVien.update({'maLop':'DH05','diemTB': 9.0})
print('UPDATE 2 VALUES TO CHANGE:',sinhVien)


print('')
# THÊM 1 ITEM
sinhVien['namHoc'] = 2025
print('UPDATE 1 ITEM TO ADD:',sinhVien)

sinhVien.setdefault('tuoi',18)
print('SETDEFAULT TO ADD:',sinhVien)

sinhVien.setdefault('diaChi')
print('SETDEFAULT TO ADD:', sinhVien)

# THÊM N ITEMS
sinhVien.update({'noiSinh':'Hà Nội','gioiTinh':'Nam'})
print('UPDATE 2 ITEMS TO ADD:',sinhVien)



print('')
# XÓA ITEM
a = sinhVien.pop('noiSinh')
print('VALUE POPPED:',a) # returns value
print('POP:',sinhVien)

b = sinhVien.popitem()
print('ITEM POPPED:',b) # returns tuple containing key, value
print('POPITEM THE LAST ITEM:',sinhVien)

del sinhVien['namHoc']
print('DEL:',sinhVien)

sinhVien.clear()
print('CLEAR:',sinhVien)

del sinhVien
# print(sinhVien) # error vì đã xóa hẳn dictionary
