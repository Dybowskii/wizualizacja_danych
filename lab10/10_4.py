import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
plt.plot(x,np.sin(x)+2,label='sinus')
plt.plot(x,np.sin(x+np.pi),label='sinus')
plt.xlabel('x')
plt.ylabel('sin(x) oraz cos(x)')
plt.legend()
plt.show()