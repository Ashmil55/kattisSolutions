#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:26:08 2019

@author: ashmil
"""

i,j = raw_input().split()

i,j = int(i),int(j)

if pow(2,j) >= i :
    print "Your wish is granted!"
else :
    print "You will become a flying monkey!"