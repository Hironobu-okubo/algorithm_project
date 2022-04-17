#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:38:19 2022

@author: okubo
"""

pos = [0] * 4

def put():
    for i in range(4):
        print(f'{pos[i]:2}',end = ' ')
    print()

def set(i: int):
    for j in range(4):
        pos[i] = j
        if i == 3:
            put()
        else:
            set(i + 1)
            
set(0)
