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
entrada_livro = None
emprestimo_cpf = None

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

        usuarios[entrada_cpf.get()] = {
            "nome": entrada_nome.get(),
            "prazo": f"{3} dias",
            "livro": "",
            "pontos": 0
        }

        with open("Dados.JSON", "w", encoding="utf-8") as Dados_usuarios:
            json.dump(usuarios, Dados_usuarios, ensure_ascii=False, indent=2)

        entrada_nome.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)

    def limpar_campo_cadastro():

        entrada_nome.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)

    def limpar_campo_penalidades():
         
         entrada_pontos.delete(0, tkinter.END)
         busca_cpf.delete(0, tkinter.END)

    def limpar_campo_associar():
         
         entrada_livro.delete(0, tkinter.END)
         emprestimo_cpf.delete(0, tkinter.END)

    def emprestar():

        global usuarios

        with open("Dados.JSON", "r") as arquivo:
             usuarios = json.load(arquivo)

        cpf = emprestimo_cpf.get()

        if cpf in usuarios:
             usuarios[cpf]["livro"] = str(entrada_livro.get())

             with open("Dados.JSON", "w") as arquivo:
                json.dump(usuarios, arquivo, ensure_ascii=False, indent=2)

        entrada_livro.delete(0, tkinter.END)
        emprestimo_cpf.delete(0, tkinter.END)

    def somar_pontos():

        global usuarios

        with open("Dados.JSON", "r") as arquivo:
             usuarios = json.load(arquivo)

        cpf = busca_cpf.get()

        if cpf in usuarios:
             usuarios[cpf]["pontos"] += int(entrada_pontos.get())

             with open("Dados.JSON", "w") as arquivo:
                  json.dump(usuarios, arquivo, ensure_ascii=False, indent=2)

        entrada_pontos.delete(0, tkinter.END)
        busca_cpf.delete(0, tkinter.END)               

    def adicionar_usuario():

        global entrada_nome, entrada_cpf

        Cadastro_nome = tkinter.Toplevel(Janela)
        Cadastro_nome.title("Novo Usuário")
        Cadastro_nome.minsize(600, 300)
        Cadastro_nome.maxsize(600, 300)

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
        titulo.pack(padx=0, pady=10, side="top")


        tkinter.Label(toplevelcadastro, text="cpf:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_cpf = ttk.Entry(toplevelcadastro)
        entrada_cpf.pack(padx=0, pady=10, side="top")

        tkinter.Label(toplevelcadastro, text="nome:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_nome = ttk.Entry(toplevelcadastro)
        entrada_nome.pack(padx=0, pady=10, side="top")

        enviar = tkinter.Button(toplevelcadastro, text="Cadastrar", command=usuario.definir_usuario, font=("Arial", 12, "bold"), width=7, height=3)
        enviar.pack(padx=75, side="right")

        limpar = tkinter.Button(toplevelcadastro, text="Limpar", command=usuario.limpar_campo_cadastro, font=("Arial", 12, "bold"), width=7, height=3)
        limpar.pack(padx=75, side="left")

        #fazer livro associado por cadastro fora de cadastro de usuário, permitindo a adição de valor na chave "livro" de cada usuário, o cadastro deve ser único

    def associar_livro():

        global entrada_livro, emprestimo_cpf

        janela = tkinter.Toplevel(Janela)
        janela.title("Empréstimo")
        janela.transient(Janela)
        janela.minsize(600, 300)
        janela.maxsize(600, 300)

        topleveldeemprestimo = tkinter.Frame(
             janela,
             width=600,
             height=300,
             bg="gray",
             bd=5,
             relief="solid"
        )
        topleveldeemprestimo.pack(padx=20, pady=20, side="top")
        topleveldeemprestimo.pack_propagate(False)

        titulo = tkinter.Label(topleveldeemprestimo, text="Digite o livro a ser associado ao cpf", font=("Arial", 12, "bold"))
        titulo.pack(padx=0, pady=10, side="top")

        tkinter.Label(topleveldeemprestimo, text="Cpf:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        emprestimo_cpf = ttk.Entry(topleveldeemprestimo)
        emprestimo_cpf.pack(padx=0, pady=10, side="top")

        tkinter.Label(topleveldeemprestimo, text="Livro:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_livro = ttk.Entry(topleveldeemprestimo)
        entrada_livro.pack(padx=0, pady=10, side="top")

        enviar = tkinter.Button(topleveldeemprestimo, text="Associar", command=usuario.emprestar, font=("Arial", 12, "bold"), width=7, height=3)
        enviar.pack(padx=75, side="right")
          
        limpar = tkinter.Button(topleveldeemprestimo, text="Limpar", command=usuario.limpar_campo_associar, font=("Arial", 12, "bold"), width=7, height=3)
        limpar.pack(padx=75, side="left")

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

        titulo = tkinter.Label(topleveldepenalidades, text="Digite o cpf a ser penalizado", font=("Arial", 12, "bold"))
        titulo.pack(padx=0, pady=10, side="top")

        tkinter.Label(topleveldepenalidades, text="cpf:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        busca_cpf = ttk.Entry(topleveldepenalidades)
        busca_cpf.pack(padx=0, pady=10, side="top")

        tkinter.Label(topleveldepenalidades, text="quantia:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
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
    Janela.configure(bg="gray", bd=5, relief="solid")

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
        text="organizador virtual bibliotecário",
        font=("Arial", 25, "bold"),
        wraplength=400,
    )
    Titulo.pack(pady=5)

    Frame_direito = tkinter.Frame(

        Janela, 
        width=350,
        height=300,
        bd=5,
        relief="solid"
    )
    Frame_direito.pack(

        padx=40,
        pady=0,
        side="right"

    )

    Descricao = tkinter.Label(Frame_direito, text="Este organizador serve para que sistemas de bibliotecas sejam admnistrados de maneira dinâmica, serve como um registro de prazos e histórico de cada pessoa a pegar livros emprestados!!!", font=("Arial", 17, "bold"), wraplength=300)

    Descricao.pack(padx=5, pady=20)

    Frame_direito.pack_propagate(False)

    area_botao = tkinter.Frame(

        Janela, 
        width=600, 
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
    botao1.pack(anchor="w")

    botao2 = tkinter.Button(
        area_botao,
        text="Adicionar usuário",
        font=("Arial", 12, "bold"),
        command=usuario.adicionar_usuario,
        width=14,
        height=2,
    )
    botao2.pack(anchor="w")

    botao3 = tkinter.Button(
         area_botao,
         text="Penalizar",
         font=("Arial", 12, "bold"),
         command=usuario.penalizar_por_cpf,
         width=14,
         height=2
    )
    botao3.pack(anchor="w")

    botao4 = tkinter.Button(
         area_botao,
         text="associar-livro",
         font=("Arial", 12, "bold"),
         command=usuario.associar_livro,
         width=14,
         height=2
    )
    botao4.pack(anchor="w")

    Janela.mainloop()

def janela_pontos():

    global usuarios

    janela = tkinter.Toplevel(Janela)
    janela.title("Cadastros")
    janela.transient(Janela)
    janela.minsize(824, 268)
    janela.maxsize(824, 268)

    cadastros = tkinter.Frame(
         janela,
         width=1366,
         height=768,
    )
    cadastros.pack(padx=0, pady=0, side="top")

    tabela = ttk.Treeview(
         cadastros,
         columns=("cpf", "nome", "prazo", "livro", "pontos"),
         show="headings",
    )

    tabela.heading("cpf", text="CPF")
    tabela.heading("nome", text="Nome")
    tabela.heading("prazo", text="Prazo")
    tabela.heading("livro", text="Livro")
    tabela.heading("pontos", text="Pontos")

    tabela.column("cpf", width=120, anchor="center")
    tabela.column("nome", width=180, anchor="center")
    tabela.column("prazo", width=100, anchor="center")
    tabela.column("livro", width=180, anchor="center")
    tabela.column("pontos", width=80, anchor="center")

    with open("Dados.JSON", "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)

    for cpf, dados in usuarios.items():

        tabela.insert(
        "",
        "end",
        values=(
            cpf,
            dados["nome"],
            dados["prazo"],
            dados["livro"],
            dados["pontos"]
        )
    )
    tabela.pack(fill="both", expand=True)

if __name__ == "__main__":
    main()