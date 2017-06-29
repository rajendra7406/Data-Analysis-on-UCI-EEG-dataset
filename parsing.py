# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:41:35 2017

@author: Chaitra
"""

import pickle  
fo = open('co2a0000364.rd.000')
count = 4
while (count>0):
    print(fo.readline())
    count=count-1;

m=[]

for channels in range(1,65):
    for readingCount in range(1,258):
        readingValue = fo.readline().split()
        m.append(readingValue)
            
        
    
    
