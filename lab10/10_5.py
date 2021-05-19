import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('iris.data', delimiter=',', header=None)
# 0, 1, 2 to domyślne etykiety tego DataFrame, sprawdź wypisując df na konsolę
x=data[0]
y=data[1]
c=data[2]
s=data[3]
plt.scatter(x,y,c=c)
plt.show()