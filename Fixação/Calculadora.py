num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))

def Soma(num1, num2):
    return num1 + num2
def Subtracao(num1, num2):
    return num1 - num2
def Multiplicacao(num1, num2):
    return num1 * num2
def Divisao(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return num1 / num2

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração") 
print("3 - Multiplicação")
print("4 - Divisão")
operacao = input("Digite o número da operação desejada (1/2/3/4): ")
if operacao == '1':
    print(f"{num1} + {num2} = {Soma(num1, num2)}")
elif operacao == '2':
    print(f"{num1} - {num2} = {Subtracao(num1, num2)}")
elif operacao == '3':
    print(f"{num1} * {num2} = {Multiplicacao(num1, num2)}")
elif operacao == '4':
    print(f"{num1} / {num2} = {Divisao(num1, num2)}")