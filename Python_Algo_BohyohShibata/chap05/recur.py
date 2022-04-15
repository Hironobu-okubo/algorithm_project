#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:03:53 2022

@author: okubo
"""

def recur(n):
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)
    
n = int(input('整数を入力せよ：'))
recur(n)