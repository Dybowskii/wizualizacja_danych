import pandas as pd
import numpy as np
df = pd.read_csv('zamowienia.csv',sep=";")
df['rok'] = pd.DatetimeIndex(df['Data zamowienia']).year
pomoc=(df[(df.rok==2004)].mean())
print(pomoc.Utarg)