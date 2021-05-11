import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx,'Arkusz1')
wyswitl = data.groupby(['Rok']).agg(liczba_urodzonych_dzieci=('Liczba','sum'))
print(wyswitl)
wyswitl = wyswitl.cumsum()
wyswitl.plot()
plt.show()
