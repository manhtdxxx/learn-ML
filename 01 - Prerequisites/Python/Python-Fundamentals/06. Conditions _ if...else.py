# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:24:48 2024

@author: Administrator
"""

'''
CÂU LỆNH RẼ NHÁNH IF ELSE
if [ĐK]:
    print()
elif [ĐK]:
    print()
else:
    print()
    
'''

# VD1
x = input('Nhập vào giá trị: ')
x = int(x)

if x%2==0:
    print(x, ' là số chẵn')
else:
    print(x, ' là số lẻ')
    
# VD2
if x>=9:
    print(x,' là học sinh xuất sắc')
elif x>=8:
    print(x,' là học sinh giỏi')
elif x>=7:
    print(x, ' là học sinh khá')
elif x>=5:
    print(x,' là học sinh trung bình')
else:
    print(x, ' là học sinh yếu')
   



print('-'*100)
'''
TOÁN TỬ ĐIỀU KIỆN
[trả về khi ĐK đúng] if [ĐK] else [trả về khi ĐK sai]

'''

x = int(input('Nhập vào x: '))
kq = 'là số chẵn' if (x%2==0) else 'là số lẻ'
print(x,kq)



'''
if statements cannot be empty, 
but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error

'''
a = 33
b = 200

if b > a:
    pass








