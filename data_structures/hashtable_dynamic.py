#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hashing with probing
Created on Sun Aug  1 12:54:48 2021

@author: sha
"""

class Hashprobe:
    def __init__(self):
        self.max_length=10
        self.arr=[[] for i in range(self.max_length)]
        
    def hashing(self,key):
        val=0
        for char in key:
            val+=ord(char)
        return (val)%(self.max_length)
        
         
    def __setitem__(self,key,value):
        location=self.hashing(key)
        for i in range(location,self.max_length):
            if len(self.arr[i])!=0 and i!=9:
                if self.arr[i][0][0]==key:
                    self.arr[i][0]=(key,value)
                    break
                else:
                    continue
            elif i==9 and len(self.arr[i])!=0:
                if self.arr[i][0][0]==key:
                    self.arr[i][0]=(key,value)
                    break
                else:
                    for i in range(location):
                        if len(self.arr[i])!=0:
                            continue
                        else:
                            self.arr[i].append((key,value))
                            break
                        break
                        
            else:
                self.arr[i].append((key,value))
                break
    def __getitem__(self,key):
        location=self.hashing(key)
        if self.arr[location][0][0]==key:
            return self.arr[location][0][1]
        else:
            for i in range(self.max_length):
                if self.arr[i][0][0]==key:
                    return self.arr[location][0][1]


hp=Hashprobe()

hp['march 6']=9
hp['march 7']=10
hp['march 17']=12
hp['march 6']=7

