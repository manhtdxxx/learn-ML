# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 12:14:55 2024

@author: Administrator
"""

'''
HÀM LÀ 1 KHỐI MÃ VÀ CHỈ ĐƯỢC CHẠY KHI NÓ ĐƯỢC GỌI
CÓ THỂ TRUYỀN DỮ LIỆU/THAM SỐ VÀO 1 HÀM
KẾT QUẢ LÀ 1 HÀM CÓ THỂ TRẢ VÈ DỮ LIỆU

'''

# KHAI BÁO HÀM
def xinChao():
    print('Xin chào!')
# GỌI HÀM
xinChao()

# HÀM CÓ THỂ NHẬN ĐỐI SỐ (ARGUMENT)
def xinChao(hoVaTen):
    print('Xin chào',hoVaTen)
    print('Xin chào ' + hoVaTen)

xinChao('Trần Đức Mạnh')

# HÀM CÓ THỂ NHẬN NHIỀU ĐỐI SỐ
def xinChao (ho,dem,ten):
    print('Xin chào ' + ho + dem + ten)

xinChao('Trần ','Đức ','Mạnh') # viết theo thứ tự
xinChao(ten='Mạnh',ho='Trần ',dem='Đức ') # không theo thứ tự thì gọi tên argument


print('')
# NẾU KHÔNG XÁC ĐỊNH ĐƯỢC SỐ LƯỢNG ARGUMENTS THÌ THÊM DẤU * OR ** TRƯỚC ARGUMENT
# XÁC ĐỊNH = VỊ TRÍ (*)
def thoiKhoaBieu(*monHoc): # * thể hiện monHoc là 1 tuple including elements
    print('Môn 1: ' + monHoc[0])
    print('Môn 2: ' + monHoc[2])
    print('Môn 3: ' + monHoc[3])

thoiKhoaBieu('Toán','Lý','Hóa','Anh')


print('')
# NẾU KHÔNG XÁC ĐỊNH ĐƯỢC SỐ LƯỢNG ARGUMENTS THÌ THÊM DẤU * OR ** TRƯỚC ARGUMENT
# XÁC ĐỊNH = TÊN (**)
def xinChao(**hoVaTen):
    print(hoVaTen['ho'])
    print(hoVaTen['dem'])
    print(hoVaTen['ten'])

xinChao(ten='Tùng',dem='Nhật',ho='Lê')


print('')
# WITHOUT RETURN
def tinhTich(*value):
    tich = 1
    for i in value:
        tich = tich * i
    print ('Tích các số trong ():', tich)

tich1 = tinhTich(1,30,5)
print(tich1) # None do vậy cần dùng return để hiển thị KQ
print(type(tich1))


print ('')
# RETURN ĐỂ TRẢ VỀ GIÁ TRỊ
# CÁC CÂU LỆNH PHÍA DƯỚI RETURN SẼ KHÔNG ĐƯỢC THỰC HIỆN
def tinhTich(*value):
    tich = 1
    for i in value:
        tich = tich * i
    return tich

tich1 = tinhTich(1,30,5)
print('Tích các số trong ():',tich1)
print(type(tich1)) # returns class int
tich2 = tinhTich(1,2,5)
print('Tích các số trong ():',tich2)
tong = tich1 + tich2
print('Tổng các tích:',tong)



print('')
'''
TÌM USCLN (greatest common division) CỦA A,B:
CÁCH GIẢI:
    LẤY SỐ LỚN HƠN TRỪ ĐI NHỎ HƠN CHO ĐẾN KHI 2 SỐ BẰNG NHAU
    THÌ ĐÓ LÀ GCD CỦA A,B
VD: GCD(35,77) = 7
    77 - 35 = 42 = b
    42 - 35 = 7 = b
    35 - 7 = 28 = a
    28 - 7 = 21 = a
    21 - 7 = 14 = a
    14 - 7 = 7 = a = b

'''
def gcd(a,b):
    while a!=b:
        if a>b:
            a = a - b 
        else:
            b = b - a
    return a

x = gcd(44,687687)
print('Ứớc số chung lớn nhất của:', x)



print('')
'''
HÀM ĐỆ QUY (RECURSION):
    a function returns itself 
    but mức độ đơn giản hơn
    and lặp lại cho đến khi đơn giản nhất

ƯU ĐIỂM:
    MÃ GỌN HƠN
NHƯỢC ĐIỂM:
    KHÓ THEO DÕI LOGIC
    KHÓ GỠ RỐI
    TỐN BỘ NHỚ (VÌ LẶP LẠI)
    
'''

def giai_thua(n):
    if n == 1:
        return 1
    else:
        return n * giai_thua(n-1)

print('GIAI THỪA:',giai_thua(3))

# ĐẶT LIMIT
import sys
sys.setrecursionlimit(50000) # set 5000 thì n max = 1558

print('GIAI THỪA:',giai_thua(1558))

    






















