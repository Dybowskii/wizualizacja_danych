import numpy as np
a=np.arange(12).reshape(3,4)
print(a)
for x in a.flat:
    print(x)
b=np.arange(12).reshape(4,3)
print(b)
for x in b.flat:
    print(x)
c=np.arange(12).reshape(2,6)
print(c)
for x in c.flat:
    print(x)