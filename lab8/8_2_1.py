import pandas as pd
import numpy as np
df = pd.read_csv('zamowienia.csv',sep=";")
unikaty=df.Sprzedawca.unique()
nazwakol=["Nazwiska"]
wynik=pd.DataFrame(unikaty,columns=nazwakol)
print(wynik)