# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:47:40 2024

@author: Administrator
"""

import random

def create_array(n):
    array = []
    for i in range(n):
        num = random.randint(0  ,100)
        array.append(num)
    return array


def insertion_sort(array):
    n = len(array)
    