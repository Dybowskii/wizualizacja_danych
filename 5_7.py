class codrugi:
    x=0
    def __init__(self, imiona):
        self.imiona = imiona
        self.index = len(imiona)-12


    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.x:
            print(self.imiona[self.x])
            raise StopIteration
        elif self.x%2==0:
            print(self.imiona[self.x])
            self.x = self.x + 1
        else:
            self.x = self.x + 1

zad=codrugi(["Jacek","Tomek","Jarek","Kasia","Bartek"])
next(zad)
next(zad)
next(zad)
next(zad)
next(zad)

