#liczba =input ('podaj liczbe:')
suma = 0
#for litera in liczba:
#    suma+=int(litera)

#print(suma)
liczba =input ('podaj liczbę:')
indeks=0
dodawanie=0
while (indeks <len(liczba)):
    dodawanie=liczba[indeks]
    suma+=int(dodawanie)
    indeks+=1
print(suma)