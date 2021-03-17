def promien(a, b,c,d):
    wynik=(c-a)**2+(d-b)**2
    return wynik**(1/2)
    

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
print(promien(a,b,x,y))