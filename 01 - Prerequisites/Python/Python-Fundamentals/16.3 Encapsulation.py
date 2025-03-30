# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:05:33 2024

@author: Administrator
"""
'''
ENCASULATION:
    USING _ OR __ TO PROTECT SOME IMPORTANT PROPERTIES

'''


class sinhVien:
    def __init__(self, hoTen, mssv):
        self.name = hoTen
        self.mssv = mssv
        self.__diem_max = 10 # using _ or __ to encapsulate
        
    def diem_tb (self,*a):  
        if len(a) == 0:
            dtb = 0
        else:
            tong = 0
            for i in a:
                if i <= self.__diem_max:
                    tong = tong + i
                else:
                    print('ĐIỂM NHẬP > ĐIỂM MAX')
                    return  
            dtb = tong / len(a)
            return dtb
    
    def set_diem_max(self,new_diem_max):
        self.__diem_max = new_diem_max
        
    
#
sv1 = sinhVien('Trần Đức Mạnh', 123)
print(sv1,'\n')

x = sv1.diem_tb(1,9)
print(x,'\n')

y = sv1.diem_tb(1,11)
print(y,'\n')

#
sv1.set_diem_max(20)

x = sv1.diem_tb(1,19)
print(x,'\n')

y = sv1.diem_tb(1,21)
print(y,'\n')

