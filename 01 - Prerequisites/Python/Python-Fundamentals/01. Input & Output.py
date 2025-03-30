# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


''' 

print(object(s), sep=seperator, end=end, file=file, flush = flush) 

- object(s): đối tượng, dữ liệu được xuất
- sep: ngăn cách
- end: kết thúc
- file: tập tin
- flush: đẩy dữ liệu

'''

print(print.__doc__)

# ; giữa 2 print để xuống dòng
print('Hello World');print(5)

print('Xin','Chào','TITV')

# ngăn cách = 1 kí tự
print('Xin','Chào','TITV',sep=',')

# không xuống dòng
print('Xin','Chào',end='...')
print('Mạnh')

# format function
print('Tên={}, Họ={}'.format(' Mạnh',' Trần'))

my_string = "{1} is a good option for beginners in {0}"
print(my_string.format("Edureka","Machine Learning"))

# Xuất dữ liệu với input
x = input('Họ: ')
y = input("Tên: ")
print('Họ={0};Tên={1}'.format(x,y))
print ('Xin chào',x,y)

