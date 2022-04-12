#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 05:04:31 2022

@author: okubo
"""

count = 0
ptr = 0
prime = [None] * 500
prime[0] = 2
ptr += 1

for i in range(3,1001,2):
    for j in range(1,ptr):
        count += 1
        if i % prime[j] == 0:
            break
    else:
        prime[ptr] = i
        ptr += 1
        print(prime)
        
print(f'除算を行った回数：{count}')