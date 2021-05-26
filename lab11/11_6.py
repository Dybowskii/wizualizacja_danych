from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection = '3d')
x = np.linspace(0, 1, 5)
y = np.cos(x) 
ax.plot(x, y, zs = 0 , zdir = 'z' , label = 'curve in (x,y)')
ax1 = fig.add_subplot(1, 2, 2, projection = '3d')
colors = ('g')
np.random.seed(19680801)
x = np.random.sample(20)
y = np.random.sample(20)
z = np.random.sample(20)

ax1.scatter(x, y, zs = z, zdir = 'y', c ='green', label = 'points in (x,z)')


ax1.legend()
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.set_zlim(0, 1)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')


plt.show()