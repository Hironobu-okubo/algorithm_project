#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 06:31:15 2022

@author: okubo
"""

import random
from max import max_of

print('乱数の最大値を求めます')
num = int(input('乱数の個数：'))
low = int(input('乱数の下弦：'))
high = int(input('乱数の上限：'))
x = [None] * num
for i in range(num):
    x[i] = random.randint(low,high)

print(f'{[x]}')
print(f'最大値は{max_of(x)}')
