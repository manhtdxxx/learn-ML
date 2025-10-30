# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 10:01:17 2024

@author: Administrator
"""

a = {'a','b','c','d'}
b = {'c','d','e','f'}

# A.INTERSECTION(B) = A & B
c1 = a.intersection(b)
print('INTERSECTION:',c1)

# A.UNION(B) = A | B
c2 = a.union(b)
print ('UNION:',c2)

# A.DIFFERENCE(B) = A - B
c3 = a.difference(b)
print('A DIFFERENCE B:',c3)

c4 = b.difference(a)
print('B DIFFERENCE A:',c4)


# A.SYMMETRIC_DIFFERENCE(B) = A ^ B
c5 = a.symmetric_difference(b)
print('SYMMETRIC_DIFFERENCE:',c5)


print('-------------------------')
# A.DIFFERENCE_UPDATE(B) -> UPDATE SET A, GIỮ NGUYÊN SET B
a1 = {'a','b','c','d'}
b1 = {'c','d','e','f'}

d1 = a1.difference_update(b) # xóa đi những values ở set A trùng với values trong set B
print('..._UPDATE KHÔNG TẠO SET MỚI:',d1)
print('A DIFFERENCE_UPDATE B:',a1)

b1.difference_update(a) # xóa đi những values ở set B trùng với values trong set A
print('B DIFFERENCE_UPDATE A:',b1)


# A.INTERSECTION_UPDATE(B)
a2 = {'a','b','c','d'}

a2.intersection_update(b)
print('INTERSECTION_UPDATE:',a2)

# A.SYMMETRIC_DIFFERENCE_UPDATE(B)
a3 = {'a','b','c','d'}

a3.symmetric_difference_update(b)
print('SYMMETRIC_DIFFERENCE_UPDATE:',a3)



print('----------------------------------')
# ISDISJOINT
print(a.isdisjoint(b)) # vì có values chung là c,d

# ISSUBSET / ISSUPERSET
e = {1,2,3}
f = {1,2,3,4}

print(e.issubset(f))
print(f.issuperset(e))




