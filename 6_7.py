import numpy as np
def funkcja(n):
    
    # m =(np.arange(dlugosc, 0, -1))
    wynik= np.diag([2 for a in range(n)])

    for x in range(1,n,1):
        x1=np.diag([2*(x+1) for _ in range(n-x)],x)
        x2=np.diag([2*(x+1) for _ in range(n-x)],-x)
        wynik+=x1+x2
    print(wynik)

dlugosc = int(input("Podaj dlugosc: "))
funkcja(dlugosc)