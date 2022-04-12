#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 02:33:51 2022

@author: okubo
"""

def reverse_array(a):
    n = len(a)
    for i in range(n // 2):
        a[i],a[n - i - 1] = a[n - i - 1],a[i]
    
if __name__ == '__main__':
    print('配列の最大数を求める')
    num = int(input('要素数'))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))
    
    reverse_array(x)
    
    print('配列の要素の並びを反転しました。')
    for i in range(num):
        print(x[i])
        