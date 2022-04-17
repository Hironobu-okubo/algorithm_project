#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 00:00:58 2022

@author: okubo
"""

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1],a[j] = a[j],a[j - 1]

if __name__ == '__main__':
    num = int(input('要素数：'))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'a[{i}]:'))
    bubble_sort(x)
    
    print(x)
        