from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.gca(projection = '3d')
x = np.linspace(0, 1, 5)
y = np.cos(x) 
ax.plot(x, y, zs = 0 , zdir = 'z' ,c='green', label = 'curve in (x,y)')
colors = ('g')
x = np.random.sample(20)
z = np.random.sample(20)
ax.scatter(x, ys=0, zs=z , zdir = 'y', c ='red', label = 'points in (x,z)')


ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(elev = 40. , azim =-90)
plt.show()