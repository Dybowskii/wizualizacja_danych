import pandas as pd
import numpy as np
df = pd.read_csv('zamowienia.csv',sep=";")
print(df.groupby('Sprzedawca').agg({'Sprzedawca':['count']}))