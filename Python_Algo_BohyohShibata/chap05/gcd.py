#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:43:11 2022

@author: okubo
"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
if __name__ == "__main__":
    print('二つの整数の最大公約数を求める')
    a = int(input('整数：'))
    b = int(input('整数：'))
    print(f'最大公約数は{gcd(a,b)}')
    