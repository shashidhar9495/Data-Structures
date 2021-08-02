#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stacking

Created on Sun Aug  1 16:49:48 2021

@author: sha
"""

from collections import deque


my_dict={'}':'{',']':'[',')':'('}
        
def is_balanced(paranthesis):
    demo='{}[]()'
    req_par=deque()
    for i in range(len(paranthesis)):
        l=paranthesis.pop()
        if l in demo:
            req_par.append(l)
        else:
            pass
    req_par=req_par 
    print(req_par)
    if len(req_par)%2!=0:
        return False
    else:
        k=len(req_par)//2-1
        for i in range(len(req_par)//2):
            if req_par[i] ==')' or req_par[i] ==']' or req_par[i] =='}':
                if my_dict[req_par[i]]==req_par[len(req_par)-i-1]:                    
                    if i==k:
                        return True
                    else:
                        continue
                else:
                    return False
            else:
                return False
        

val=deque('({a+b})')

req=is_balanced(val)