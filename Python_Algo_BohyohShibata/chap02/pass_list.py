#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 04:49:49 2022

@author: okubo
"""

def change(lst, idx, val):
    lst[idx] = val

x = [11,22,33,44,55]
print(x)
index = int(input('インデックス：'))
value = int(input('新しい値：'))
change(x,index,value)
print(x)