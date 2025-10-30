# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:28:49 2024

@author: Administrator
"""

class sinhVien:
    def __init__(self, hoTen, mssv):
        self.name = hoTen
        self.mssv = mssv
    def diem_tb (self,*a):  
        if len(a) == 0:
            dtb = 0
        else:
            tong = 0
            for i in a:
                tong = tong + i
            dtb = tong / len(a)
            return dtb
    
sv1 = sinhVien('mạnh',456)
print(sv1.name)
print(sv1.mssv)

a = sv1.diem_tb()
print(a)

b = sv1.diem_tb(1,2,3)
print(b)


'''
Xây dựng class Ngay gồm các attributes : ngày, tháng, năm
Xây dựng các methods:
    cho biết ngày đó là ngày thứ bao nhiêu trong năm
    static method: cho biết tháng đó có bao nhiêu ngày
    
'''

class date:
    def __init__(self, ngay,thang,nam):
        self.day = ngay
        self.month = thang
        self.year = nam
    
    @staticmethod
    def soNgayTrongThang(thang,nam): # staticmethod không cần self
        if thang in (1,3,5,7,8,10,12):
            return 31
        elif thang in (4,6,9,11):
            return 30
        else:
            if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
                return 29
            else:
                return 28
            
    def ngayTrongNam(self):
        ngayTrongNam = 0
        # Tính tổng số ngày các tháng trước
        for i in range (1,self.month):
            ngayTrongNam += self.soNgayTrongThang(i, self.year)
        # Tính số ngày của tháng hiện tại
        ngayTrongNam += self.day
        return ngayTrongNam



date1 = date(15,3,2022)

# static method k cần object
x = date.soNgayTrongThang(1, 2024)
print(x)

#
y = date1.ngayTrongNam()
print(y)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            