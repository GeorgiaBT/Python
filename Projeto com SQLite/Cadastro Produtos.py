import pyodbc

from tkinter import *
from tkinter import ttk

def verificacredenciais():

    conexao = pyodbc.connect("Driver={SQLite3 ODBC Driver}; Server=localhost; Database=C:\\Users\\georg\\Documents\\Python - GitHub\\Python\\Projeto com SQLite\\Projeto_compras.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?", (nomeusuarioentry.get(), senhaentry.get()))

    usuario = cursor.fetchall()

    if usuario:

        print("Logado com sucesso!")

        janelaprincipal.destroy()

        def  listadados():

            for linha in treeview.get_children():

                treeview.delete(linha)

            cursor.execute("SELECT * From Produtos")

            valores = cursor.fetchall()

            for valor in valores:

                treeview.insert("", "end", values=(valor[0], valor[1], valor[2], valor[3]))

        janela = Tk()
        janela.title("Cadastro de Produto")

        janela.configure(bg="#F5F5F5")

        #tela cheia
       # janela.attributes("-fullscreen", True)

        Label(janela, text="Nome do Produto", font="Arial 16", bg="#F5F5F5").grid(row=0, column=2, padx=10,pady=10)

        nomeproduto = ttk.Combobox(janela, font="Arial 16")
        nomeproduto.grid(row=0, column=3, padx=10,pady=10, sticky="NSEW")

        #pega valores unicos da coluna nomeproduto e ordena em ordem crescente
        cursor.execute("SELECT DISTINCT NomeProduto FROM Produtos ORDER BY NomeProduto ASC")

        valores = cursor.fetchall()

        nomesprodutos = [valor[0] for valor in valores]

        nomeproduto['values'] = nomesprodutos

        Label(janela, text="Descrição do Produto", font="Arial 16", bg="#F5F5F5").grid(row=0, column=5, padx=10,pady=10)

        descricaoproduto = ttk.Combobox(janela, font="Arial 16")
        descricaoproduto.grid(row=0, column=6, padx=10, pady=10, sticky="NSEW")

        cursor.execute("SELECT DISTINCT descricao FROM Produtos ORDER BY descricao ASC")

        valoresdescricao = cursor.fetchall()

        descricao_produtos = [valor[0] for valor in valoresdescricao]

        descricaoproduto['values'] = descricao_produtos

        def cadastrar():

            janelacadastrar = Toplevel(janela)
            janelacadastrar.title("Cadastrar Produto")
            janelacadastrar.config(bg="#FFFFFF")

            largurajanela = 500
            alturajanela = 300

            larguratela = janelacadastrar.winfo_screenmmwidth()
            alturatela = janelacadastrar.winfo_screenheight()

            pos_x = (larguratela // 2) - (largurajanela // 2)
            pos_y = (alturatela // 2) - (alturajanela // 2)

            janelacadastrar.geometry('{}x{}+{}+{}'.format(largurajanela, alturajanela, pos_x, pos_y))

            Label(janelacadastrar, text="Nome do Produto", font="Arial 12", bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, sticky="W")

            nomeprodutocadastrar = Entry(janelacadastrar, font="Arial 12")
            nomeprodutocadastrar.grid(row=0, column=1, padx=10,pady=10)

            Label(janelacadastrar, text="Descrição do Produto", font="Arial 12", bg="#FFFFFF").grid(row=1, column=0, padx=10,                                                                                 pady=10, sticky="W")

            descricaoprodutocadastrar = Entry(janelacadastrar, font="Arial 12")
            descricaoprodutocadastrar.grid(row=1, column=1, padx=10, pady=10)

            Label(janelacadastrar, text="Preço do Produto", font="Arial 12", bg="#FFFFFF").grid(row=2, column=0, padx=10,pady=10, sticky="W")

            precoprodutocadastrar = Entry(janelacadastrar, font="Arial 12")
            precoprodutocadastrar.grid(row=2, column=1, padx=10, pady=10)

            def salvardados():

                #tupla
                novoprodutocadastrar = (nomeprodutocadastrar.get(), descricaoprodutocadastrar.get(), precoprodutocadastrar.get())

                #executa um comando sql para inserir os dados na tabela de produtos
                cursor.execute("INSERT INTO Produtos (NomeProduto, descricao, Preco) VALUES (?,?,?)",(novoprodutocadastrar))

                conexao.commit()

                listadados()


                # Atualiza a lista de valores na Combobox de descrição do produto

                cursor.execute("SELECT DISTINCT NomeProduto FROM Produtos ORDER BY NomeProduto ASC")
                valores = cursor.fetchall()
                nomesprodutos = [valor[0] for valor in valores]
                nomeproduto['values'] = nomesprodutos

                cursor.execute("SELECT DISTINCT descricao FROM Produtos ORDER BY descricao ASC")
                valoresdescricao = cursor.fetchall()
                descricao_produtos = [valor[0] for valor in valoresdescricao]
                descricaoproduto['values'] = descricao_produtos
                #chama a funcao para listar os dados e mostrar na treeview
                listadados()

                janelacadastrar.destroy()

                calculasoma()

            botaosalvardados = Button(janelacadastrar, text="Salvar", command=salvardados, font="Arial 20")
            botaosalvardados.grid(row=4, column=0, columnspan=2, sticky="NSEW", pady=5, padx=5)

            botaocancelar = Button(janelacadastrar, text="Cancelar", command=janelacadastrar.destroy, font="Arial 20")
            botaocancelar.grid(row=5, column=0, columnspan=2, sticky="NSEW", pady=5, padx=5)

            for i in range(5):
                janelacadastrar.grid_rowconfigure(i, weight=1)
            for i in range(2):
                janelacadastrar.grid_columnconfigure(i, weight=1)

        botaogravar = Button(janela, text="Novo", command=cadastrar, font="Arial 26")
        botaogravar.grid(row=5, column=0, columnspan=4, sticky="NSEW", pady=5)

        style = ttk.Style(janela)

        treeview = ttk.Treeview(janela, style="mystyle.Treeview")
        style.theme_use("default")
        style.configure("mystyle.Treeview", font="Arial 14")

        colunas = ["ID", "Nome do Produto", "Descrição", "Preço"]
        treeview["columns"] = colunas

        listadados()

        for col in colunas:

            treeview.heading(col, text= col)


        treeview.grid(row=4, column=0, columnspan=10, padx=5,pady=5, sticky="NSEW")

        #oculta primeira coluna
        treeview.column("#0", width=0, stretch=False)

        def limpadados():

            for linha in treeview.get_children():

                treeview.delete(linha)

        somalabel = Label(janela, text="Total: R$ 0.00", font="Arial 20", bg="#FFFFFF")
        somalabel.grid(row=3, column=0, columnspan=10, sticky="NSEW", padx=10, pady=10)

        def calculasoma():

            total = 0
            qtdregistros = 0

            for linha in treeview.get_children():

                valores = treeview.item(linha)['values']

                if valores:

                    total += float(valores[3])
                    qtdregistros += 1

                somalabel.config(text=f"Total: R$ {total:.2f} - Itens: {qtdregistros}")

        calculasoma()

        def editardados(event):

            itemselecionado = treeview.selection()[0]

            valoresselecionados = treeview.item(itemselecionado)['values']

            janelaedicao = Toplevel(janela)
            janelaedicao.title("Editar Produto")
            janelaedicao.config(bg="#FFFFFF")

            largurajanela = 500
            alturajanela = 300

            larguratela = janelaedicao.winfo_screenmmwidth()
            alturatela = janelaedicao.winfo_screenheight()

            pos_x = (larguratela // 2) - (largurajanela // 2)
            pos_y = (alturatela // 2) - (alturajanela // 2)


            janelaedicao.geometry('{}x{}+{}+{}'.format(largurajanela, alturajanela, pos_x, pos_y))

            Label(janelaedicao, text="Nome do Produto", font="Arial 12", bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, sticky="W")

            nomeprodutoedicao = Entry(janelaedicao, font="Arial 12", textvariable=StringVar(value=valoresselecionados[1]))
            nomeprodutoedicao.grid(row=0, column=1, padx=10,pady=10)

            Label(janelaedicao, text="Descrição do Produto", font="Arial 12", bg="#FFFFFF").grid(row=1, column=0, padx=10,                                                                                 pady=10, sticky="W")

            descricaoprodutoedicao = Entry(janelaedicao, font="Arial 12", textvariable=StringVar(value=valoresselecionados[2]))
            descricaoprodutoedicao.grid(row=1, column=1, padx=10, pady=10)

            Label(janelaedicao, text="Preço do Produto", font="Arial 12", bg="#FFFFFF").grid(row=2, column=0, padx=10,pady=10, sticky="W")

            precoprodutoedicao = Entry(janelaedicao, font="Arial 12", textvariable=StringVar(value=valoresselecionados[3]))
            precoprodutoedicao.grid(row=2, column=1, padx=10, pady=10)

            def salvaredicao():

                #tupla
                novonome = nomeprodutoedicao.get()
                novadescricao = descricaoprodutoedicao.get()
                novopreco = precoprodutoedicao.get()

                treeview.item(itemselecionado, values=(valoresselecionados[0], novonome, novadescricao, novopreco))

                #executa um comando sql para inserir os dados na tabela de produtos
                cursor.execute("UPDATE Produtos SET NomeProduto = ?, descricao = ?, Preco = ? WHERE ID = ?",
                               (novonome, novadescricao, novopreco, valoresselecionados[0]))

                conexao.commit()

                cursor.execute("SELECT DISTINCT NomeProduto FROM Produtos ORDER BY NomeProduto ASC")
                valores = cursor.fetchall()
                nomesprodutos = [valor[0] for valor in valores]
                nomeproduto['values'] = nomesprodutos

                cursor.execute("SELECT DISTINCT descricao FROM Produtos ORDER BY descricao ASC")
                valoresdescricao = cursor.fetchall()
                descricao_produtos = [valor[0] for valor in valoresdescricao]
                descricaoproduto['values'] = descricao_produtos
                # chama a funcao para listar os dados e mostrar na treeview
                listadados()

                calculasoma()

                # Atualiza a lista de valores na Combobox de descrição do produto

                janelaedicao.destroy()

            botaosalvaredicao = Button(janelaedicao, text="Editar", command=salvaredicao, font="Arial 16", bg="#008000",fg="#FFFFFF")
            botaosalvaredicao.grid(row=4, column=0, pady=20, padx=20)

            def deletaritem():

                #recupera id do registro
                selecteditem = treeview.selection()[0]

                idselecionado = treeview.item(selecteditem)['values'][0]

                #deleta registro do banco de dados
                cursor.execute("DELETE FROM Produtos WHERE Id=?", (idselecionado))

                conexao.commit()

                janelaedicao.destroy()

                listadados()

                calculasoma()

            botaodeletar = Button(janelaedicao, text="Excluir", command=deletaritem, font="Arial 16", bg="#FF0000",fg="#FFFFFF")
            botaodeletar.grid(row=4, column=1, pady=20, padx=20)

            for i in range(5):
                janelaedicao.grid_rowconfigure(i, weight=1)
            for i in range(2):
                janelaedicao.grid_columnconfigure(i, weight=1)

            #botaocancelaredicao = Button(janelaedicao, text="Cancelar", command=janelaedicao.destroy, font="Arial 20")
            #botaocancelaredicao.grid(row=5, column=0, columnspan=2, sticky="NSEW", pady=5, padx=5)


        treeview.bind("<Double-1>", editardados)

        def filtrardados(nomeproduto, descricaoproduto):

            if nomeproduto.get() == "" and descricaoproduto.get() == "":

                listadados()

                calculasoma()

                return

            #monta a consulta sql dinamicamente
            sql = "SELECT * FROM Produtos"

            params = []

            if nomeproduto.get():

                sql += " WHERE NomeProduto LIKE ?"
                params.append('%' + nomeproduto.get()+'%')

            if descricaoproduto.get():

                if nomeproduto.get():

                    sql += " AND"

                else:

                    sql += " WHERE"
                sql += " descricao LIKE ?"
                params.append('%' + descricaoproduto.get() + '%')

            cursor.execute(sql, tuple(params))
            produtos = cursor.fetchall()

            limpadados()


            for dados in produtos:

                treeview.insert("", "end", values=(dados[0], dados[1], dados[2], dados[3]))

            calculasoma()

        nomeproduto.bind('<KeyRelease>', lambda e: filtrardados(nomeproduto, descricaoproduto))
        descricaoproduto.bind('<KeyRelease>', lambda e: filtrardados(nomeproduto, descricaoproduto))

        nomeproduto.bind('<<ComboboxSelected>>', lambda e: filtrardados(nomeproduto, descricaoproduto))
        descricaoproduto.bind('<<ComboboxSelected>>', lambda e: filtrardados(nomeproduto, descricaoproduto))

        def deletar():

            # recupera id do registro
            selecteditem = treeview.selection()[0]

            idselecionado = treeview.item(selecteditem)['values'][0]

            # deleta registro do banco de dados
            cursor.execute("DELETE FROM Produtos WHERE Id=?", (idselecionado))

            conexao.commit()

            listadados()

            calculasoma()

        botaodeletar = Button(janela, text="Deletar", command=deletar, font="Arial 26")
        botaodeletar.grid(row=5, column=4, columnspan=4, sticky="NSEW", pady=5)

        #configura a janela para utilizar a barra de menu criada
        menubarra = Menu(janela)
        janela.config(menu=menubarra)

        menuarquivo = Menu(menubarra, tearoff=0)
        menubarra.add_cascade(label="Arquivo", menu=menuarquivo)

        menuarquivo.add_command(label="Cadastrar", command=janela.destroy)

        menuarquivo.add_command(label="Sair", command=janela.destroy)

        janela.mainloop()

        cursor.close()
        conexao.close()

    else:

        msg_label = Label(janelaprincipal, text="Nome de usuário ou senha incorreta",
                          fg="red")
        msg_label.grid(row=3, column=0, columnspan=2)

janelaprincipal = Tk()
janelaprincipal.title("Tela de login")
janelaprincipal.config(bg="#F5F5F5")

largurajanela = 450
alturajanela = 300

larguratela = janelaprincipal.winfo_screenmmwidth()
alturatela = janelaprincipal.winfo_screenheight()

pos_x = (larguratela//2) - (largurajanela//2)
pos_y = (alturatela//2) - (alturajanela//2)

janelaprincipal.geometry('{}x{}+{}+{}'.format(largurajanela, alturajanela, pos_x, pos_y))

titulolbl = Label(janelaprincipal, text="Tela de Login",
                  font="Arial 20",
                  fg="blue",
                  bg="#F5F5F5")
titulolbl.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

nomeusuariolbl = Label(janelaprincipal, text="Nome do Usuário:",
                  font="Arial 14",
                  fg="black",
                  bg="#F5F5F5")
nomeusuariolbl.grid(row=1, column=0, sticky="e")

senhausuariolbl = Label(janelaprincipal, text="Senha:",
                  font="Arial 14",
                  fg="black",
                  bg="#F5F5F5")
senhausuariolbl.grid(row=2, column=0, sticky="e")

nomeusuarioentry = Entry(janelaprincipal, font="Arial 18")
nomeusuarioentry.grid(row=1, column=1, pady=10)

senhaentry = Entry(janelaprincipal, font="Arial 18", show="*")
senhaentry.grid(row=2, column=1, pady=10)

entrarbtn = Button(janelaprincipal, text="Entrar", font="Arial 14", command=verificacredenciais)
entrarbtn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")

sairbtn = Button(janelaprincipal, text="Sair", font="Arial 14", command=janelaprincipal.destroy)
sairbtn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")

#centralizar os widgets na janela
for i in range(5):
    janelaprincipal.grid_rowconfigure(i, weight=1)
for i in range(2):
        janelaprincipal.grid_columnconfigure(i, weight=1)

entrarbtn.config(width=10)
sairbtn.config(width=10)

janelaprincipal.mainloop()