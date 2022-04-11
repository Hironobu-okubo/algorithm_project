#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:37:14 2022

@author: okubo
"""
import hashlib

class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity
    
    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16) % self.capacity)
    