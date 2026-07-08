import tkinter
from tkinter import ttk
import json
import time

usuarios = {}

Janela = None
entrada_nome = None
entrada_livro = None
entrada_cpf = None
entrada_pontos = None

class usuario:

    def __init__(self):
          
          global entrada_nome, entrada_livro, entrada_cpf, entrada_pontos

    def definir_usuario(self):

        usuarios[entrada_nome.get()] = {
            "Livro": entrada_livro.get(),
            "cpf": entrada_cpf.get(),
            "pontos": entrada_pontos.get()
        }

        with open("Dados.JSON", "w", encoding="utf-8") as Dados_usuarios:
            json.dump(usuarios, Dados_usuarios, ensure_ascii=False, indent=2)

        entrada_nome.delete(0, tkinter.END)
        entrada_livro.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)
        entrada_pontos.delete(0, tkinter.END)

    def somar_pontos(self):

        with open("Dados.JSON", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)

        with open("Dados.JSON", "w") as arquivo:
            usuarios[nome]["pontos"] += 1

        with open("Dados.JSON", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, ensure_ascii=False, indent=2)

    def adicionar_usuario():
        global entrada_nome, entrada_cpf, entrada_livro, entrada_pontos

        Cadastro_nome = tkinter.Toplevel(Janela)
        Cadastro_nome.title("Cadastro de usuário")
        Cadastro_nome.minsize(500, 200)
        Cadastro_nome.maxsize(500, 200)

        toplevelcadastro = tkinter.Frame(

            Cadastro_nome, 
            width=500, 
            height=200,
            bd=0,
            bg="gray",
            relief="solid"

        )
        toplevelcadastro.pack(padx=20, pady=20, side="top")
        toplevelcadastro.pack_propagate(False)

        titulo = tkinter.Label(toplevelcadastro, text="Digite o usuário a ser adicionado", font=("Arial", 12, "bold"))
        titulo.pack(padx=0, pady=2, side="top")


        entrada_nome = ttk.Entry(toplevelcadastro)
        entrada_nome.pack(padx=0, pady=5, side="top")

        entrada_livro = ttk.Entry(toplevelcadastro)
        entrada_livro.pack(padx=0, pady=5, side="top")

        entrada_cpf = ttk.Entry(toplevelcadastro)
        entrada_cpf.pack(padx=0, pady=5, side="top")

        entrada_pontos = ttk.Entry(toplevelcadastro)
        entrada_pontos.pack(padx=0, pady=5, side="top")

        entrada_nome.bind("<Return>", usuario.definir_usuario)
          
def main():
    global Janela

    Janela = tkinter.Tk()
    Janela.title("Janela principal")
    Janela.geometry("1024x720")
    Janela.minsize(960, 720)
    Janela.configure(bg="gray")

    Head = tkinter.Frame(

        Janela, 
        width=400, 
        height=100,
        bd=5,
        relief="solid"

    )
    Head.pack(

        pady=40, 
        padx=0, 
        side="top"

    )

    Head.pack_propagate(False)

    Titulo = ttk.Label(
        Head,
        text="Seja bem vindo!!\n organizador virtual literário",
        font=("Arial", 20, "bold"),
        wraplength=400,
    )
    Titulo.pack()

    Frame_direito = tkinter.Frame(

        Janela, 
        width=300,
        height=400,
        bd=5,
        relief="solid"
    )
    Frame_direito.pack(

        padx=40,
        pady=0,
        side="right"

    )

    Descricao = tkinter.Label(Frame_direito, text="Este organizador serve para que sistemas de bibliotecas sejam admnistrados de maneira dinâmica e aumenta a produtividade, serve como um registro de prazos e histórico de cada pessoa a pegar livros emprestados!!!", font=("Arial", 19, "bold"), wraplength=300)

    Descricao.pack(padx=0, pady=0)

    Frame_direito.pack_propagate(False)


    area_botao = tkinter.Frame(

        Janela, 
        width=200, 
        height=400,
        bd=5,
        relief="solid"
    )
    area_botao.pack(

        pady=0, 
        padx=50, 
        side="left"

    )

    area_botao.pack_propagate(False)

    botao1 = tkinter.Button(
        area_botao,
        text="Verificar Pontos",
        font=("Arial", 15, "bold"),
        command=janela_pontos,
        width=14,
        height=2,
    )
    botao1.pack(anchor="center")

    botao2 = tkinter.Button(
        area_botao,
        text="Adicionar usuário",
        font=("Arial", 15, "bold"),
        command=usuario.adicionar_usuario,
        width=14,
        height=2,
    )
    botao2.pack(anchor="center")

    Janela.mainloop()

def janela_pontos():
    global nome

    janela = tkinter.Toplevel(Janela)
    janela.title("Pontos")
    janela.transient(Janela)
    janela.minsize(560, 380)

    with open("Dados.JSON", "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)

    lista_de_usuarios = tkinter.Frame(

        janela, 
        width=100, 
        height=500,
        bd=2,
        relief="solid",
    )
    lista_de_usuarios.pack(padx=15, pady=15)

    texto = "Usuários:\n\n"

    for nome in usuarios:
        texto += f"Nome: {nome}\n"
        texto += f"Livro: {usuarios[nome]['Livro']}\n"
        texto += f"CPF: {usuarios[nome]['cpf']}\n\n"
        texto += f"Pontos: {usuarios[nome]['pontos']}\n\n\n"


    usuarios_label = ttk.Label(
        lista_de_usuarios,
        text=texto,
        font="Arial",
        justify="left"
    )

    usuarios_label.pack(padx=10, pady=10)


if __name__ == "__main__":
    main()