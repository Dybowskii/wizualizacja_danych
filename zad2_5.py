a=input("podaj liczbe a")
b=input("podaj liczbe b")
c=input("podaj liczbe c")
if (int(a)>0 and int(a)<=10) :
    if(int(a)>int(b)):
        print("a miesci sie w przedziale oraz a jest wieksze od b")
    elif(int(b)>int(c)):
        print("a miesci sie w przedziale oraz b jest wieksze od c1")
    else:
        print("a miesci sie w przedziale")
else :
    print ("nie jest")