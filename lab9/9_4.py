import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed()
data = pd.read_csv('iris.data')
data.columns=['sepal length in cm',  'sepal width in cm', 'petal length in cm', 'petal width in cm', 'clas']
a = data[data.clas=='Iris-setosa']
b = data[data.clas=='Iris-versicolor']
c = data[data.clas=='Iris-virginica']
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(a['sepal length in cm'],a['sepal width in cm'], color='green', marker='x')
ax1.scatter(b['sepal length in cm'],b['sepal width in cm'], color='orange', marker='*')
ax1.scatter(c['sepal length in cm'],c['sepal width in cm'], color='red', marker='<')
plt.show()