import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pickle

#Import dict serially from the pickle
with open('readings.pickle', 'rb') as f: 
    dictCount = pickle.load(f)
    alcDictList = pickle.load(f)
    conDictList = pickle.load(f)
    readingsdfL = pickle.load(f)
    
#using one dictionary for simplicity
readingsDict = alcDictList[0]

#using one dataframe for simplicity
readingsdf = readingsdfL[0]
    
#_____________________plotting_________________________    
#using pandas visualisation 
#all recordings of one channel
readingsdf.plot(y='OZ')

#plotting all recordings of 3 channels
readingsdf.plot(y=['OZ','P6'])
#____________________________________________________________________
#creating dataframe with just avg values
avgdf = readingsdf.mean()
avgdf = avgdf.to_frame(name=None)

#density plot
avgdf.plot.kde()

tempdf = readingsdf.drop('category',1)

#area plot
readingsdf.plot.area(stacked=False)

#heatmap for avg values
ax = sns.heatmap(avgdf, linewidths=.25)

#heat map for all readings
sns.heatmap(tempdf)

#cluster map
sns.clustermap(tempdf)

#histogram plot
readingsdf.hist()
#____________________3D plot 1 ___________________________

x = np.arange(len(tempdf.columns))
y = tempdf.index
X,Y = np.meshgrid(x,y)
Z = tempdf
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
