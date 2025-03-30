# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:31:48 2024

@author: Administrator
"""

import random

#
def create_array(n):
    array = []
    for i in range(n):
        num = random.randint(0  ,100)
        array.append(num)
    return array

#
def bubble_sort(array):
    n = len(array)
    print('STEPS:') 
    for index in range(n): # array = [0, ... n-1]
        continue_to_sort = False
        
        for j in range (n-2, index-1, -1): # array [i, ... n-2, n-1]
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                continue_to_sort = True # nếu có sự thay đổi vị trí trong 1 vòng lặp j 
            else:
                pass # sẽ không thay đổi vị trí và chạy vòng lặp j kế tiếp
        # sẽ chạy hết tất cả vòng lặp j r mới đến vòng lặp i kế tiếp
        
        if continue_to_sort == False: # nếu KHÔNG có sự thay đổi vị trí trong 1 vòng lặp j
            break
            
        print(index+1, ':', array)

#    
def main():
    array = create_array(5)
    print('ORIGINAL ARRAY:\n', array)
    print()
    
    bubble_sort(array)

    
#
if __name__ == '__main__':
    main()

                
        