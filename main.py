import tkinter
from tkinter import ttk, messagebox
import json
from datetime import datetime, timedelta
usuarios = {}
Janela = None
entrada_nome = None
entrada_telefone = None
entrada_pontos = None
entrada_livro = None
entrada_cpf = None
class usuario:

    def __init__(self):

        pass

    def definir_usuario():
        
        global usuarios, entrada_nome, entrada_cpf, entrada_telefone

        try:
            with open("Dados.JSON", "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)
        except:
            with open("Dados.JSON", "w", encoding="utf-8") as arquivo:
                        json.dump({},arquivo)
            
            with open("Dados.JSON", "r", encoding="utf-8") as arquivo:
                    usuarios = json.load(arquivo)
        cpf = entrada_cpf.get()
        telefone = entrada_telefone.get()
        nome = entrada_nome.get()
        if entrada_cpf.get() == "":
             messagebox.showerror("Erro", "É necessário digitar\n um cpf")
             return
        if len(cpf) != 11:
            messagebox.showerror("Erro", "O CPF deve conter 11 dígitos")
            return
        if entrada_telefone.get() == "":
             messagebox.showerror("Erro", "É necessário digitar\n um telefone")
             return
        if len(telefone) not in (10, 11):
            messagebox.showerror(
        "Erro",
        "O telefone deve conter 10 ou 11 dígitos"
            )
            return
        if cpf in usuarios:
            messagebox.showerror(
            "Erro",
            "Já existe um usuário cadastrado com este CPF."
        )
            return
        if not telefone.isdigit():
            messagebox.showerror(
                "Erro",
                "O telefone deve conter apenas números."
            )
            return
        if not cpf.isdigit():
            messagebox.showerror(
                "Erro",
                "O CPF deve conter apenas números."
            )
            return
        if nome and not nome.replace(" ", "").isalpha():
            messagebox.showerror(
                "Erro",
                "O nome deve conter apenas letras."
            )
            return
        usuarios[cpf] = {
                    "nome": entrada_nome.get(),
                    "prazo": f"{0} dias",
                    "livro": "Nenhum",
                    "pontos": int(0),
                    "telefone": entrada_telefone.get()
                }
        with open("Dados.JSON", "w", encoding="utf-8") as Dados_usuarios:
            json.dump(usuarios, Dados_usuarios, ensure_ascii=False, indent=2)

        entrada_nome.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)
        entrada_telefone.delete(0, tkinter.END)
        messagebox.showinfo("Parabéns", "cadastro concluido")

    def limpar_campo_cadastro():

        entrada_nome.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)
        entrada_telefone.delete(0, tkinter.END)

    def limpar_campo_penalidades():
         
         entrada_pontos.delete(0, tkinter.END)
         entrada_cpf.delete(0, tkinter.END)

    def limpar_campo_associar():
         
         entrada_livro.delete(0, tkinter.END)
         entrada_cpf.delete(0, tkinter.END)

    def limpar_campo_devolver():

         entrada_cpf.delete(0, tkinter.END)
         

    def emprestar():

        global usuarios, entrada_cpf, entrada_livro

        with open("Dados.JSON", "r") as arquivo:
             usuarios = json.load(arquivo)

        cpf = entrada_cpf.get()
        livro = entrada_livro.get()
        prazo = datetime.now() + timedelta(seconds=15)

        if cpf == "":
            messagebox.showerror(
                "Erro",
                "Informe um CPF."
            )
            return

        if livro == "":
            messagebox.showerror(
                "Erro",
                "Informe o nome do livro."
            )
            return

        if cpf not in usuarios:
            messagebox.showerror(
                "Erro",
                "Nenhum usuário encontrado para o CPF informado."
            )
            return

        if usuarios[cpf]["livro"] != "Nenhum":
            messagebox.showerror(
                "Erro",
                "Este usuário já possui um livro emprestado."
            )
            return

        for cpf_ocupante in usuarios:
            if usuarios[cpf_ocupante]["livro"] == livro:
                messagebox.showerror(
                    "Erro",
                    "Este livro já está emprestado."
                )
                return

        usuarios[cpf]["livro"] = livro
        usuarios[cpf]["prazo"] = prazo.strftime("%Y-%m-%d %H:%M:%S")

        with open("Dados.JSON", "w", encoding="utf-8") as arquivo:
                json.dump(usuarios,arquivo, ensure_ascii=False, indent=2)


        entrada_livro.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)
        
        messagebox.showinfo(
    "Sucesso",
    "Livro emprestado com sucesso."
)

    def add_pontos():

        global usuarios

        with open("Dados.JSON", "r") as arquivo:
             usuarios = json.load(arquivo)

        cpf = entrada_cpf.get()
        pontos = entrada_pontos.get()

        if cpf == "":
            messagebox.showerror(
                "Erro",
                "Informe um CPF."
            )
            return

        if entrada_pontos.get() == "":
            messagebox.showerror(
                "Erro",
                "Informe a quantidade de pontos."
            )
            return

        try:
            pontos = int(entrada_pontos.get())
        except ValueError:
            messagebox.showerror(
                "Erro",
                "Informe um número inteiro."
            )
            return
        if cpf not in usuarios:
                    messagebox.showerror(
                        "Erro",
                        "Nenhum usuário encontrado para o CPF informado."
                    )
                    return

        if pontos <= 0:
            messagebox.showerror(
                "Erro",
                "Os pontos devem ser maiores que zero."
            )
            return
        
        usuarios[cpf]["pontos"] += pontos
         
        with open("Dados.JSON", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, ensure_ascii=False, indent=2)

        entrada_pontos.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)  

        messagebox.showinfo(
    "Sucesso",
    f"Penalidade aplicada com sucesso\n pontos atuais do cpf: {usuarios[cpf]["pontos"]}."
)
    def remove_pontos():
    
        global usuarios
    
        with open("Dados.JSON", "r") as arquivo:
            usuarios = json.load(arquivo)
    
        cpf = entrada_cpf.get()
        pontos = entrada_pontos.get()

        if cpf == "":
            messagebox.showerror(
                "Erro",
                "Informe um CPF."
            )
            return

        if entrada_pontos.get() == "":
            messagebox.showerror(
                "Erro",
                "Informe a quantidade de pontos."
            )
            return

        try:
            pontos = int(entrada_pontos.get())
        except ValueError:
            messagebox.showerror(
                "Erro",
                "Informe um número inteiro."
            )
            return
        
        if cpf not in usuarios:
                    messagebox.showerror(
                        "Erro",
                        "Nenhum usuário encontrado para o CPF informado."
                    )
                    return

        if pontos <= 0:
            messagebox.showerror(
                "Erro",
                "Os pontos devem ser maiores que zero."
            )
            return
        if usuarios[cpf]["pontos"] < pontos:
            messagebox.showerror(
                "Erro",
                "O usuário não possui essa quantidade de pontos."
            )
            return

        usuarios[cpf]["pontos"] -= pontos
    
        with open("Dados.JSON", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, ensure_ascii=False, indent=2)
    
        entrada_pontos.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END) 
        
        messagebox.showinfo(
    "Sucesso",
    f"Penalidade removida com sucesso\n pontos atuais do cpf: {usuarios[cpf]["pontos"]}"
)            

    def adicionar_usuario():

        global entrada_nome, entrada_cpf, entrada_telefone

        janela = tkinter.Toplevel(Janela)
        janela.title("Usuário")
        janela.transient(Janela)
        janela.minsize(600, 350)
        janela.maxsize(600, 350)

        toplevelcadastro = tkinter.Frame(

            janela, 
            width=600, 
            height=300,
            bd=5,
            bg="gray",
            relief="solid"

        )
        toplevelcadastro.pack(padx=20, pady=20, side="top")
        toplevelcadastro.pack_propagate(False)

        titulo = tkinter.Label(toplevelcadastro, text="Digite o usuário", font=("Arial", 12, "bold"))
        titulo.pack(padx=0, pady=10, side="top")


        tkinter.Label(toplevelcadastro, text="Cpf:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_cpf = ttk.Entry(toplevelcadastro)
        entrada_cpf.pack(padx=0, pady=10, side="top")

        tkinter.Label(toplevelcadastro, text="Telefone:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_telefone = ttk.Entry(toplevelcadastro)
        entrada_telefone.pack(padx=0, pady=10, side="top")

        tkinter.Label(toplevelcadastro, text="Nome: (opcional)", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_nome = ttk.Entry(toplevelcadastro)
        entrada_nome.pack(padx=0, pady=10, side="top")

        enviar = tkinter.Button(toplevelcadastro, text="Cadastrar", command=usuario.definir_usuario, font=("Arial", 12, "bold"), width=7, height=3)
        enviar.pack(padx=10, side="right")

        remover = tkinter.Button(toplevelcadastro, text="Remover", command=usuario.remover_usuario, font=("Arial", 12, "bold"), width=7, height=3)
        remover.pack(padx=10, side="right")

        limpar = tkinter.Button(toplevelcadastro, text="Limpar", command=usuario.limpar_campo_cadastro, font=("Arial", 12, "bold"), width=7, height=3)
        limpar.pack(padx=65, side="left")

    def associar_livro():

        global entrada_livro, entrada_cpf

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
        entrada_cpf = ttk.Entry(topleveldeemprestimo)
        entrada_cpf.pack(padx=0, pady=10, side="top")

        tkinter.Label(topleveldeemprestimo, text="Livro:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_livro = ttk.Entry(topleveldeemprestimo)
        entrada_livro.pack(padx=0, pady=10, side="top")

        enviar = tkinter.Button(topleveldeemprestimo, text="Associar", command=usuario.emprestar, font=("Arial", 12, "bold"), width=7, height=3)
        enviar.pack(padx=75, side="right")
          
        limpar = tkinter.Button(topleveldeemprestimo, text="Limpar", command=usuario.limpar_campo_associar, font=("Arial", 12, "bold"), width=7, height=3)
        limpar.pack(padx=75, side="left")

    def penalizar_por_cpf():

        global entrada_pontos, entrada_cpf

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

        titulo = tkinter.Label(topleveldepenalidades, text="Digite o cpf e os pontos", font=("Arial", 12, "bold"))
        titulo.pack(padx=0, pady=10, side="top")

        tkinter.Label(topleveldepenalidades, text="Cpf:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_cpf = ttk.Entry(topleveldepenalidades)
        entrada_cpf.pack(padx=0, pady=10, side="top")

        tkinter.Label(topleveldepenalidades, text="Quantia:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_pontos = ttk.Entry(topleveldepenalidades)
        entrada_pontos.pack(padx=0, pady=10, side="top")

        enviar = tkinter.Button(topleveldepenalidades, text="Penalizar", command=usuario.add_pontos, font=("Arial", 12, "bold"), width=7, height=3)
        enviar.pack(padx=10, side="right")

        remover = tkinter.Button(topleveldepenalidades, text="Remover", command=usuario.remove_pontos, font=("Arial", 12, "bold"), width=7, height=3)
        remover.pack(padx=10, side="right")

        limpar = tkinter.Button(topleveldepenalidades, text="Limpar", command=usuario.limpar_campo_penalidades, font=("Arial", 12, "bold"), width=7, height=3)
        limpar.pack(padx=65, side="left")

    def devolver():

        global usuarios
        
        with open("Dados.JSON", "r") as arquivo:
             usuarios = json.load(arquivo)
        
        cpf = entrada_cpf.get()
        
        if cpf == "":
            messagebox.showerror(
                "Erro",
                "Informe um CPF."
            )
            return

        if cpf not in usuarios:
            messagebox.showerror(
                "Erro",
                "Nenhum usuário encontrado para o CPF informado."
            )
            return

        if usuarios[cpf]["livro"] == "Nenhum":
            messagebox.showerror(
                "Erro",
                "Este usuário não possui empréstimos ativos."
            )
            return

        usuarios[cpf]["livro"] = "Nenhum"
        usuarios[cpf]["prazo"] = "0 dias"
        
        with open("Dados.JSON", "w", encoding="utf-8") as arquivo:
                json.dump(usuarios, arquivo, ensure_ascii=False, indent=2)
        
        entrada_cpf.delete(0, tkinter.END)
        
        messagebox.showinfo(
    "Sucesso",
    "Livro devolvido com sucesso."
)

    def devolver_livro():

        global entrada_cpf

        janela = tkinter.Toplevel(Janela)
        janela.title("Devolução")
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
        
        titulo = tkinter.Label(topleveldeemprestimo, text="Digite o cpf que realizou a devolução", font=("Arial", 12, "bold"))
        titulo.pack(padx=0, pady=20, side="top")
        
        tkinter.Label(topleveldeemprestimo, text="Cpf:", font=("Arial", 12, "bold")).pack(padx=0, side="top")
        entrada_cpf = ttk.Entry(topleveldeemprestimo)
        entrada_cpf.pack(padx=0, pady=20, side="top")
        
        devolver = tkinter.Button(topleveldeemprestimo, text="Devolver", command=usuario.devolver, font=("Arial", 12, "bold"), width=7, height=3)
        devolver.pack(padx=75, side="right")
                  
        limpar = tkinter.Button(topleveldeemprestimo, text="Limpar", command=usuario.limpar_campo_devolver, font=("Arial", 12, "bold"), width=7, height=3)
        limpar.pack(padx=75, side="left")

    def remover_usuario():
        
        global usuarios
        
        with open("Dados.JSON", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)

        cpf = entrada_cpf.get()

        if cpf == "":
            messagebox.showerror(
                "Erro",
                "Informe um CPF."
            )
            return

        if cpf not in usuarios:
            messagebox.showerror(
                "Erro",
                "Nenhum usuário encontrado para o CPF informado."
            )
            return
        if usuarios[cpf]["livro"] != "Nenhum":
            messagebox.showerror(
                "Erro",
                "Este usuário possue um empréstimo"
            )
            return
        
        del usuarios[cpf]

        entrada_nome.delete(0, tkinter.END)
        entrada_cpf.delete(0, tkinter.END)
        entrada_telefone.delete(0, tkinter.END)

        with open("Dados.JSON", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, ensure_ascii=False, indent=2)
            
        messagebox.showinfo(
    "Sucesso",
    "Usuário removido com sucesso."
)

    def verificar_prazos():

        global usuarios

        with open("Dados.JSON", "r") as arquivo:
                usuarios = json.load(arquivo)
        
        for cpf in usuarios:

            if usuarios[cpf]["prazo"] != "0 dias":

                if usuarios[cpf]["prazo"] in ("0 dias", "Em atraso"):
                    continue

                prazo = datetime.strptime(
                usuarios[cpf]["prazo"],
                "%Y-%m-%d %H:%M:%S"
            )

                if datetime.now() >= prazo:

                    usuarios[cpf]["pontos"] += 1
                    usuarios[cpf]["prazo"] = "Em atraso"

        with open("Dados.JSON", "w", encoding="utf-8") as arquivo:
           json.dump(usuarios, arquivo, indent=2)

    def atualizar():
        usuario.verificar_prazos()
        Janela.after(1000, usuario.atualizar)

def main():
                
    global Janela

    Janela = tkinter.Tk()
    Janela.title("Janela principal")
    Janela.geometry("1024x720")
    Janela.minsize(960, 720)
    Janela.maxsize(960, 720)
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
        padx=40, 
        side="top"

    )

    Head.pack_propagate(False)

    Titulo = ttk.Label(
        Head,
        text="organizador virtual bibliotecário",
        font=("Arial", 25, "bold"),
        wraplength=400,
    )
    Titulo.pack(pady=5, padx=40, side="left")

    Frame_direito = tkinter.Frame(

        Janela, 
        width=350,
        height=270,
        bd=5,
        relief="solid"
    )
    Frame_direito.pack(

        padx=40,
        pady=0,
        side="right"

    )

    Descricao = tkinter.Label(Frame_direito, text="Este organizador serve para que sistemas de bibliotecas sejam admnistradas de maneira dinâmica. Serve como um meio de controle para aquelas pessoas que forem pegar livros emprestados!!!", font=("Arial", 17, "bold"), wraplength=330)

    Descricao.pack(padx=5, pady=20)

    Frame_direito.pack_propagate(False)

    area_botao = tkinter.Frame(

        Janela, 
        width=150, 
        height=270,
        bd=5,
        relief="solid"
    )
    area_botao.pack(

        pady=0, 
        padx=50, 
        side="left"

    )

    area_botao.pack_propagate(False)

    area_explicacao = tkinter.Frame(

        Janela,
        width=300,
        height=270,
        bd=5,
        relief="solid"
    )
    area_explicacao.pack(
         
        
        side="left"
    )

    area_explicacao.pack_propagate(False)

    explicacao_cadastros = tkinter.Frame(

         area_explicacao,
         width=300,
         height=54,
         bd=1,
         relief="solid"
    )
    explicacao_cadastros.pack(side="top")
    explicacao_cadastros.pack_propagate(False)

    Label_cadastros = tkinter.Label(
         explicacao_cadastros,
         text="Analise de dados\n e prazos em tempo real",
         font=("Arial", 12)
    )
    Label_cadastros.pack(padx=5, pady=5)

    explicacao_usuario = tkinter.Frame(
    
            area_explicacao,
            width=300,
            height=54,
            bd=1,
            relief="solid"
    )
    explicacao_usuario.pack(side="top")
    explicacao_usuario.pack_propagate(False)

    Label_usuario = tkinter.Label(
             explicacao_usuario,
             text="Cadastro e remoção\n através do CPF",
             font=("Arial", 12)
        )
    Label_usuario.pack(padx=5, pady=5)

    explicacao_penalidade = tkinter.Frame(
    
             area_explicacao,
             width=300,
             height=54,
             bd=1,
             relief="solid"
        )
    explicacao_penalidade.pack(side="top")
    explicacao_penalidade.pack_propagate(False)

    Label_penalidade = tkinter.Label(
                 explicacao_penalidade,
                 text="Adição ou remoção\n de penalidades",
                 font=("Arial", 12)
            )
    Label_penalidade.pack(padx=5, pady=5)

    explicacao_associar = tkinter.Frame(
    
             area_explicacao,
             width=300,
             height=54,
             bd=1,
             relief="solid"
        )
    explicacao_associar.pack(side="top")
    explicacao_associar.pack_propagate(False)

    Label_associar = tkinter.Label(
             explicacao_associar,
             text="Empréstimo de livro\n por CPF",
             font=("Arial", 12)
        )
    Label_associar.pack(padx=5, pady=5)

    explicacao_devolver = tkinter.Frame(
    
            area_explicacao,
            width=300,
            height=54,
            bd=1,
            relief="solid"
    )
    explicacao_devolver.pack(side="top")
    explicacao_devolver.pack_propagate(False)

    Label_devolver = tkinter.Label(
             explicacao_devolver,
             text="Devolução por informe\n de CPF",
             font=("Arial", 12)
        )
    Label_devolver.pack(padx=5, pady=5)

    botao1 = tkinter.Button(
        area_botao,
        text="Usuários",
        font=("Arial", 12, "bold"),
        command=janela_pontos,
        width=14,
        height=2,
    )
    botao1.pack(anchor="w")

    botao2 = tkinter.Button(
        area_botao,
        text="Cadastrar",
        font=("Arial", 12, "bold"),
        command=usuario.adicionar_usuario,
        width=14,
        height=2,
    )
    botao2.pack(anchor="w")

    botao3 = tkinter.Button(
         area_botao,
         text="Pontos",
         font=("Arial", 12, "bold"),
         command=usuario.penalizar_por_cpf,
         width=14,
         height=2
    )
    botao3.pack(anchor="w")

    botao4 = tkinter.Button(
         area_botao,
         text="Associar livro",
         font=("Arial", 12, "bold"),
         command=usuario.associar_livro,
         width=14,
         height=2
    )
    botao4.pack(anchor="w")

    botao5 = tkinter.Button(
             area_botao,
             text="Devolução livro",
             font=("Arial", 12, "bold"),
             command=usuario.devolver_livro,
             width=14,
             height=2
        )
    botao5.pack(anchor="w")

    
    usuario.atualizar()
    Janela.mainloop()

def janela_pontos():

    global usuarios

    try:
        with open("Dados.JSON", "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)
    except:
        with open("Dados.JSON", "w", encoding="utf-8") as arquivo:
                json.dump({},arquivo)
        with open("Dados.JSON", "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)

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
         columns=("cpf", "nome", "prazo", "livro", "pontos","telefone"),
         show="headings",
    )

    tabela.heading("cpf", text="CPF")
    tabela.heading("nome", text="Nome")
    tabela.heading("prazo", text="Prazo")
    tabela.heading("livro", text="Livro")
    tabela.heading("pontos", text="Pontos")
    tabela.heading("telefone", text="Telefone")

    tabela.column("cpf", width=100, anchor="center")
    tabela.column("nome", width=100, anchor="center")
    tabela.column("prazo", width=150, anchor="center")
    tabela.column("livro", width=150, anchor="center")
    tabela.column("pontos", width=80, anchor="center")
    tabela.column("telefone", width=100, anchor="center")

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
            dados["pontos"],
            dados["telefone"]
        )
    )
    tabela.pack(fill="both", expand=True)




if __name__ == "__main__":
    main()