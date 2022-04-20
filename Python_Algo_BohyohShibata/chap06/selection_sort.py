#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:36:18 2022

@author: okubo
"""
from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(0,n - 1):
            min = i
            for j in range(i + 1,n):
                if a[min] > a[j]:
                    min = j
            a[min], a[i] = a[i], a[min]
        

if __name__ == '__main__':
    n = int(input('要素数：'))
    x = [None] * n
    for i in range(n):
        x[i] = int(input(f'x[{i}]:'))
    selection_sort(x)
    print(x)
    