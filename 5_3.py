class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
    def __ge__(self,other):
        if self.x>=other.x:
            print("prawda")
        else:
            print("falsz")  
    def __gt__(self,other):
        if self.x>other.x:
            print("prawda")
        else:
            print("falsz") 
    def __le__(self,other):
        if self.x<=other.x:
            print("prawda")
        else:
            print("falsz") 
    def __lt__(self,other):
        if self.x<other.x:
            print("prawda")
        else:
            print("falsz")   
        
kw1=Kwadrat(2)
kw2=Kwadrat(3)
kw1>=kw2
kw2>kw1
kw1<kw2
kw2<=kw1