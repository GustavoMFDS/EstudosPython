import os
import pandas as pd
import plotly.express as px 

# Carregar todos os arquivos de vendas em uma lista
tabelas = [pd.read_csv(f"Vendas/{arquivo}") for arquivo in os.listdir("Vendas") if "Vendas" in arquivo]
tabela_total = pd.concat(tabelas, ignore_index=True)


# Calcular faturamento
tabela_total["Faturamento"] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

# Análise de produtos
tabela_produtos = tabela_total.groupby("Produto")["Quantidade Vendida"].sum().sort_values(ascending=False)
print("\n=== PRODUTOS MAIS VENDIDOS ===")
print(tabela_produtos)

# Análise de faturamento por produto
tabela_faturamento = tabela_total.groupby("Produto")["Faturamento"].sum().sort_values(ascending=False)
print("\n=== FATURAMENTO POR PRODUTO ===")
print(tabela_faturamento)

# Análise por loja
tabela_loja = tabela_total.groupby("Loja")["Faturamento"].sum().sort_values(ascending=False).reset_index()
print("\n=== FATURAMENTO POR LOJA ===")
print(tabela_loja)


grafico = px.bar(tabela_loja, x='Loja', y='Faturamento') 
grafico.show()