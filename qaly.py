#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:32:57 2019

@author: ashmil
"""



n = int(input())


constqual = 0
constperi = 0

qoly = 0

for i in range(n):
    constqual, constperi = raw_input().split() #raw_input because the input should be taken as string because it has space and \n
    
    qoly = qoly + float(constqual)*float(constperi)
    
print qoly
