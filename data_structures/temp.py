#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:20:33 2021

@author: sha
"""

def recursion(n):
    while n<=1:
        return 1
    return n+recursion(n-1)
    
ans=recursion(6)