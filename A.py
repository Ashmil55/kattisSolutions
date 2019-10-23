#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:04:21 2019

@author: ashmil
"""

x,y = raw_input().split()

x,y = int(x), int(y)

if (x==0 and y==0) :
    print "Not a moose"

elif (x!=y):
    print "Odd ",2*(max(x,y))

else :
    print "Even ", 2*x
