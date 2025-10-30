# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:18:47 2024

@author: Administrator
"""

import numpy as np
import pandas as pd


#
np.random.seed(0)

sales_amounts = np.random.randint(0,20,(5,3))

weekly_sales = pd.DataFrame(sales_amounts, index=['Mon','Tue','Wed','Thu','Fri'],
                            columns=['Almond Butter','Peanut Butter','Cashew Butter'])
print(weekly_sales)
print(weekly_sales.shape)


print('-'*50)
#
prices = np.array([10,8,12]) # mảng 1 chiều
# DataFrame là 2 chiều nên cần reshape thành mảng 2 chiều chứa 1 mảng 1 chiều
butter_prices = pd.DataFrame(prices.reshape((1,3)), index=['Price'],
                             columns=['Almond Butter','Peanut Butter','Cashew Butter'])
print(butter_prices)
print(butter_prices.shape)


print('-'*50)
#
total_prices = weekly_sales.dot(butter_prices.T)
print(total_prices)
print()

weekly_sales['Total Price'] = total_prices
print(weekly_sales)









