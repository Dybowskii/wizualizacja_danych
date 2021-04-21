import numpy as np
def funkcja(dlugosc):
    # m =(np.arange(dlugosc, 0, -1))
    return (np.diag(np.arange(dlugosc,0,-1)))

dlugosc = int(input("Podaj dlugosc: "))
print(funkcja(dlugosc))
mat_diag = np.diag([2 for a in range(5)])
print(mat_diag)