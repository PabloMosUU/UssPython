#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:03:33 2022

@author: alpiz001


"""
#%% Lecture 4: maximum between three numbers
first = float(input("Enter first number:"))
second = float(input("Enter second number:")) 
third = float(input("Enter third number:")) 

if first > second:
    if first > third:
        print(f"{first} is the biggest number!")
    else:
        print(f"{third} is the biggest number!")
else:
    if second > third:
        print(f"{second} is the biggest number!")
    else:
        print(f"{third} is the biggest number!")
        
#%% Lecture 4: bitwise example
shelf = 8
if shelf & 1:
    print("ODD shelf -> go to the right!")
else:
    print("EVEN shelf -> go to the left!")
    
# bin(8) = 1000
# &           1
# =           0 

# bin(7) = 111
# &          1
# =          1 