
import numpy as np
import pickle
#Import file from the pickle
with open('readings.pickle','rb') as f:
    readingsDict = pickle.load(f)

readingCount = []
for i in range(1,257):
     readingCount.append(i)

import matplotlib.pyplot as plt
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

#plotting mean of all recordings of 64 channels
#iterating through keys in list
avgValues = []
for key in readingsDict.keys():
    #converting string values to float values in list
    temp = list(map(float, readingsDict[key]))
    #taking mean of all values from one channel
    avg = np.mean(temp)
    #appending mean value of single channel to yValues for plotting
    avgValues.append(avg)

#plotting
channelCount = []
for i in range(1,65):
     channelCount.append(i)

plt.xlabel('channel count')
plt.ylabel('avg of all readings in single channel')
plt.plot(channelCount, avgValues, label='avg values')


import seaborn as sns
uniform_data = [avgValues]
ax = sns.heatmap(uniform_data, linewidth = 2)

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
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

'''
#experimentation
from __future__ import print_function

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import time


def generateVoltage(X, Y):
    '''
   # Generates Z data(voltage) for the points in the X(channelCount), Y() meshgrid and .
    '''
    print(X)
    return X


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make the X, Y meshgrid.
timeSplit = np.linspace(0,1,256)
X, Y = np.meshgrid(channelCount, timeSplit)

# Set the z axis limits so they aren't recalculated each frame.
ax.set_zlim(-64, 64)

# Begin plotting.
wframe = None
tstart = time.time()
for phi in range(1,13):
    print(phi)
    # If a line collection is already remove it before drawing.
    if wframe:
        ax.collections.remove(wframe)

    # Plot the new wireframe and pause briefly before continuing.
    Z = generateVoltage(X, Y)
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)

print('Average FPS: %f' % (100 / (time.time() - tstart)))

"""
Demonstrates using custom hillshading in a 3D surface plot.
"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cbook
from matplotlib import cm
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt
import numpy as np

filename = cbook.get_sample_data('jacksboro_fault_dem.npz', asfileobj=False)
a = np.load(filename)
with np.load(filename) as dem:
    z = dem['elevation']
    nrows, ncols = z.shape
    x = np.linspace(dem['xmin'], dem['xmax'], ncols)
    y = np.linspace(dem['ymin'], dem['ymax'], nrows)
    x, y = np.meshgrid(x, y)

z = []
z.append(1,2)
for key in readingsDict.keys():
    #converting string values to float values in list
    temp = list(map(float, readingsDict[key]))
    z.append(temp)
    
z = 
x, y = np.meshgrid(channelCount, timeSplit)


region = np.s_[5:50, 5:50]
x, y, z = x[region], y[region], z[region]

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))

ls = LightSource(270, 45)
# To use a custom hillshading mode, override the built-in shading and pass
# in the rgb colors of the shaded surface calculated from "shade".
rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

plt.show()
'''