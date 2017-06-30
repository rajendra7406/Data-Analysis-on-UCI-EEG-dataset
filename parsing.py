# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:41:35 2017

@author: Chaitra
"""

import pickle  
fo = open('co2a0000364.rd.000')

#file to be dumped to pickle
reading = {['name']:[]}

for count in range(1,5):
    print(fo.readline())

reading['name'] = 'raju'
reading['name'].append('raju2')
m=[]

for channels in range(1,65):
    for readingCount in range(1,258):
        readingValue = fo.readline().split()
        m.append(readingValue)
        reading['']

fo.close()            
        
    
    
