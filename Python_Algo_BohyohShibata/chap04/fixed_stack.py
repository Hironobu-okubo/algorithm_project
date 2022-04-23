#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 23:23:38 2022

@author: okubo
"""

class Fixedstack:
    """空のFixedStackに対してpopが呼び出された時"""
    class Empty:
        pass
    
    """満杯のFixedStackにたいしてpushが呼び出された時"""
    class Full:
        pass
    
    def __init__(self,capacity):
       self.stk = [None] * capacity
       self.capacity = capacity
       ptr = 0
       
    
    