# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:20:06 2024

@author: Administrator
"""
'''
lIST:
    CÓ THỨ TỰ
    CÓ THỂ THAY ĐỔI
    PHẦN TỬ CÓ THỂ TRÙNG NHAU
    CÁC PHẦN TỬ CÓ THỂ KHÔNG CÙNG LOẠI, CÓ THỂ LÀ SET, LIST, TUPLE

TRONG LIST CÓ THỂ CHỨA LIST, SET, TUPLE
'''

# TẠO 1 LIST RỖNG
emptyList1 = []
emptyList2 = list()
print(emptyList1)
print(emptyList2)


# TẠO 1 LIST CÓ DỮ LIỆU, VỊ TRÍ ĐƯỢC ĐÁNH DẤU TỪ 0 TỪ TRÁI -> PHẢI
studentList = ['An','Bình','Ngân','Vy']
number=[3,5,7,23,7,32,65,7]


# CHỌN TẤT CẢ
print('chọn tất cả: ',studentList)

# CHỌN 1 NGƯỜI THEO VỊ TRÍ
print('chọn vị trí 2: ',studentList[2])
print('chọn vị trí 0: ',studentList[0])

# CHỌN DÃY NGƯỜI TRONG KHOẢNG [x,y)
print('chọn vị trí >=1 và < 2: ', studentList[1:2])
print('chọn vị trí >=0 và < 3: ',studentList[0:3])

# CHỌN PHẦN TỬ TRONG 1 TẬP HỢP TRONG LIST
# print(list_name[][])

# CỘNG LIST
x = studentList + number # chỉ được cộng 2 list với nhau
print('CỘNG LIST:',x)

# LẶP LIST
x = studentList*2
print('LẶP LIST:',x)

# MIN, MAX, SUM : CÁC PHẦN TỬ PHẢI CÙNG LOẠI
print('MIN:',min(number))
print('MAX:',max(number))
print('SUM:',sum(number)) # với số



# DUYỆT PHẦN TỬ TRONG LIST = FOR
for i in studentList:
    print('DUYỆT = FOR:',i)

print('')

for i in range(len(studentList)):
    print('DUYỆT = FOR:',studentList[i])
    


# ADD DỮ LIỆU VÀO CUỐI LIST
studentList.append('Thiên')
print('APPEND:',studentList)
print('TỔNG SỐ LƯỢNG ELEMENTS:',len(studentList))

studentList[len(studentList):] = ['Thành']
print('THÊM VÀO CUỐI LIST = LEN: ',studentList)


# ADD DỮ LIỆU VÀO VỊ TRÍ BẤT KÌ TRONG LIST
studentList.insert(2,'Ngọc') 
print('INSERT 2: ',studentList)
studentList.insert(4,'Trang')
print('INSERT 4: ',studentList)
studentList.insert(1,'Trang')
print('INSERT 1: ',studentList)



# COUNT('VALUE')
print ('COUNT:',studentList.count('Ngọc'))
    
# INDEX('VALUE',START,END)
print('INDEX:',studentList.index('Ngọc'))
# studentList.index('Thanh') # index phần tử không có trong list --> error
# kiểm tra nếu có --> no error
if 'Thanh' in studentList:
    print(studentList.index('Thanh')) 



# XÓA PHẦN TỬ = GIÁ TRỊ
studentList.remove('Ngân')
print('REMOVE:',studentList)

# nếu có phần tử trùng nhau thì xóa phần tử đầu tiên từ trái sang phải
studentList.remove('Trang')
print('REMOVE DUPLICATE VALUE:',studentList)

# studentList.remove('Kate') # remove phần tử không có trong list --> error
# kiểm tra nếu có --> no error
if 'Kate' in studentList:
    studentList.remove('Kate')
    print(studentList)



# XÓA PHẦN TỬ = VỊ TRÍ
popped = studentList.pop(0)
print('ELEMENT BỊ POP: ',popped) # khác del vì có thể trả về giá trị bị xóa
print('POP:',studentList)

del studentList[-1]
print('DEL:',studentList)


print('------------------')
# UPDATE DỮ LIỆU
thislist = ["apple", "banana", "cherry"]
print('thislist:',thislist)
thislist[1] = "blackcurrant"
print('update vị trí 1:',thislist)

thislist[1:3] = ["grape", "watermelon"]
print('update vị trí 1 đến 2:',thislist)

thislist[1:2] = ["blackcurrant", "watermelon1"]
print('update vị trí 1 với 2 value:',thislist)

thislist[1:3] = ["lemon"]
print('update vị trí 1,2 với 1 value:',thislist)



print('----------------')
# ĐẢO NGƯỢC LIST
studentList.reverse()
print('REVERSE:',studentList)


# SẮP XẾP LIST : CHỈ SORT ĐƯỢC KHI CÁC PHẦN TỬ CÙNG KIỂU
# SORT(KEY=..., REVERSE=TRUE/FALSE)
studentList.sort() # reverse = False
print('SORT TĂNG DẦN:',studentList)
studentList.sort(reverse=True)
print('SORT GIẢM DẦN:',studentList)


# EXTEND: THÊM VÀO CUỐI LIST 1 TẬP HỢP LIST, TUPLE, SET
number={3,5,7,23,7,32,65,7}
studentList.extend([number]) # [] thể hiện tập con trong list, có thể bỏ
print('EXTEND:', studentList)

# COPY TẠO THÀNH 1 LIST MỚI
y = studentList.copy()
print('COPY:',y)

# LÀM RỖNG LIST
studentList.clear()
print('original list: ',studentList)
print('copied list:',y)

# XÓA LIST
del studentList
#print(studenList) # error vì đã bị del







