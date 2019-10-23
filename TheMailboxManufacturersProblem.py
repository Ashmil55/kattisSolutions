#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:04:14 2019

@author: ashmil
"""

b1,b2,b3  = False, False, False


def maxcrackers(k,m):
    total = 0
    mini = 1
#    print k
#    print m 
#    print total
    if k==1 :
        total = (m*(m+1))/2
    else :
        while (mini < m) :    
            total = total+int((mini+m)/2)
            mini = int((mini+m)/2)
    
    return total

n = input() #n test cases

for i in range(n):
    k,m = raw_input().split()
    k,m = int(k), int(m)
#    print k 
#    print m 
    print maxcrackers(k,m)



    


