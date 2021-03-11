liczba = input("Podaj liczbe: ")
liczba = liczba.split()
a = len(liczba)
for x in range(0, a, 1):
    print(int(liczba[x])*int(liczba[x]))