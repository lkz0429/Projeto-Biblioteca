import tkinter
from tkinter import ttk
import json

usuarios = {}

Janela = None
entrada_nome = None
entrada_livro = None
entrada_cpf = None
entrada_pontos = None
busca_cpf = None
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
            "cpf": entrada_cpf.get(),
            "prazo": f"{3} dias"
        }

        with open("Dados.JSON", "w", encoding="utf-8") as Dados_usuarios:
            json.dump(usuarios, Dados_usuarios, ensure_ascii=False, indent=2)

        entrada_nome.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)

    def limpar_campo_cadastro():

        entrada_nome.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)
        entrada_pontos.delete(0, tkinter.END)

    def limpar_campo_penalidades():
         
         entrada_pontos.delete(0, tkinter.END)
         busca_cpf.delete(0, tkinter.END)


    def somar_pontos(self):

        #função deve retornar a busca do nome do usuário pelo cpf dele e somar +quantia especificada em "entrada_pontos" na chave "pontos" do usuário
        pass

    def adicionar_usuario():

        global entrada_nome, entrada_cpf

        Cadastro_nome = tkinter.Toplevel(Janela)
        Cadastro_nome.title("Novo Usuário")
        Cadastro_nome.minsize(600, 400)
        Cadastro_nome.maxsize(600, 400)

        toplevelcadastro = tkinter.Frame(

            Cadastro_nome, 
            width=600, 
            height=300,
            bd=5,
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

        tkinter.Label(toplevelcadastro, text="cpf:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_cpf = ttk.Entry(toplevelcadastro)
        entrada_cpf.pack(padx=0, pady=5, side="top")

        enviar = tkinter.Button(toplevelcadastro, text="Cadastrar", command=usuario.definir_usuario, font=("Arial", 12, "bold"), width=7, height=3)
        enviar.pack(padx=75, side="right")

        limpar = tkinter.Button(toplevelcadastro, text="Limpar", command=usuario.limpar_campo_cadastro, font=("Arial", 12, "bold"), width=7, height=3)
        limpar.pack(padx=75, side="left")

        #fazer livro associado por cadastro fora de cadastro de usuário, permitindo a adição de valor na chave "livro" de cada usuário, o cadastro deve ser único

    def associar_livro():

        janela = tkinter.Toplevel(Janela)
        janela.title("Penalidades")
        janela.transient(Janela)
        janela.minsize(600, 300)
        janela.maxsize(600, 300)

        topleveldepenalidades = tkinter.Frame(
             janela,
             width=600,
             height=300,
             bg="gray",
             bd=5,
             relief="solid"
        )
        topleveldepenalidades.pack(padx=20, pady=20, side="top")
        topleveldepenalidades.pack_propagate(False)
          
    def penalizar_por_cpf():

        global entrada_pontos, busca_cpf

        janela = tkinter.Toplevel(Janela)
        janela.title("Penalidades")
        janela.transient(Janela)
        janela.minsize(600, 300)
        janela.maxsize(600, 300)

        topleveldepenalidades = tkinter.Frame(
             janela,
             width=600,
             height=300,
             bg="gray",
             bd=5,
             relief="solid"
        )
        topleveldepenalidades.pack(padx=20, pady=20, side="top")
        topleveldepenalidades.pack_propagate(False)

        tkinter.Label(topleveldepenalidades, text="cpf:", font=("Arial", 12, "bold")).pack(padx=0, pady=10, side="top")
        busca_cpf = ttk.Entry(topleveldepenalidades)
        busca_cpf.pack(padx=0, pady=10, side="top")

        tkinter.Label(topleveldepenalidades, text="quantia:", font=("Arial", 12, "bold")).pack(padx=0, pady=10, side="top")
        entrada_pontos = ttk.Entry(topleveldepenalidades)
        entrada_pontos.pack(padx=0, pady=10, side="top")

        enviar = tkinter.Button(topleveldepenalidades, text="Penalizar", command=usuario.somar_pontos, font=("Arial", 12, "bold"), width=7, height=3)
        enviar.pack(padx=75, side="right")

        limpar = tkinter.Button(topleveldepenalidades, text="Limpar", command=usuario.limpar_campo_penalidades, font=("Arial", 12, "bold"), width=7, height=3)
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

    botao3 = tkinter.Button(
         area_botao,
         text="Penalizar",
         font=("Arial", 12, "bold"),
         command=usuario.penalizar_por_cpf,
         width=14,
         height=2
    )
    botao3.pack(anchor="center")

    botao4 = tkinter.Button(
         area_botao,
         text="associar-livro",
         font=("Arial", 12, "bold"),
         command=usuario.associar_livro,
         width=14,
         height=2
    )
    botao4.pack(anchor="center")

    Janela.mainloop()

def janela_pontos():

    janela = tkinter.Toplevel(Janela)
    janela.title("Cadastros")
    janela.transient(Janela)
    janela.minsize(560, 380)
    janela.maxsize(560, 9800)

    #visualização feita em tkinter.treeview para os Dados escritos no JSON de forma mais recente ( uma leitura a cada clique no botão que executa essa função )


if __name__ == "__main__":
    main()