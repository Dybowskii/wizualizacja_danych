class slowka:
    def __init__(self, slowo1, slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    def palindrom(self,a):
        if a==1:
            dlugosc=len(self.slowo1)
            x=1
            z=0
            while (x<=dlugosc/2):
                if self.slowo1[x]==self.slowo1[dlugosc-x]:
                    z=z+1
                x = x + 1
            if(z!=1):
                return "slowo jest palindromem"
            else:
                return "nie jest palindromem"
        else:
            dlugosc=len(self.slowo2)
            x=1
            z=0
            while (x<=dlugosc/2):
                if self.slowo2[x]==self.slowo2[dlugosc-x]:
                    z=z+1
                x = x + 1
            if(z!=1):
                return "slowo jest palindromem"
            else:
                return "nie jest palindromem"
    def metagram(self):
        x=len(self.slowo1)
        meta=0
        if(x!=len(self.slowo2)):
            return "te slowa to nie metagramy"
        else:
            for z in range(0,x,1):
                if(self.slowo1[z]!=self.slowo2[z]):
                    meta+=1
            if(meta==1):
                return "slowo jest metagramem"
            else:
                return "slowo nie jest metagramem"
    def wyswietl_wyrazy(self):
        print(self.slowo1)
        print(self.slowo2,end="")
        return ""         
    def anagram(self):
        x=len(self.slowo1)
        meta=0
        if(x!=len(self.slowo2)):
            return "te slowa to nie anagramy"
        else:
            litery_slowo1=list(self.slowo1)
            litery_slowo2=list(self.slowo2)
            litery_slowo1.sort()
            litery_slowo2.sort()
            if(litery_slowo1==litery_slowo2):
                return "te slowa to anagramy"
            else:
                return "te slowa to nie angarmay"



slowa=slowka("tat","att")
print(slowa.palindrom(2))
print(slowa.metagram())
print(slowa.wyswietl_wyrazy())
print(slowa.anagram())



    