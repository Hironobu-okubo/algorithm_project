#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 05:57:22 2022

@author: okubo
"""

from max import max_of

print('配列の最大値を求めます')


number = 0
x = []
while True:
    print('nで終了')
    s = input(f'x{[number]}:')
    if s == 'n':
        break
    x.append(int(s))
    number += 1

print(f'最大値は{max_of(x)}')
    