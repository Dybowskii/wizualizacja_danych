def prostopadlosc(a, b,c,d):
    if a==c:
        return "proste sa rownolegle"
    elif a*c==-1:
        return "proste sa prostopadle"
    else:
        return "nie sa prostopadle ani rownolegle"

a1 = int(input("Podaj a1: "))
a2 = int(input("Podaj a2: "))
b1 = int(input("Podaj b1: "))
b2 = int(input("Podaj b2: "))
print(prostopadlosc(a1,b1,a2,b2))