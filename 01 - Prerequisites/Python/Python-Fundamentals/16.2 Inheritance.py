# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:52:46 2024

@author: Administrator
"""
'''
INHERITANCE:
    KHI KẾ THỪA PHẢI CHỈ RÕ TÊN CHA:
        class subClass_name (class_name)
    DÙNG super().function_name() ĐỂ KẾ THỪA

'''

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


class sinhVien_db(sinhVien):
    def __init__(self, hoTen, mssv, ngaySinh, gioiTinh):
        super().__init__(hoTen, mssv)
        self.birth = ngaySinh
        self.sex = gioiTinh
        
    def diem_tb (self,*a):  
        return super().diem_tb(*a)
        
    def diemTong(self,*b):
        tong = 0
        for i in b:
            tong = tong + i
        return tong
            

svdb1 = sinhVien_db('Tran Duc Manh', 123, '15-10-2004', 'nam')
print(svdb1.birth)
print(svdb1.mssv)

x = svdb1.diem_tb(1,2,3)
print(x)

y = svdb1.diemTong(1,2,3)
print(y)
        
z = svdb1.diem_tb()
print(z)
        
   
print('')
###
class animal:
    def __init__(self,kind,name,width,height,weight):
        self.kind = kind
        self.name = name
        self.width = width
        self.height = height
        self.weight = weight
    def makeVoice(self):
        print('Unknown Voice')
    def printMe(self):
        print('type:{},name:{},width:{},height:{},weight:{}'.format(self.type,self.name,self.width,self.height,self.weight))
    

class dog(animal):
    def __init__(self,name,width,height,weight,isChampion):
        # kế thừa
        animal.__init__(self, 'Dog', name, width, height, weight)
        # thuộc tính riêng
        self.ischampion = isChampion
    # override method
    def makeVoice(self):
        print('{}: gogo'.format(self.name))
    def printMe(self):
        print('name: {}, width: {}, height: {}, weight: {}'.format(self.name,self.width,self.height,self.weight))
    # method riêng
    def guardHome(self):
        print('{}: zzzzZZZZ'.format(self.name))
    


dog1 = dog('Cậu Vàng','80cm','40cm','20kg',True)

dog1.printMe()
dog1.makeVoice()
dog1.guardHome()

        
        
        
        
        
        
        
        
        
        
        