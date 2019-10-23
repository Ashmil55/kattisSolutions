#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:10:23 2019

@author: ashmil
"""

origStack = []

n = input()

origStack = raw_input().split()
#origStack = int(origStack)

#print origStack

auxStack = []
#auxStack.append(origStack.pop())
#count = 0
for i in range(2*n):
    if (len(auxStack) == 0) and (len(origStack) > 0):
        auxStack.append(origStack.pop())
#        count = count + 1
        
    elif (origStack[len(origStack)-1] == auxStack[len(auxStack)-1]) :
        origStack.pop()
        auxStack.pop()
#        count = count+1
    else :
        auxStack.append(origStack.pop())
#        count = count + 1
#    print origStack
#    print auxStack
if ((len(origStack) == 0) and (len(auxStack) == 0)):
    print 2*n
else :
    print "impossible"
        
