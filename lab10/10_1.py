import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx,'Arkusz1')
nowa=data.groupby([data.Plec]).agg({'Liczba':[sum]})
a=nowa.loc['K']
b=nowa.loc['M']
a = int(a)
b = int(b)
plt.subplot(3,1,1)
etykiety = ['K', 'M']
wartosci = [a,b]

plt.bar(etykiety,wartosci, )
plt.show()