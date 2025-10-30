# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:50:32 2024

@author: Administrator
"""

''' 
- TUPLE LÀ LIST CỐ ĐỊNH: 
    CÓ THỨ TỰ
    GIÁ TRỊ TRÙNG LẶP
    KHÔNG THỂ CẬP NHẬT, THÊM HAY XÓA

- TUPLE ĐƯỢC DÙNG ĐỂ BẢO VỆ DỮ LIỆU & NHANH HƠN LIST 
  VÌ CHÚNG KHÔNG THỂ THAY ĐỔI TỰ ĐỘNG

- TRONG TUPLE CÓ THỂ CHỨA LIST, TUPLE, SET
 
'''

gioiTinh = ('Nam','Nữ')
lopHoc = (1,2,3,4,5,6,7,8,9,10,11,12)
traiCay = ('Táo','Chuối','Cam','Táo','Mận','Dưa hấu')

# CHỌN
print ('chọn 1 theo vị trí: ',gioiTinh[0])
print ('chọn dãy theo vị trí: ',traiCay[0:4])

# KHÔNG THỂ THAY ĐỔI GIÁ TRỊ 
#lopHoc[0] = 13 # error


# CỘNG TUPLE
y = gioiTinh + lopHoc
print(y)

# LẶP 
y = gioiTinh * 4
print(y)

# KIỂM TRA TỒN TẠI
print('Kiểm tra tồn tại: ','Táo' in traiCay)
print('Kiểm tra tồn tại: ','Dưa' in traiCay)

# DUYỆT PHẦN TỬ = FOR
for i in traiCay:
    print('Duyệt phần tử = for: ',i)

# LEN
print('LEN:',len(traiCay))

# COUNT
print('COUNT:',traiCay.count('Táo'))

# INDEX('VALUE',START,END)
print('INDEX:',traiCay.index('Táo'))
print('INDEX:',traiCay.index('Táo',2))
# nên dùng if ... in để ktra sự tồn tại nếu không sẽ error


# MIN,MAX,SUM : KHI CÁC PHẦN TỬ CÙNG KIỂU DỮ LIỆU
print(min(lopHoc))
print(max(lopHoc))
print(sum(lopHoc))
print(min(traiCay))
print(max(traiCay))



'''
KHÔNG DÙNG SORT ĐƯỢC VÌ KHI SORT TUPLE PHẢI THAY ĐỔI VỊ TRÍ
MÀ MỖI VỊ TRÍ TRONG TUPLE ĐÃ ĐƯỢC CỐ ĐỊNH VÀ KHÔNG THỂ THAY ĐỔI
NÊN PHẢI DÙNG SORTED ĐỂ TẠO RA 1 LIST MỚI

TƯƠNG TỰ REVERSE
'''

# SORTED
sortedTC = sorted(traiCay) # SORT SẼ TẠO 1 LIST MỚI
print('Sorted tuple tạo thành list mới: ',sortedTC)
print(type(sortedTC))


# TUPLE(REVERSED())
x = (4,5,9,1,0)
reversed_x = tuple(reversed(x))
print(x)
print('Reversed tuple tạo thành 1 tuple mới:',reversed_x)

# ĐỔI TỪ LIST, SET, STR SANG TUPLE
tupleTC = tuple(sortedTC) # LẠI TẠO THÀNH 1 TUPLE MỚI
print('Đổi từ List sang Tuple: ',tupleTC)
print(type(tupleTC))

# XÓA TUPLE
#del tuple_name
