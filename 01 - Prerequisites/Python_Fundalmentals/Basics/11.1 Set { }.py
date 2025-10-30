# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:15:06 2024

@author: Administrator
"""

'''
SET:
    KHÔNG CÓ THỨ TỰ
    KHÔNG THỂ THAY ĐỔI, NHƯNG VẪN XÓA VÀ THÊM ĐƯỢC -> MUTABLE
    GIÁ TRỊ KHÔNG TRÙNG NHAU
    
    CHỈ CHỨA IMMUATABLE SUCH AS TUPLE (TRONG TUPLE CHỈ CHỨA IMMUTABLE),...
    KHÔNG CHỨA LIST, SET
    
'''

# TẠO SET
monHoc = {'Toán','Lý','Hóa'}
print ('tạo set:',monHoc)

#
x = (4,2,'a') # NẾU X LÀ SET OR LIST (MUTABLE) THÌ Y KHÔNG CHỨA ĐƯỢC
y = {3,4,12,x}
print('SET CHỈ CHỨA IMMUTABLE TUPLE:',y)

# LEN
print('LEN:',len(monHoc))

# KIỂM TRA SỰ TỒN TẠI
print('check existence:', 'Toán' in monHoc)

# DÙNG FOR DUYỆT PHẦN TỬ
for i in monHoc:
    print('dùng for duyệt phần tử: ',i)

# MAX, MIN, SUM : KHI CÁC PHẦN TỬ CÙNG KIỂU DỮ LIỆU


print('')
# THÊM 1 PHẦN TỬ = ADD
monHoc.add('Lịch sử')
print('ADD:',monHoc)

monHoc.add('Lịch sử') # không lấy giá trị trùng
print('ADD DUPLICATE:',monHoc)


print('')
#THÊM 1 TẬP HỢP = UPDATE
hocThem1 = {'Anh Văn','Đàn Piano'}
monHoc.update(hocThem1)
print('UPDATE SET:',monHoc)

hocThem2 = ('Sinh học','Vật lý')
monHoc.update(hocThem2)
print('UPDATE TUPLE:',monHoc)

hocThem3 = ['Địa Lý','Tin học']
monHoc.update(hocThem3)
print('UPDATE LIST:',monHoc)


print('')
# TẠO 1 SET MỚI KHI THÊM TẬP HỢP = UNION
x = {'a','b','c'}

x1 = {1,2,3}
y1 = x.union(x1)
print('UNION SET:',y1)

x2 = [5,6,7]
y2 = x.union(x2)
print('UNION LIST:',y2)

x3 = ('e','f','g')
y3 = x.union(x3)
print('UNION TUPLE:',y3)

print('ORIGINAL SET:',x)



print('')
# XÓA = REMOVE
monHoc.remove('Sinh học')
print('REMOVE:',monHoc)

#monHoc.remove('Võ thuật') # error vì phần tử không tồn tại
#print(monHoc)

# dùng if ... in kiểm tra sự tồn tại to avoid error
if 'Võ thuật' in monHoc:
    monHoc.remove('Võ thuật')
    print(monHoc)


# XÓA = DISCARD
monHoc.discard('Toán')
print('DISCARD:',monHoc)

monHoc.discard('Võ thuật')
print('DISCARD NON-EXSISTING ELEMENT:',monHoc)


# XÓA PHẦN TỬ ĐẦU TIÊN = POP
monHoc.pop()
print('POP THE FIRST ELEMENT:',monHoc)


print('')
# COPY
copied = monHoc.copy()
print('COPIED SET:',copied)


# SORTED
x = {4,6,2,7,23,45,7,54,}
sorted_x = sorted(x)
print('SORTED TẠO THÀNH LIST MỚI:',sorted_x)
sorted_x = set(sorted_x)
print('LIST --> SET:',sorted_x)


# LÀM RỖNG TẬP HỢP = CLEAR
monHoc.clear()
print('CLEAR:',monHoc)


# XÓA HẲN TẬP HỢP = DEL
del monHoc
# print(monHoc) # error vì không còn tồn tại

















