numeros =[1,2,3,4,5]
numeros.append(6)
numeros.remove(2)
posicao = numeros.index(4)
numeros.insert(posicao,40)
numeros.remove(4)
numeros.sort(reverse=True)  
print(numeros)


frutas = ("maçã", "banana", "laranja","uva")
if 'banana' in frutas:
    print("Banana esta na tupla")
frutas_lista = list(frutas)
frutas_lista.append("abacaxi")
frutas = tuple(frutas_lista)
print(frutas)

aluno = {"nome": "Maria", "idade": 20, "curso": "Engenharia"}
aluno['nota'] = 9.5 
aluno['idade'] = 21
aluno.pop('curso')
aluno['curso'] = ["Engenharia", "Computacao", "Medicina"]
print(aluno["curso"][1])