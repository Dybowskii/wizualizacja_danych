import pandas as pd
import numpy as np
df = pd.read_csv('zamowienia.csv',sep=";")
df['rok'] = pd.DatetimeIndex(df['Data zamowienia']).year
print(df[(df.rok==2005)& (df.Kraj=="Polska")].agg({'Sprzedawca':['count']}))
