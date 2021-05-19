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
plt.yticks(np.arange(0, 4000000, 500000))
plt.bar(etykiety,wartosci)

plt.subplot(3,1,2)
kobiet=data[(data.Plec=='K')]
chlopcy=data[(data.Plec=='M')]
wyswitl = kobiet.groupby(['Rok']).sum().reset_index()
wyswitl2 = chlopcy.groupby(['Rok']).sum().reset_index()
plt.bar(wyswitl.Rok,wyswitl.Liczba,color='red',label='chlopcy')
plt.bar(wyswitl2.Rok,wyswitl2.Liczba, color='green', bottom=wyswitl2.Liczba,label='dziweczynki')
plt.legend()

plt.subplot(3,1,3)
suma=data.groupby([data.Rok]).sum()
suma=suma.reset_index()
plt.bar(suma.Rok,suma.Liczba)
plt.ylabel('ilosc')
plt.xlabel('Rok')
plt.show()