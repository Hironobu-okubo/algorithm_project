#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 03:24:39 2022

@author: okubo
"""

def sum_1ton(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('xの値：'))
print(f'1から{x}までの総和は{sum_1ton(x)}')