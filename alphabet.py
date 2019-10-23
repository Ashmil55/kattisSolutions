#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:27:46 2019

@author: ashmil
"""

word = raw_input()

print word.index(min(word))

word = word[word.index(min(word)):]


print word


s1 = []

o = raw_input()

for i in range(o) :
    if o[i+1] > o[i]:
        pass
    else :
        s1.append(o.pop)



o = "ggt"
print o.remove('t')