# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:31:58 2024

@author: Student
"""

x=float(input("Nhập giá trị:"))
while x not in range(-99,99):
    x=float(input("Nhập lại giá trị x:")) 
print("Giá trị đã nhập:",x)