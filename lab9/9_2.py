import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx,'Arkusz1')
wyswitl = data.groupby(['Plec']).agg(liczba_urodzonych=('Liczba','sum'))
print(wyswitl)
wykres = wyswitl.plot.bar(width=0.3)
wykres.set_ylabel('Mln')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('Liczba urodzonych chlopcow i dziwczynek')
plt.show()
