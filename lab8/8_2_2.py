import pandas as pd
import numpy as np
df = pd.read_csv('zamowienia.csv',sep=";")
print(df.nlargest(5,"Utarg"))