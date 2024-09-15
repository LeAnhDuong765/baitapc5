# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:02:19 2024

@author: Student
"""
count = 0
n= int(input("Nhập vào số lần cần lập:"))
while (count < n):
    print("Lần lập thứ:", count + 1, "\tBien đếm:", count)
    count = count + 1
else:
    print("\tThuc hiện lệnh trong else, do:", 
          "\ncount =", count, "\nn=",n , 
          "\nbool(count<n)=",bool(count<n))