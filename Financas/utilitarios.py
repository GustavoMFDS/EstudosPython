from categoria import Categoria
from transacao import Transacao

Lista_categorias = []
Lista_transacoes = []

def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome=nome)
    Lista_categorias.append(nova_categoria)
    return nova_categoria

def cadastrar_transacao(descricao, valor, categoria):
    nova_transacao = Transacao(
        descricao= descricao,
        valor= valor,
        categoria= categoria,
    )
    Lista_transacoes.append(nova_transacao)
    return nova_transacao

def saldo_total():
    total = 0
    for t in Lista_transacoes:
        total += t.valor
    return total

