def monotonicznosc(a, b):
    if a>0:
        return "funkcja  rosnąca"
    elif a<0:
        return "funkcja  malejaca"
    elif a==0:
        return "funkcja  stala"

a = int(input("Podaj a: "))
b = input(("Podaj b: "))
print(monotonicznosc(a,b))