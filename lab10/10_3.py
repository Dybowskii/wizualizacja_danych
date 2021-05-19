import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = np.arange(0, 30, 0.1)
plt.plot(x,np.sin(x),label='sinus')
plt.plot(x,np.cos(x),label='sinus')
plt.xlabel('x')
plt.ylabel('sin(x) oraz cos(x)')
ax.annotate('cosinus w pi', xy=(np.pi, -1), xytext=(10, -1.4),
            arrowprops=dict(facecolor='black', shrink=1),
            )
ax.annotate('sinus w 0,5pi', xy=(np.pi*0.5, 1), xytext=(10, 1.3),
            arrowprops=dict(facecolor='black', shrink=1),
            )
ax.set_ylim(-1.5, 1.5)
plt.show()