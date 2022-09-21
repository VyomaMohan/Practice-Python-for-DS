# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello world")

var1 = "testing"
print(type(var1))

pi_string = "3.14"
pi_float= float(pi_string)
print(type(pi_float))

#List can contain diff types
list_1 = ["cat", 3.14, True]
print(list_1)

#for splicing, the end is exclusive
#start inclusive, end exclusive
list_2 = ["zero", "one", "two", "three", "four", "five", "six" ]
print(list_2[3:5])
#above gives only three, four
print(list_2[:4])
print(list_2[3:])

#Replace a set of values
list_3 = ["zero", "one", "two", "three", "four", "five", "six" ]
list_3[0:2] = ["test1", "test2"]
print(list_3)

#Add/Concat the lists
list_3 = list_3 + ["new val"]
print(list_3)

#Delete an element from list
del(list_3[0])
print(list_3)

#Equals sign copies the REFERENCE FOR THE LIST
list_4 = ["one", "two"]
list_5 = list_4
list_4[1] = "three"
print(list_5)

#To copy as SEPERATE lists have to use the list function
list_6 = ["one", "two"]
list_7 = list(list_6)
list_6[1] = "three"
print(list_7)