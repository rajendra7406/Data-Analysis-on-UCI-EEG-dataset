from collections import defaultdict
import pickle  

#Opening the file 
filesList = ['co2a0000364.rd.000', 'co2a0000364.rd.002']
#creating dictionaries list
dictList= []
for files in filesList:
    dictName = files + '.dict'
    dictList.append(dictName)
    
for i in range(len(filesList)):
    fo = open(filesList[i])
    print(dictList[i])
    #defining the dict as defaultdict
    dictList[i] = defaultdict(list)
    #defining the temp defaultdict    
    tempDict = defaultdict(list)
    #skipping header lines
    for count in range(1,5):
        print(fo.readline())
    #looping from 6th line
    for channels in range(1,65):
        for readingCount in range(1,258):
            readingValue = fo.readline().split() 
            if readingCount!=1:
                tempDict[readingValue[1]].append(readingValue[3])
    dictList[i] = tempDict
    fo.close()

#pickling dictList 
with open('readings.pickle', 'wb') as f: 
    pickle.dump(len(dictList),f)
    pickle.dump(dictList,f)

