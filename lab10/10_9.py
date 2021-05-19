import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('zamowienia.csv',sep=";")
nowe=df.groupby(['Sprzedawca']).count()
nowe=nowe.reset_index()
a=nowe['Kraj']
b=nowe['Sprzedawca']
wedges, texts, autotexts = plt.pie(a, labels=b,
                                   autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"))
plt.setp(autotexts, size=14, weight="bold")
plt.title("dwie godziny z tym walcze")
plt.legend(title='Sprzedwacy')
plt.show()