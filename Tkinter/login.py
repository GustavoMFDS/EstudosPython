import tkinter as tk


contas = [
    ("admin", "1234"),
    ("Gustavo", "abcd")
]
janela = tk.Tk()
janela.title("Login")
janela.geometry("300x200")

pagina_login = tk.Frame(janela)
pagina_login.pack()
tk.Label(pagina_login, text="Usuário:").pack()
entrada_usuario = tk.Entry(pagina_login)
entrada_usuario.pack()

tk.Label(pagina_login, text="Senha:").pack()
entrada_senha = tk.Entry(pagina_login)
entrada_senha.pack()

def fazer_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if (usuario, senha) in contas:
        pagina_login.pack_forget()
        pagina_sistema.pack()
    else: 
        mensagem['text'] = "Usuário ou senha incorretos."
    

botao_login = tk.Button(pagina_login, text="Login", command=fazer_login).pack()
mensagem = tk.Label(pagina_login, text="")
mensagem.pack()

pagina_sistema = tk.Frame()
tk.Label(pagina_sistema, text="Bem-vindo ao sistema!").pack()
janela.mainloop()