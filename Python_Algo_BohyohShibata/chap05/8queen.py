#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:01:57 2022

@author: okubo
"""

pos = [0] * 4
flag_a = [False] * 4
flag_b = [False] * 7
flag_c = [False] * 7

def put():
    for j in range(4):
        for i in range(4):
            print('■' if pos[i] == j else '□', end = '')
        print()
    print()
            
    '''
    for i in range(3):
        print(f'{pos[i]}',end = ' ')
    print()
    '''

def set(i: int):
    for j in range(4):
        if (not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + 4]):
                pos[i] = j
                if i ==  3:
                    put()
                else:
                    flag_a[j] = flag_b[i + j] = flag_c[i - j + 4] = True
                    set(i + 1)
                    flag_a[j] = flag_b[i + j] = flag_c[i - j + 4] = False

set(0)