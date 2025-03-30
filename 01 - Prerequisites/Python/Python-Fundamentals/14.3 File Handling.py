# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:34:38 2024

@author: Administrator
"""

'''
'''

# W+
f = open('.\\file_handling\\file3.txt', 'w+', encoding='utf-8')

# read when open
r = f.read()  # không đọc được gì vì lúc open đã bị xóa
print(r)
print('-'*100)


# write
f.seek(0)
f.write('ABCD -----------------------')

f.seek(0)
r = f.read()
print(r)
print(len('ABCD -----------------------'))
print('-'*100)


# write tiếp
f.seek(0)
f.write('OVERRIDING ***')

f.seek(0)
r = f.read()
print(r)
print(len('OVERRIDING ***--------------'))

print('-'*100)


f.close()
