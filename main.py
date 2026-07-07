import tkinter
from tkinter import ttk
from tkinter import ttk as Tk

usuarios = {}
Janela = None

def main():
    global Janela
    Janela = tkinter.Tk()
    Janela.title("janela 1")  
    Janela.geometry("1024x720")
    Janela.minsize(960, 720)

    Head = ttk.Frame(Janela, width=200, height=100 )
    Head.pack(pady=20, padx=20, side="top")
    Titulo = ttk.Label(
                            Head, 
                            text="Olá, seja bem vindo ao organizador virtual literário", 
                            font="Arial"
    )
    Titulo.pack()

    area_botao = Tk.Frame(Janela, width=20, height=50)
    area_botao.pack(pady=20, padx=20,  side="top")
    ttk.Button(area_botao, text="Verificar Pontos", command= janela_pontos).pack(anchor="w")
    ttk.Button(area_botao, text="Adicionar usuário", command=adicionar_usuario).pack(anchor="w")

    Janela.mainloop()

def adicionar_usuario():
    nome = input("escreva o nome do usuário: ") # logo vai ser substituído por entry
    usuarios[nome] =  {"Livro": tkinter.StringVar(value="nenhum"), "Pontos": tkinter.StringVar(value=0),} # este dicionário vai ser substituído por um sistema de classes
    return

def janela_pontos():

    janela_pontos = tkinter.Toplevel(Janela)
    janela_pontos.title("Pontos de Usuários")
    janela_pontos.transient(Janela)
    janela_pontos.minsize(560, 380)

    lista_de_usuários = ttk.Frame(janela_pontos, width=100, height=500 )
    lista_de_usuários.pack(padx=15, pady=15)
    usuários = ttk.Label(
        lista_de_usuários,
        text= f"{usuarios}\n",
        font= "Arial"
    )
    usuários.pack(padx=10, pady=10)

        

if __name__ == "__main__":
    main()