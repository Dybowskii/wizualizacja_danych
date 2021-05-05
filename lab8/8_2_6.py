import pandas as pd
import numpy as np
df = pd.read_csv('zamowienia.csv',sep=";")
df['rok'] = pd.DatetimeIndex(df['Data zamowienia']).year
pomoc1= df[(df.rok==2004)]
pomoc2= df[(df.rok==2005)]
pomoc1.to_csv("zamowienia_2004.csv", sep=";")
pomoc2.to_csv("zamowienia_2005.csv", sep=";")