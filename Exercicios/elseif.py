#A
print("Estou aprendendo python")

#B
nome = input("Qual seu nome:")
idade = int(input("Qual sua idade:"))

print(f"Seu nome é {nome}, e sua idade e  {idade}.")


#C
num1 = int(input("Digite um numero:"))
num2 = int(input("Digite outro numero:"))


soma = num1 + num2
sub= num1 - num2
print(f"A soma dos numeros e {soma} e a subtração e {sub}")

#D
pao = 10
dinheiro= float(input("Quanto dinheiro voce tem:"))
if dinheiro >= pao:
  print("Voce comprou 1 pão")
else:
  print("Voce e pobre suficinete pra nao conseguir comprar pao")

#E
temperatura = int(input("Digite a temperatura atual"))

if temperatura < 15:
  print("Esta frio")
elif temperatura < 28:
  print("Esta normal")
elif temperatura > 28:
  print("Ta torrando de calor")

#F
horario = int(input("Digite o horario aqui:"))
 
if horario < 12 and horario >=6:
  print("Bom dia")
elif horario<18 and horario>=12:
  print("Boa tarde")
elif horario<24 and horario>=18:
  print("Boa noite")
else:
  print("Boa madrugada")

#G
idade= int(input("Digite sua idade:"))
condicao = str(input("Se voce tem condicionamento fisico ou permissao medica digite sim, caso nao tenha digite nao:"))

if idade>18 and idade<35:
  if condicao=="sim":
    print("Voce pode participar da corrida")
  else: 
    print("Voce nao pode participar")