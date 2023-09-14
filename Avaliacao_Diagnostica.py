import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def trabalho():
    nome = nomeEntry.get()
    mensagem = mensagemEntry.get()
    
    if nome and mensagem:
        mensagemjanela = tk.Toplevel(janela)
        mensagemjanela.title('Mensagem Enviada')
        Labelmensagem = tk.Label(mensagemjanela, text=f"{nome} diz {mensagem}")
        Labelmensagem.pack()
        janela.wait_window(mensagemjanela)
    else:
        messagebox.showerror("Erro", "Por favor, insira o nome e a mensagem")


janela = tk.Tk()
janela.title("Prova diagnóstica")
janela.geometry("250x130")
janela.configure(background="turquoise")


Nome = tk.Label(janela, text="Nome",  background="turquoise")
Nome.pack()
nomeEntry = tk.Entry(janela)
nomeEntry.pack()

mensagem = tk.Label(janela, text="Mensagem", background="turquoise")
mensagem.pack()
mensagemEntry = tk.Entry(janela)
mensagemEntry.pack()

botaoenviar = tk.Button(janela, text="Enviar", background="violet", command=trabalho)
botaoenviar.pack()

mensagemaguardando = tk.Label(janela, text="Aguardando mensagem do usuário", background="turquoise")
mensagemaguardando.pack()

janela.mainloop()