def pitagoras(a = 0, b = 0):
    wynik=a**2+b**2
    return wynik**(1/2)

a=int(input("podaj bok a"))
b=int(input("podaj bok b"))
print(pitagoras(a,b))