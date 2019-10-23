#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:02:14 2019

@author: ashmil
"""

#converting long name format to short initials format


full_name = raw_input()

short_name = full_name[0]

for i in range(len(full_name)):
    if (full_name[i] == '-') :
        short_name  = short_name + full_name[i+1]
        

print short_name
