# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:43:35 2024

@author: Administrator
"""

import random

def create_array(n):
    array = []
    for i in range(n):
        num = random.randint(0  ,100)
        array.append(num)
    return array


def selection_sort(array):
    n = len(array)
    print('STEPS:')
    for i in range (n-1):
        index_min = i
        
        # tìm index của số nhỏ nhất
        for j in range(i+1, n):
            if array[index_min] > array[j]:
                index_min = j

        # thay thế
        array[i], array[index_min] = array[index_min], array[i]
        
        print(i+1, '-', array)


#    
def main():
    array = create_array(5)
    print('ORIGINAL ARRAY:\n', array)
    print()
    selection_sort(array)

    
#
if __name__ == '__main__':
    main()