class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def wydruk(self):
        print(self.nazwa_produktu) 
        print(self.ilosc)
        print(self.jednostka_miary)
        print(self.cena_jed)
        return " "
    def ile_produktu(self):
        print(self.ilosc,self.jednostka_miary,end=" ")
        return " "
    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed
obiekt = NaZakupy("jablko",7,"kg",3)
print(obiekt.wydruk())
print(obiekt.ile_produktu())
print(obiekt.ile_kosztuje())
print(obiekt.cena_jed)

