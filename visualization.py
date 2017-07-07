
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd #for dataframe
import numpy as np
import pickle

#Import file from the pickle
with open('readings.pickle','rb') as f:
    readingsDict = pickle.load(f)

readingCount = []
for i in range(1,257):
     readingCount.append(i)

channelCount = []
for key in readingsDict.keys():
    #storing keys as column names
    channelCount.append(key)

#creating dataframe
readingsDataframe = pd.DataFrame(index=readingCount, columns=channelCount)
#storing values in dataframe
for key in readingsDict.keys():
    #converting string values to float values in list
    temp = list(map(float, readingsDict[key]))
    #storing reading values to their respective columns 
    readingsDataframe[key] = temp

#_____________________plotting_________________________    
#all recordings of one channel
plt.xlabel('readings')
plt.ylabel('value count')
plt.plot(readingCount, readingsDict['OZ'], label='OZ channel')

#plotting all recordings of 3 channels
#x values, y values, color
OZ, = plt.plot(readingCount, readingsDict['OZ'], label='OZ channel')
P6, = plt.plot(readingCount, readingsDict['P6'], label='P6 channel')
AF2, = plt.plot(readingCount, readingsDict['AF2'], label='AF2 channel')
plt.xlabel('readings')
plt.ylabel('value count')
plt.legend(handles=[OZ, P6, AF2])

#____________________________________________________________________
#creating dataframe with just avg values
#creating one row for avg
index = []
index = [1]
avgReadingsDataframe = pd.DataFrame(index=readingCount, columns=channelCount)

#storing avg values in dataframe
for key in readingsDict.keys():
    #converting string values to float values in list
    temp = list(map(float, readingsDict[key]))
    #storing reading values to their respective columns 
    avgReadingsDataframe[key] = np.mean(temp)

#heatmap for avg values
ax = sns.heatmap(avgReadingsDataframe, linewidths=.25)

#________heat map for all readings______________________________________________
sns.heatmap(readingsDataframe)
#cluster map
sns.clustermap(readingsDataframe)

#____________________3D plot 1 ___________________________

x = np.arange(len(readingsDataframe.columns))
y = readingsDataframe.index
X,Y = np.meshgrid(x,y)
Z = readingsDataframe
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel('channel')
ax.set_ylabel('reading count')
ax.set_zlabel('voltage')

#____________________3D plot 2 ______________________________

from matplotlib import style
style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = []
y = []
z = []

for j in range(1,65):
    for i in range(1,257):
        x.append(j)
        y.append(i)
    
for key in readingsDict.keys():
    #converting string values to float values in list
    temp = list(map(float, readingsDict[key]))
    #appending values of single channel to yValues for plotting
    z.extend(temp)

ax1.scatter(x, y, z, c='g', marker='o')

ax1.set_xlabel('channel')
ax1.set_ylabel('reading count')
ax1.set_zlabel('voltage')

plt.show()
#_____________________end 3D plot_______________________________
