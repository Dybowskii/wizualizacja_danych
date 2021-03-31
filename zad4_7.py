class robocik:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def __del__(self):
        return "skasowane"
    def idz_w_gore(self,ile):
        for z in range (0,ile,1):
            self.y=self.y+self.krok
        return ""
    def idz_w_dol(self,ile):
        for z in range (0,ile,1):
            self.y=self.y-self.krok
        return ""
    def idz_w_prawo(self,ile):
        for z in range (0,ile,1):
            self.x=self.x+self.krok
        return ""
    def idz_w_lewo(self,ile):
        for z in range (0,ile,1):
            self.x=self.x-self.krok
        return ""
    def pozycja(self):
        print("aktualna wspolrzedna x:",self.x)
        print("aktualna wspolrzedna y:",self.y, end="")
        return " "




robo1=robocik(74,13,6)
print(robo1.idz_w_gore(2))
print(robo1.idz_w_dol(7))
print(robo1.idz_w_prawo(2))
print(robo1.idz_w_lewo(5))
print(robo1.pozycja())
print(del.robocik)
print(robo1.pozycja())
