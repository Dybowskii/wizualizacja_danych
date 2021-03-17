def ciag(a1 = 1, r = 1,ile=10):
    suma=a1
    for x in range(1,ile,1):
        a1+=r
        suma+=a1
    return suma

a=int(input("podaj a1: "))
b=int(input("podaj wielkosc o jaka rosnie ciag: "))
c=int(input("podaj ilosc elementow: "))
print(ciag())
print(ciag(a,b,c))
