
with open("kolejne.txt", "r+","w+") as plik:
    plik.write("""
    Swiat: Istnieje
    Programisa: Witaj :)
    """)
    for linia in plik:
        print(linia, end="")