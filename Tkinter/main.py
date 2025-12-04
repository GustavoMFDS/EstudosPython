import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")

nome = input("Digite seu nome: ")

texto = tk.Label(janela, text=f"Bem vindo, {nome}")
texto.pack()

def ao_clicar():
    nome = entrada_texto.get()
    texto['text'] = f"Olá, {nome}!"

entrada_texto = tk.Entry(janela)
entrada_texto.pack()
botao = tk.Button(janela, text="Clique aqui", command=ao_clicar).pack()

janela.mainloop()