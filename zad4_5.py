class ciagi:
    ciag=[]
    def __init__(self, a1, r,ile):
        self.a1=a1
        self.r=r
        self.ile=ile

    def wyswietl_dane(self):
        print("a1=",self.a1," r=",self.r,end="")
        return ""
    def suma(self):
        suma=self.a1
        zmianka=self.a1
        for x in range(0,self.ile,1):
            zmianka+=self.r
            suma=suma+zmianka
        return suma
    def policz_elementy(self):
        for x in range(0,self.ile,1):
            print(self.a1+self.r*x ,end=" ")
        return " "
obiekt = ciagi(1,4,3)
print(obiekt.suma())
print(obiekt.policz_elementy())
print(obiekt.wyswietl_dane())
