import pandas as pd

df = pd.read_csv("Marcelo/data/points_tmw - dados origem.csv")
df.head()

#%%
#Frequencia absoluta
freq_produto = (df.groupby(["descProduto"])[["idTransacao"]].count())
#Frequencia absoluta acumulada
freq_produto['Freq.ABS.Acum'] =freq_produto["idTransacao"].cumsum()
#Frequencia relativa
freq_produto['Freq.relativa'] = freq_produto["idTransacao"] / freq_produto["idTransacao"].sum()
#Frequencia relativa acumulada
freq_produto['Freq.relativa.Acum'] = freq_produto['Freq.relativa'].cumsum()

freq_produto["Freq.Asoluta"] = freq_produto["idTransacao"]
freq_produto

# %%
