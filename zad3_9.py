def ciag(a1 = 1, r = 1,ile=10):
    iloczyn=a1
    for x in range(1,ile,1):
        a1+=r
        iloczyn*=a1
    return iloczyn

a=int(input("podaj a1: "))
b=int(input("podaj wielkosc o jaka rosnie ciag: "))
c=int(input("podaj ilosc elementow: "))

print(ciag(a,b,c))