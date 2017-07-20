#default dict used to create nested dictionaries
from collections import defaultdict
import pandas as pd
import pickle  

#getting the small set of files for data analysis
alcFiles = ['co2a0000364.rd.000', 'co2a0000364.rd.002']
conFiles = ['co2c0000337.rd.000','co2c0000337.rd.000']
#creating dictionaries list
alcDictList= []
conDictList= []

#appending 'dict' to dictionaries for easy recognition
for files in alcFiles:
    dictName = files + '.dict'
    alcDictList.append(dictName)

for files in conFiles:
    dictName = files + '.dict'
    conDictList.append(dictName)

#creating dictionaries from files list
for i in range(len(alcFiles)):
    fo = open(alcFiles[i])
    #defining the dict as defaultdict
    alcDictList[i] = defaultdict(list)
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
    alcDictList[i] = tempDict
    fo.close()
    
#creating dictionaries from files list
for i in range(len(conFiles)):
    fo = open(conFiles[i])
    #defining the dict as defaultdict
    conDictList[i] = defaultdict(list)
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
    conDictList[i] = tempDict
    fo.close()
#______________________________________________________________
#creating dataframes
#taking only one dictionary for simplicity
readingsDict = alcDictList[0] 
#creating index values for dataframe
readingCount = []
for i in range(1,257):
     readingCount.append(i)
     
#creating column values for dataframe
channelCount = []
#adding category column for future use
channelCount.append('category')
for key in readingsDict.keys():
    #storing keys as column names
    channelCount.append(key)

#creating dataframe
alcReadingsDataframe = pd.DataFrame(index=readingCount, columns=channelCount)
#storing values in dataframe
for key in readingsDict.keys():
    #converting string values to float values in list
    temp = list(map(float, readingsDict[key]))
    #storing reading values to their respective columns 
    alcReadingsDataframe[key] = temp
    alcReadingsDataframe['category']='alcohol'


#creating another dataframe
readingsDict = conDictList[0] 
conReadingsDataframe = pd.DataFrame(index=readingCount, columns=channelCount)
#storing values in dataframe
for key in readingsDict.keys():
    #converting string values to float values in list
    temp = list(map(float, readingsDict[key]))
    #storing reading values to their respective columns 
    conReadingsDataframe[key] = temp
    conReadingsDataframe['category']='control'

#creating lists of dictionaries and dataframes and meta info for easy pickling
readingsDataframeList = []
readingsDataframeList.append(alcReadingsDataframe)
readingsDataframeList.append(conReadingsDataframe)
#pickling
with open('readings.pickle', 'wb') as f: 
    pickle.dump(len(alcDictList),f)
    pickle.dump(alcDictList,f)
    pickle.dump(conDictList,f)
    pickle.dump(readingsDataframeList,f)
