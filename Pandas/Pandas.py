import pandas as pd
import plotly_express as pe

tabela = pd.read_csv("ClientesBanco.csv", encoding="latin1")
tabela = tabela.drop("CLIENTNUM", axis=1)
tabela = tabela.dropna()
#tabela = tabela.describe().round(1) -> limita os numeros dps da virgula
print(tabela)

for coluna in tabela:
    grafico = pe.histogram(tabela, x=coluna, color="Categoria")
    #grafico.show()


qtde_categoria = tabela["Categoria"].value_counts()
print(qtde_categoria)
qtde_categoria_percentual = tabela["Categoria"].value_counts(normalize=True)

grafico = pe.histogram(tabela, x="Idade", color="Categoria")
#grafico.show() -> mostra o grafico
