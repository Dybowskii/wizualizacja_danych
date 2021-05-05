import pandas as pd
import numpy as np
import xlrd
import openpyxl
xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx,'Arkusz1')
print(data[(data.Rok<=2005)].agg({'Liczba':[sum]}))