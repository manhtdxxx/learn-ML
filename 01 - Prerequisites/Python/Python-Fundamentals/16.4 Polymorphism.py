# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 23:09:03 2024

@author: Administrator
"""

'''
POLYMORPHISM:
    DÙNG CHO NHIỀU HÀM THUỘC CÁC CLASS KHÁC NHAU CÓ CÁC CHỨC NĂNG KHÁC NHAU
    CÁC HÀM ĐÓ PHẢI CÙNG TÊN

'''


class sinhVien_nu:
    def __init__ (self,hoTen,mssv):
        self.name = hoTen
        self.mssv = mssv
    def xinChao(self):
        print('Xin chào, tôi là sinh viên nữ')
        
class sinhVien_nam:
    def __init__ (self,hoTen,mssv):
        self.name = hoTen
        self.mssv = mssv
    def xinChao(self):
        print('Xin chào, tôi là sinh viên nam')
    
def abc(sinhVien_nu):
    sinhVien_nu.xinChao()
    
sv1 = sinhVien_nam('Mạnh', '-')
sv1.xinChao()

sv2 = sinhVien_nu('Ngọc', 'mssv')
sv2.xinChao()

abc(sv1)
abc(sv2)
