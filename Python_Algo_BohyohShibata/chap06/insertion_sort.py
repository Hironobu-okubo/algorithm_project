#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 07:31:49 2022

@author: okubo
"""

def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        tmp = a[i]
        j = i
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp
        
if __name__ == '__main__':
    n = int(input('要素数：'))
    x = [None] * n
    for i in range(n):
        x[i] = int(input(f'x[{i}]:'))
    insertion_sort(x)
    print(x)