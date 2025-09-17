import pandas as pd

df = pd.read_csv("data/points_tmw - dados origem.csv")

df.head()

#Frequencia absoluta
freq_categoria = (df.groupby(["descCategoriaProduto"])[["idTransacao"]].count())
#Frequencia absoluta acumulada
freq_categoria['Freq.ABS.Acum'] =freq_categoria["idTransacao"].cumsum()
#Frequencia relativa
freq_categoria['Freq.relativa'] = freq_categoria["idTransacao"] / freq_categoria["idTransacao"].sum()
#Frequencia relativa acumulada
freq_categoria['Freq.relativa.Acum'] = freq_categoria['Freq.relativa'].cumsum()

freq_categoria["Freq.Asoluta"] = freq_categoria["idTransacao"]
freq_categoria

