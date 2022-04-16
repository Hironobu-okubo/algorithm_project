#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:01:39 2022

@author: okubo
"""
def hanoi(start, goal, work,n):
    if n == 1:
        print(f'{start}から{goal}')
    if n >= 2:
        hanoi(start, work, goal,n - 1)
        hanoi(start, goal, work, 1)
        hanoi(work, goal, start, n - 1)
    
if __name__ == '__main__':
    n = int(input('円盤の枚数：'))
    hanoi(1,2,3,n)
