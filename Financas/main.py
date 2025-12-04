from utilitarios import (
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total,
)
# Categorias
categoria_receita = cadastrar_categoria("Receitas")
categoria_contas = cadastrar_categoria("Contas fixas")
categoria_viagens = cadastrar_categoria("Viagens")
categoria_lazer = cadastrar_categoria("Lazer")

# Transacoes
cadastrar_transacao(descricao = "Salario", valor= 1500.00, categoria= categoria_receita)

cadastrar_transacao(descricao = "Mesada",valor= 200.00, categoria= categoria_receita)

cadastrar_transacao(descricao= "Ingresso F1",valor= -1000.00,categoria = categoria_lazer)

cadastrar_transacao( descricao= "conta de luz", valor= -150.00,categoria = categoria_contas)

cadastrar_transacao(descricao= "disney", valor= -400.00,categoria= categoria_viagens)

total = saldo_total()
print(f"Saldo total: {total}")