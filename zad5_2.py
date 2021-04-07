class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
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


# a teraz klasa która dziedziczy po klasie Ksztalty
class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
    def __add__(self,other):
        self.x=self.x+other.x
        self.y=self.x
        print("nowy x",self.x)
        
kw1=Kwadrat(8)
kw2=Kwadrat(3)
print(kw1+kw2)
    