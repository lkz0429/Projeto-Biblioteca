import tkinter
from tkinter import ttk
from tkinter import ttk as Tk

Janela = None

def main():

    Janela = tkinter.Tk() #caso isolado
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

    area_botao = Tk.Frame(Janela, width=200, height=100)
    area_botao.pack(pady=20, padx=20,  side="top")
    ttk.Button(area_botao, text="Abrir janela", command= abrir_janela).pack(anchor="w")

    Janela.mainloop()

def abrir_janela():

    janela = tkinter.Toplevel(Janela)
    janela.title("Verificar usuários")
    janela.transient(Janela)
    janela.minsize(560, 380)

        

if __name__ == "__main__":
    main()