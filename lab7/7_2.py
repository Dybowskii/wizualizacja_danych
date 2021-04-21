import numpy as np
a=np.arange(1,10).reshape(3,3)
b=np.array([6,2,3,5,7,9,3,2,4,6,8,2,1,3,5,6]).reshape(4,4)
print(a)
print(b)
print("najmniejsze wartosci kolumn a: ",a.min(axis=0))
print("najmniejsze wartosci rzedow a: ",a.min(axis=1))
print("najmniejsze wartosci kolumn b: ",b.min(axis=0))
print("najmniejsze wartosci rzedow b: ",b.min(axis=1))
