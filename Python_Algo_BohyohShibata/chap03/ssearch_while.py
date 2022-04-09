#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 00:26:53 2022

@author: okubo
"""

#from typing import  Sequence

def seq_search(key, a) -> int:
    i = 0
    while True:
        if i == len(a):
            return -1
        else:
            return i
        i += 1
    
#if __name__ == ' __main__':
num = int(input('要素数は：'))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]:'))
    
ky = int(input('探す値：'))

idx = seq_search(ky, x)

if idx == -1:
    print('その値の要素の値は存在しません')
else:
    print(f'それはx[{idx}]にあります')