# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 02:45:18 2022

@author: vyoma
"""

import numpy as np

array_1 = np.array([1,2,3])
print(array_1)

#NumPy list advantage over array is that calc can be done over entire arrays

height = np.array([1.73])
weight = np.array([65.4])

bmi = weight / height ** 2
print(bmi)

#NumPy array contains only one type
#If different types, casted to string

array_2 = np.array([7, 1, 9, 2, 8, 3])
array_3 = array_2 > 5
print(array_3)

#To print greater than 5
print(array_2[array_3])

#When there are integer and boolean, bool true is 1, false is 0
array_4 = np.array([True, 1])
array_5 = np.array([2,3])
print(array_4 + array_5)

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball = np.array(baseball)

print(np_baseball.shape)

#Mean of a column in a numpy array. USe the numpy mean.
print(np.mean(np_baseball[:,0]))
print(np.median(np_baseball[:,0]))
print(np.std(np_baseball[:,0]))
#Correlation between the columns
print(np.corrcoef(np_baseball[:,0], np_baseball[:,1]))

#Since numpy single datatype, it's faster