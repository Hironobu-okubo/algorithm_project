#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 02:51:05 2022

@author: okubo
"""

#読み込んだ10進数を2〜36進数に変換
#from typing import Int
def card_conv(num : int, base : int) -> str:
    result = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRTSUVWXYZ'
    
    while num > 0:
        result += dchar[num % base]
        num //= base
    return result[::-1]

if __name__ == '__main__':
    print('10進数を基数変換します')
    
    while True:
        num = int(input('変換する非負の整数：'))
        if num > 0:
            break
    
    base = int(input('何進数に変換しますか(2~36)：'))

    
    print(f'{base}進数では{card_conv(num,base)}です。')
    
        
        