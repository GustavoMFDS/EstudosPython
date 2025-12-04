#exercicio 1
def contardor_regressivo(n):
    while n >= 0:
        print(n)
        n -= 1
contardor_regressivo(10)
#exercicio 2
def maior_numero(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior
print(maior_numero(3,5,7,2,8,1))


    
