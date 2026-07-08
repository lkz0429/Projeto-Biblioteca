import tkinter
from tkinter import ttk
from tkinter import ttk as Tk

usuarios = {}
Janela = None
entrada_nome = None
nome = None

def main():
    global Janela

    Janela = tkinter.Tk()
    Janela.title("janela 1")
    Janela.geometry("1024x720")
    Janela.minsize(960, 720)

    Head = ttk.Frame(Janela, width=200, height=100)
    Head.pack(pady=20, padx=20, side="top")

    Titulo = ttk.Label(
        Head,
        text="Olá, seja bem vindo ao organizador virtual literário",
        font="Arial"
    )
    Titulo.pack()

    area_botao = Tk.Frame(Janela, width=200, height=100)
    area_botao.pack(pady=20, padx=20, side="top")

    ttk.Button(
        area_botao,
        text="Verificar Pontos",
        command=janela_pontos
    ).pack(anchor="w")

    ttk.Button(
        area_botao,
        text="Adicionar usuário",
        command=adicionar_usuario
    ).pack(anchor="w")

    Janela.mainloop()

def adicionar_usuario():
        global entrada_nome

        Cadastro_nome = tkinter.Toplevel(Janela)
        Cadastro_nome.title("Janela de nomes")
        Cadastro_nome.minsize(400, 400)

        Nome = Tk.Frame(Cadastro_nome, width=200, height=100)
        Nome.pack(padx=20, pady=20, side="top")

        entrada_nome = ttk.Entry(Nome)
        entrada_nome.pack(pady=5)

        entrada_nome.bind("<Return>", definir_usuario)

def definir_usuario(event=None, janela=None):
        
        global entrada_nome

        nome = entrada_nome.get()

        usuarios[nome] = {
            "Livro": tkinter.StringVar(value="Nenhum"),
            "Pontos": tkinter.StringVar(value=0)
        }
        
        entrada_nome.delete(0, tkinter.END)

        if janela:
            janela.estroy()


def janela_pontos():
    global nome

    janela = tkinter.Toplevel(Janela)
    janela.title("Pontos de Usuários")
    janela.transient(Janela)
    janela.minsize(560, 380)

    lista_de_usuarios = ttk.Frame(janela, width=100, height=500)
    lista_de_usuarios.pack(padx=15, pady=15)

    texto = "Usuários:\n\n"

    for nome in usuarios:
        texto += f"Nome: {nome}\n"
        texto += f"Livro: {usuarios[nome]['Livro'].get()}\n"
        texto += f"Pontos: {usuarios[nome]['Pontos'].get()}\n\n"

    usuarios_label = ttk.Label(
        lista_de_usuarios,
        text=texto,
        font="Arial",
        justify="left"
    )

    usuarios_label.pack(padx=10, pady=10)


if __name__ == "__main__":
    main()