#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 05:57:22 2022

@author: okubo
"""

from typing import Sequence

def max_of(a: Sequence) -> int:
    maximum = a[0]
    for i in range(len(a)):
        if maximum < a[i]:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('配列の最大数を求める')
    num = int(input('要素数'))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))
    
    print(f'最大値は{max_of(x)}')
    