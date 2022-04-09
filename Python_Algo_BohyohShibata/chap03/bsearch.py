#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:57:22 2022

@author: okubo
"""
from typing import Sequence 

def bin_search(key, a: Sequence) -> int:
    left = 0
    right = len(a) - 1
    
    while True:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            left = mid + 1
        else:
            right = mid -1
        if left > right:
            break
    return -1
    
    
if __name__ == '__main__':
    
    num = int(input('要素数：'))
    x = [None] * num
    
    print('昇順に入力して下さい')
    
    x[0] = int(input('x[0]:'))
    
    for i in range(1,num):
        while True:
            x[i] = int(input(f'x[{i}]:'))
            if x[i] >= x[i - 1]:
                break
    ky = int(input('探す値：'))
    
    idx = bin_search(ky, x)
    
    if idx == -1:
        print('その値は存在しません')
    else:
        print(f'その値はx[{idx}]にあります')