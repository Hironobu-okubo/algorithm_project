#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 06:45:57 2022

@author: okubo
"""
from typing import MutableSequence


def bubble_sort(a: MutableSequence):
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1,k,-1):
            if a[j - 1] > a[j]:
                a[j - 1],a[j] = a[j],a[j - 1]
                last = j
        k = last
                

if __name__ == '__main__':
    num = int(input('要素数：'))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'a[{i}]:'))
    bubble_sort(x)
    
    print(x)
        