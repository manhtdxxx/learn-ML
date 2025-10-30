# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 21:52:37 2024

@author: Administrator
"""

import random

def create_array(n):
    array = []
    for i in range(n):
        random_int = random.randint(-100, 100)
        array.append(random_int)
    return array


def linear_search(array, x):
    n = len(array)
    for index in range(n):
        if array[index] == x:
            return index
    return -1


def main():
    array = create_array(10)
    print(array)
    
    x = int(input('Nhập vào số nguyên cần tìm: '))
    
    index = linear_search(array, x)
    if index != -1:
        print(f'giá trị {x} được tìm thấy tại vị trí {index}')
    else:
        print(f'Không tìm thấy giá trị {x}')
        

if __name__ == '__main__':
    main()
