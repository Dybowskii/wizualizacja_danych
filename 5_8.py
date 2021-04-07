class samogloski:
    def __init__(self, samolitera):
        self.samolitera = samolitera
        self.index = len(samolitera)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index<0:
            raise StopIteration
        elif(self.samolitera[self.index] in "aeiouy"):
            print(self.samolitera[self.index],end="")
            self.index = self.index - 1
            return ""
        else:
            self.index = self.index - 1
            return ""
        
zad=samogloski("afiodee",)
print(zad.__next__())
print(zad.__next__())
print(zad.__next__())
print(zad.__next__())
print(zad.__next__())
print(zad.__next__())

