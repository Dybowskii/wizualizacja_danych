import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('zamowienia.csv',sep=";")
dane_do_wykresu=df.groupby('Sprzedawca').agg({'Sprzedawca':['count']})
print(dane_do_wykresu)
wykres = dane_do_wykresu.plot.bar(width=0.8,color='green',edgecolor='blue', linewidth=2)
wykres.set_ylabel('ilosc zamowien')
wykres.set_xlabel('Sprzedawca')
wykres.legend()
plt.title('Ilosc zlozonych zamowien przez sprzedawcow')
plt.show()
