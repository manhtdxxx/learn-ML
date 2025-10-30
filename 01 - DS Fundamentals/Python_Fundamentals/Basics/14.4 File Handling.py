# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:34:38 2024

@author: Administrator
"""

'''
'''


f = open('.\\file_handling\\file4.txt', 'a+', encoding='utf-8')

# read when open
f.seek(0)  # cần seek về 0 vì file when open, pointer ở cuối
r = f.read()
print(r)
print('-'*100)


# no need seek as file pointer when write is always in the end
f.seek(0)
f.write('\nHôm nay trời nắng đẹp')

f.seek(0)
r = f.read()
print(r)
print('-'*100)


f.close()