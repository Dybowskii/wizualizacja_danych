
import numpy as np
def potega(a,b):
    print("\n", np.logspace(1, b, num=b, base = a, dtype=int))

x=int(input("jaka liczbe chcesz potegowac: "))
y=int(input("ile razy chcesz ja potegowac: "))
potega(x,y)