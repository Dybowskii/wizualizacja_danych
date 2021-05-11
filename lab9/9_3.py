import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx,'Arkusz1')
wyswitl = data[data['Rok']>2016].groupby(['Plec']).agg(Liczba_urodzonych=('Liczba','sum'))
print(wyswitl)
wykres = wyswitl.plot.pie(subplots=False, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title('suma urodzonych dziewczynek i chlopcow od 2016r')
plt.show()
