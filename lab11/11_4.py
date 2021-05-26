import matplotlib
from matplotlib.colors import LightSource
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# konfiguracja wielkości wykresu, figsize określa wielkość wykresu w calach
fig = plt.figure()
ax1 = fig.add_subplot(221, projection = '3d')
ax2 = fig.add_subplot(222, projection = '3d')
ax3 = fig.add_subplot(223, projection = '3d')
ax4 = fig.add_subplot(224, projection = '3d')

# fikcyjne dane
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade = True)
ax1.set_title('Wykres zacieniony')
ax2.bar3d(x, y, bottom, width, depth, top, shade = False, alpha=0.5 )
ax2.set_title('Wykres przezroczysty')
ax3.bar3d(x, y, bottom, width, depth, top, shade = True, antialiased=False,color='g' )
ax3.set_title('wykres zielony')
ax4.bar3d(x, y, bottom, width, depth, top, shade = False ,antialiased=False,color='r')
ax4.set_title('Wykres nie czerwony bez obrysu')
plt.show()