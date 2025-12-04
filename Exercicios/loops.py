#Exercicio 1
numero = 0
while numero <= 10:
    print(numero)
    numero += 1

#exercicio 2 

numero = int(input("Digite um numero para ver sua tabuada:"))
for i in range(11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#exercicio 3

vogais = 0
palavra = input("Digite uma palavra:")
for letra in palavra:
    if letra.lower() in 'aeiou':
       vogais += 1
print(f"{palavra} tem {vogais} vogais.")

#exercicio 4

tabuada = 0
for i in range(1, 101):
    for j in range(1, 11):
        tabuada = i*j
        print(f"{i} x {j} = {tabuada}")

