# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:08:51 2024

@author: Administrator
"""

'''
CHUYỂN ĐỔI LIST, TUPLE, SET SANG DICT

'''

# LIST SANG DICT
list1 = [[1,'a'],[2,'b']]  # list chứa list
dict1 = dict(list1)
print('LIST -> DICT USING []:',dict1)

list2 = [(1,'a'),(2,'b')]  # list chứa tuple
dict2 = dict(list2)
print('LIST -> DICT USING ():',dict2)

list3 = [{1,'a'},{2,'b'}]  # list chứa set
dict3 = dict(list3)
print('LIST -> DICT USING {}:',dict3)


print('')
# TUPLE SANG DICT
tuple1 = ([1,'a'],[2,'b']) # tuple chứa list
dict4 = dict(tuple1)
print('TUPLE -> DICT USING []:',dict4)

tuple2 = ((1,'a'),(2,'b')) # tuple chứa tuple
dict5 = dict(tuple2)
print('TUPLE -> DICT USING ():',dict5)

tuple3 = ({1,'a'},{2,'b'}) # tuple chứa set
dict6 = dict(tuple3)
print('TUPLE -> DICT USING {}:',dict6)


print('')
# SET SANG DICT
# set không thể chứa mutable (list,set)
set1 = {(1,'a'),(2,'b')} # set chứa tuple
dict7 = dict(set1)
print('SET -> DICT ONLY USING ():',dict7)


print('')
# DICT SANG LIST, TUPLE, SET : CHỈ LẤY ĐƯỢC KEY
list4 = list(dict1)
print('DICT -> LIST:',list4)

tuple4 = tuple(dict7)
print('DICT -> TUPLE:',tuple4)

set2 = set(dict2)
print('DICT -> SET:',set2)



print('')
'''
x = dict.fromkeys(y, 'value'):
    dùng khi muốn nhiều key dùng chung 1 value
    dùng khi key có không có value
    
'''

x1 = {'giám đốc','thư ký', 'nhân viên'}
z = {'Mạnh', 'Huy'} # list, tuple, set đều được
y1 = dict.fromkeys(x1,z)
y2 = dict.fromkeys(x1)
print(y1)
print(y2)

x2 = ('giám đốc','thư ký', 'nhân viên')
y3 = dict.fromkeys(x2,z)
print(y3)

x3 = ['giám đốc','thư ký', 'nhân viên']
y4 = dict.fromkeys(x3,z)
print(y4)


















