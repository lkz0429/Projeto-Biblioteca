import tkinter
from tkinter import ttk
import json

usuarios = {}

Janela = None
entrada_nome = None
entrada_livro = None
entrada_cpf = None
entrada_prazo = None

class usuario:

    def __init__(self):

        pass

    def definir_usuario():

        try:
            with open("Dados.JSON", "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)
        except:
            with open("Dados.JSON", "w", encoding="utf-8") as arquivo:
                        usuarios = json.dump({},arquivo)
            
            with open("Dados.JSON", "r", encoding="utf-8") as arquivo:
                        usuarios = json.load(arquivo)

        usuarios[entrada_nome.get()] = {
            "Livro": entrada_livro.get(),
            "cpf": entrada_cpf.get(),
            "prazo": entrada_prazo.get()
        }

        with open("Dados.JSON", "w", encoding="utf-8") as Dados_usuarios:
            json.dump(usuarios, Dados_usuarios, ensure_ascii=False, indent=2)

        entrada_nome.delete(0, tkinter.END)
        entrada_livro.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)
        entrada_prazo.delete(0, tkinter.END)

    def limpar_campo_entrada():

        entrada_nome.delete(0, tkinter.END)
        entrada_livro.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)
        entrada_prazo.delete(0, tkinter.END)
        


    def somar_pontos(self):

        with open("Dados.JSON", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)

        with open("Dados.JSON", "w") as arquivo:
            usuarios[nome]["pontos"] += 1

        with open("Dados.JSON", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, ensure_ascii=False, indent=2)

    def adicionar_usuario():

        global entrada_nome, entrada_livro, entrada_cpf, entrada_prazo

        Cadastro_nome = tkinter.Toplevel(Janela)
        Cadastro_nome.title("Novo Usuário")
        Cadastro_nome.minsize(600, 400)
        Cadastro_nome.maxsize(600, 400)

        toplevelcadastro = tkinter.Frame(

            Cadastro_nome, 
            width=600, 
            height=300,
            bd=0,
            bg="gray",
            relief="solid"

        )
        toplevelcadastro.pack(padx=20, pady=20, side="top")
        toplevelcadastro.pack_propagate(False)

        titulo = tkinter.Label(toplevelcadastro, text="Digite o usuário a ser adicionado", font=("Arial", 12, "bold"))
        titulo.pack(padx=0, pady=2, side="top")


        tkinter.Label(toplevelcadastro, text="Nome:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_nome = ttk.Entry(toplevelcadastro)
        entrada_nome.pack(padx=0, pady=5, side="top")

        tkinter.Label(toplevelcadastro, text="livro:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_livro = ttk.Entry(toplevelcadastro)
        entrada_livro.pack(padx=0, pady=5, side="top")

        tkinter.Label(toplevelcadastro, text="cpf:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_cpf = ttk.Entry(toplevelcadastro)
        entrada_cpf.pack(padx=0, pady=5, side="top")

        tkinter.Label(toplevelcadastro, text="prazo:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_prazo = ttk.Entry(toplevelcadastro)
        entrada_prazo.pack(padx=0, pady=5, side="top")

        enviar = tkinter.Button(toplevelcadastro, text="Cadastrar", command=usuario.definir_usuario, font=("Arial", 12, "bold"), width=7, height=3)
        enviar.pack(padx=75, side="right")

        limpar = tkinter.Button(toplevelcadastro, text="Limpar", command=usuario.limpar_campo_entrada, font=("Arial", 12, "bold"), width=7, height=3)
        limpar.pack(padx=75, side="left")
          
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

    Frame_mid = tkinter.Frame(
    
            Janela, 
            width=300,
            height=250,
            bd=5,
            relief="solid"
        )
    Frame_mid.pack(
    
            padx=40,
            pady=0,
            side="right"
    
        )
    
    Descricao2 = tkinter.Label(Frame_mid, text="O sistema de pontos é uma maneira de penalizar aqueles que descumprem o prazo, você pode verificar a situação dos usuários em cadastros", font=("Arial", 19, "bold"), wraplength=300)
    
    Descricao2.pack(padx=0, pady=0)
    
    Frame_mid.pack_propagate(False)


    area_botao = tkinter.Frame(

        Janela, 
        width=200, 
        height=300,
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
        text="cadastros",
        font=("Arial", 12, "bold"),
        command=janela_pontos,
        width=14,
        height=2,
    )
    botao1.pack(anchor="center")

    botao2 = tkinter.Button(
        area_botao,
        text="Adicionar usuário",
        font=("Arial", 12, "bold"),
        command=usuario.adicionar_usuario,
        width=14,
        height=2,
    )
    botao2.pack(anchor="center")

    Janela.mainloop()

def janela_pontos():
    global nome

    janela = tkinter.Toplevel(Janela)
    janela.title("Cadastros")
    janela.transient(Janela)
    janela.minsize(560, 380)
    janela.maxsize(9680, 300)

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
        texto += f"Prazo: {usuarios[nome]['prazo']}\n\n\n"


    usuarios_label = ttk.Label(
        lista_de_usuarios,
        text=texto,
        font="Arial",
        justify="left"
    )

    usuarios_label.pack(padx=10, pady=10)


if __name__ == "__main__":
    main()