#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 04:57:03 2022

@author: okubo
"""

count = 0
for i in range(2,1001):
    for j in range(2,i):
        count += 1
        if i % j == 0:
            break
    else:
            print(i)
    

print(f'除算を行った回数：{count}')