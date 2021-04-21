import numpy as np
def tab(n):
    x = np.arange(1,n*n+1).reshape(n, n)
    return x
a=int(input("podaj lizcbe"))
print(tab(a))


