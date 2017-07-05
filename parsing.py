

fo = open('co2a0000364.rd.000')

from collections import defaultdict
#defining dictionary

readingsDict = defaultdict(list)

my_list = [(1234, 100.23),(1234,123), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]



#skipping header lines
for count in range(1,5):
    print(fo.readline())

#looping from 6th line
for channels in range(1,65):
    for readingCount in range(1,258):
        readingValue = fo.readline().split() 
        if readingCount!=1:
            readingsDict[readingValue[1]].append(readingValue[3]) 
        

import pickle  
#dump readingsDict to pickle
with open('readings.pickle', 'wb') as f: 
    pickle.dump(readingsDict, f)

#closing the file
fo.close()            
        
    
    
