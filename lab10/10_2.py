import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(0,20,30)
plt.plot(x,1/x,label='liniowa',marker='>',linestyle='dashed')
plt.xlabel('os x')
plt.axis([0,20,0,1])
plt.ylabel('f(x)')
plt.legend()
plt.show()
