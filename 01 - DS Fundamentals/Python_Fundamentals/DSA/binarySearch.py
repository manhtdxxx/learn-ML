# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:34:15 2024

@author: Administrator
"""

import random

def create_array_ascending (n):
    array = []
    first_num = random.randint(-100, 100)
    array.append(first_num)
    for i in range(n):
        step = random.randint(1, 10)
        next_num = array[i-1] + step
        array.append(next_num)
    array.sort()
    return array


def binary_search(array, x):
    left_index = 0
    right_index = len(array) - 1
    
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if array[middle_index] == x:
            return middle_index
        
        if x < array[middle_index]:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1
            
    return -1


def main():
    array = create_array_ascending(10)
    print(array)
    
    x = int(input('Nhập vào số nguyên cần tìm: '))
    
    index = binary_search(array, x)
    if index != -1:
        print(f'giá trị {x} được tìm thấy tại vị trí {index}')
    else:
        print(f'Không tìm thấy giá trị {x}')
        

if __name__ == '__main__':
    main()

