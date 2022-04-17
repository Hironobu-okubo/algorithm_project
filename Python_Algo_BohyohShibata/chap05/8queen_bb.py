#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:51:19 2022

@author: okubo
"""
pos = [0] * 3
flag = [False] * 3

def put():
    for j in range(3):
        for i in range(3):
            print('■' if pos[i] == j else '□', end = '')
        print()
    print()
            
    '''
    for i in range(3):
        print(f'{pos[i]}',end = ' ')
    print()
    '''

def set(i: int):
    for j in range(3):
        if not flag[j]:
            pos[i] = j
            if i ==  2:
                put()
            else:
                flag[j] = True
                set(i + 1)
                flag[j] = False

set(0)