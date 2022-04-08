#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:52:44 2022

@author: okubo
"""

#固定長スタッククラス

class FixedStack:
    
    class Empty(Exception):
        pass
    
    class Full(Exception):
        pass
    
    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity  #スタック本体
        self.capacity = capacity      #スタックの容量
        self.ptr = 0                  #スタックポインタ
        
    def __len__(self) -> int:
        return self.ptr
    
    def is_empty(self) -> bool:
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        return self.ptr >= self.capacity
    
    