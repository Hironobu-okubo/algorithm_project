#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 05:24:33 2022

@author: okubo
"""

count = 0
ptr = 0
prime = [None] * 168
prime[ptr] = 2
ptr += 1
prime[ptr] = 3
ptr += 1

for i in range(5,1001,2):
    n = 1
    while prime[n] * prime[n] <= i:
        count += 2
        if i % prime[n] == 0:
            break
        n += 1
    else:
        prime[ptr] = i
        ptr += 1
        count += 1
print(prime)
print(count)
    